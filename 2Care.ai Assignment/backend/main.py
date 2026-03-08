from fastapi import FastAPI
from backend.websocket import router as websocket_router

app = FastAPI(title="Voice AI Clinical Agent")

app.include_router(websocket_router)

@app.get("/")
def health_check():
    return {"status": "Voice AI Agent Running"}