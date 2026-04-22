from fastapi import FastAPI, WebSocket
from backend.routes.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)

@app.get("/")
def health():
    return {"status": "running"}


# ⚡ WEBSOCKET (REAL-TIME)
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"AI: {data}")