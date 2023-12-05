import asyncio
import os

import streamlit as st
from st_audiorec import st_audiorec
from streamlit_chat import message

from src.audio.audio_synthesizer import AudioSynthesizer
from src.audio.audio_transcriber import AudioTranscriber
from src.llm.create_prompt import generate_prompt
from src.llm.yandex_gpt import process_prompt_yandex


def generate_response(question: str) -> str:
    try:
        print(f"Generating response for question: {question}")
        prompt = generate_prompt(question)
        response = process_prompt_yandex(prompt)
        return response
    except Exception as e:
        print(f"Error while generating prompt: {e}")
        return "Ошибка при генерации ответа"


def generate_audio(text: str) -> bytes:
    text_synthesizer = AudioSynthesizer()
    audio_path = "output.wav"
    try:
        asyncio.run(
            text_synthesizer.synthesize(
                audio_path,
                text,
            )
        )
        file_bytes = open(audio_path, "rb").read()
        return file_bytes
    finally:
        print("Removing audio file")
        os.remove(audio_path)


key: int = 1


def send_message(msg: str, is_user: bool = True):
    global key
    message(msg, is_user=is_user, key=key)
    key = key + 1


def transcribe_audio(wav_audio_data: bytes) -> str:
    file_path = "audio.wav"
    try:
        with open(file_path, "wb") as f:
            f.write(wav_audio_data)

        audio_transcriber = AudioTranscriber()
        transcription = asyncio.run(audio_transcriber.speech_to_text(file_path))
        return transcription
    except Exception as e:
        print(f"Error while processing audio: {e}")
        return "Ошибка при обработке аудио"
    finally:
        print("Removing audio file")
        os.remove(file_path)


st.title("Voice Assistant бот")

if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []

wav_audio_data = st_audiorec()
send_message(
    "Приветствую, я аудио помощник. Задай мне вопрос используя микрофон и я на него отвечу.",
    False,
)
if wav_audio_data is not None:
    send_message("Слушаю аудио...", False)
    transcription = transcribe_audio(wav_audio_data)
    send_message(f"Мой вопрос: {transcription}", True)
    response = generate_response(transcription)
    send_message(response, False)
    audio_response = generate_audio(response)
    st.audio(audio_response)
