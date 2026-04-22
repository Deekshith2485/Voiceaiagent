import whisper
from gtts import gTTS

model = whisper.load_model("base")

def speech_to_text(file_path):
    result = model.transcribe(file_path)
    return result["text"]

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename