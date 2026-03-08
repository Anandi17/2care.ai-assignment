from gtts import gTTS
import io

def speak(text, language="English"):

    lang_code = "en"

    if language == "Hindi":
        lang_code = "hi"

    if language == "Tamil":
        lang_code = "ta"

    tts = gTTS(text=text, lang=lang_code)

    audio_buffer = io.BytesIO()

    tts.write_to_fp(audio_buffer)

    return audio_buffer.getvalue()