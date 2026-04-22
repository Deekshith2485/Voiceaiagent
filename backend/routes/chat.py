from fastapi import APIRouter
from backend.services.ai_service import get_ai_response

router = APIRouter()

@router.post("/chat")
async def chat(input_text: str):
    response = get_ai_response(input_text)
    return {"response": response}