# Django Speech Transcription Project

This project is created using Django for transcribing speech audio files.

## Requirements

- Python 3.x
- Django
- pydub
- Whisper model

## How to Run

1. Install Python (https://www.python.org/downloads/)
2. Clone the project: `git clone https://github.com/safaraliyevelmir/neurotime_task.git`
3. Navigate to the project directory: `cd neurotime_task`
4. Create a virtual environment (optional): `python -m venv venv`
5. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
6. Install the requirements: `pip install -r requirements.txt`
8. Start the server: `python manage.py runserver`

## About the Project

This project is used to automatically transcribe speech audio files. The audio files are processed using the pydub library and split based on silence intervals. Then, the OpenAI Whisper model is used for transcription. This model includes a specially tailored version for faster transcription. Finally, the transcriptions are presented to the user.

## Important Notes

- The audio files are split based on silence intervals using the `split_on_silence` method of pydub. By default, this occurs with 100 millisecond pauses.
- The OpenAI Whisper model is used for the transcription process. This model is trained specifically to provide fast and accurate results.

## Sample Video

[![Project Video]()](./tutorials/transcript.mp4)


