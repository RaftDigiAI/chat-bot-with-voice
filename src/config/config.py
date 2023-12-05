import os

from dotenv import load_dotenv

load_dotenv()


YANDEX_SPEECH_API_KEY = os.getenv("YANDEX_SPEECH_API_KEY", "")
YANDEX_GPT_API_KEY = os.getenv("YANDEX_GPT_API_KEY", "")
