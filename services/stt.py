import io
from google.cloud import speech_v1p1beta1 as speech

def transcribe_file(path: str, language_code: str = "en-US") -> str:
    try:
        client = speech.SpeechClient()
        with io.open(path, "rb") as audio_file:
            content = audio_file.read()
        audio = speech.RecognitionAudio(content=content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            language_code=language_code,
            enable_automatic_punctuation=True
        )
        response = client.recognize(config=config, audio=audio)
        return " ".join([r.alternatives[0].transcript for r in response.results])
    except Exception as e:
        return f"[Error: {e}]"
