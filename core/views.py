from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pydub import AudioSegment
from pydub.silence import split_on_silence
from uuid import uuid4
from config import settings
import speech_recognition as sr

def main(request):
    if request.method == 'POST' and request.FILES['file']:
        audio_file = request.FILES['file']
        fs = FileSystemStorage()
        file_name = fs.save('temp/' + str(uuid4()) + '.mp3', audio_file)
        file_path = fs.path(file_name)

        chunks = split_file(file_path)

        transcriptions = [transcribe_audio(chunk) for chunk in chunks]
        print(transcriptions)
        text = process_transcription(transcriptions)

        return render(request, 'index.html', {'text': text, 'is_posted': True, 'audio_files': chunks})
    return render(request, 'index.html', {'text': "transcription will appear here"})

def split_file(file_path):
    # Convert MP3 to WAV
    audio = AudioSegment.from_mp3(file_path)
    audio = audio.set_channels(1)  
    audio = audio.set_frame_rate(16000)  
    wav_path = file_path[:-4] + ".wav"  
    audio.export(wav_path, format="wav")

    audio = AudioSegment.from_wav(wav_path)
    chunks = split_on_silence(audio, min_silence_len=1000, silence_thresh=-40)

    output_files = []
    for i, chunk in enumerate(chunks):
        chunk_file = f"media/chunk_{i}.wav"
        chunk.export(chunk_file, format="wav")
        output_files.append(chunk_file)
    
    return output_files

def transcribe_audio(chunk):
    recognizer = settings.SPEECH_RECOGNIER
    with sr.AudioFile(chunk) as source:
        audio = recognizer.record(source)
    text = recognizer.recognize_google(audio, language="en-US")
    return text

def process_transcription(transcription):
    text = ""
    for segment in transcription:
        text += segment.strip() + "\n"
    return text
