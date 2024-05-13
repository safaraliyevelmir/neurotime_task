from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from pydub import AudioSegment
from pydub.silence import split_on_silence
from uuid import uuid4
from config import settings

def main(request):
    if request.method == 'POST' and request.FILES['file']:
        audio_file = request.FILES['file']
        fs = FileSystemStorage()
        file_name = fs.save('temp/' + str(uuid4()) + '.mp3', audio_file)
        file_path = fs.path(file_name)
        
        chunks = split_file(file_path)
        transcriptions = [transcribe_audio(chunk) for chunk in chunks]
        text = process_transcription(transcriptions)

        return render(request, 'index.html', {'text': text})
    return render(request, 'index.html', {'text': "trasncription will appear here"})

def split_file(file_path):
    audio = AudioSegment.from_file(file_path, format="mp3")
    chunks = split_on_silence(audio, min_silence_len=100, silence_thresh=-40)

    output_files = []
    for i, chunk in enumerate(chunks):
        chunk_file = f"temp/chunk_{i}.mp3"
        chunk.export(chunk_file, format="mp3")
        output_files.append(chunk_file)
    return output_files

def transcribe_audio(file_path):
    segments, info = settings.WISHPER_MODEL.transcribe(file_path)
    return segments

def process_transcription(transcription):
    text = ""
    for segment in transcription:
        for sentence in segment:
            text += sentence.text.strip() + " "
        text += "\n"
    return text
