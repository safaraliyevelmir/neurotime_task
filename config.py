from pydantic_settings import BaseSettings
from faster_whisper import WhisperModel
from typing import Any
import speech_recognition

class Settings(BaseSettings):
    # WISHPER_MODEL: Any = None
    SPEECH_RECOGNIER: Any = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.WISHPER_MODEL = WhisperModel("large", compute_type="int8_float32")
        self.SPEECH_RECOGNIER = speech_recognition.Recognizer()

settings = Settings()
