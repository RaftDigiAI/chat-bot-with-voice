from speechkit import configure_credentials, creds, model_repository
from speechkit.stt import AudioProcessingType

from src.config.config import YANDEX_SPEECH_API_KEY


class AudioTranscriber:
    def __init__(
        self,
    ):
        configure_credentials(
            yandex_credentials=creds.YandexCredentials(api_key=YANDEX_SPEECH_API_KEY)
        )

    async def speech_to_text(
        self,
        audio_path: str,
    ) -> str:
        model = model_repository.recognition_model()

        model.model = "general"
        model.language = "ru-RU"
        model.audio_processing_type = AudioProcessingType.Full

        results = model.transcribe_file(audio_path)
        normalized_text = ""
        unique_results = set([result.normalized_text for result in results])
        for result in unique_results:
            normalized_text += result
            normalized_text += "\n"

        return normalized_text
