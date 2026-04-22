from fastapi import APIRouter, UploadFile, File
from fastapi.responses import FileResponse

from backend.models.chat_model import ChatRequest
from backend.services.ai_service import get_ai_response
from backend.services.memory_service import save_memory, get_memory
from backend.services.speech_service import speech_to_text, text_to_speech
from backend.services.language_service import detect_language
from backend.services.appointment_service import create_appointment

router = APIRouter()

# 🔥 CHAT (AI + MEMORY + LANGUAGE)
@router.post("/chat")
async def chat(request: ChatRequest):
    user_id = request.user_id
    message = request.message

    save_memory(user_id, f"user: {message}")
    history = get_memory(user_id)

    lang = detect_language(message)

    response = get_ai_response(message, history)

    save_memory(user_id, f"ai: {response}")

    return {
        "response": response,
        "language": lang,
        "history": history
    }


# 🎤 VOICE INPUT
@router.post("/voice")
async def voice_chat(file: UploadFile = File(...)):
    path = f"temp_{file.filename}"

    with open(path, "wb") as f:
        f.write(await file.read())

    text = speech_to_text(path)

    return {"text": text}


# 🔊 TEXT TO SPEECH
@router.post("/speak")
async def speak(text: str):
    file = text_to_speech(text)
    return FileResponse(file, media_type="audio/mpeg")


# 📅 APPOINTMENT
@router.post("/appointment")
async def book(user: str, date: str, time: str):
    return create_appointment(user, date, time)