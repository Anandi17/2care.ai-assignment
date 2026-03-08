from fastapi import APIRouter, WebSocket
from services.speech_to_text import transcribe_audio
from services.text_to_speech import speak
from services.language_detection import detect_language
from agent.agent import process_request
from backend.latency import measure_latency

router = APIRouter()

@router.websocket("/voice")
async def voice_agent(websocket: WebSocket):

    await websocket.accept()

    while True:

        audio_bytes = await websocket.receive_bytes()

        with measure_latency("voice_pipeline"):

            text = transcribe_audio(audio_bytes)

            language = detect_language(text)

            response = process_request(text, language)

            audio = speak(response, language)

        await websocket.send_bytes(audio)