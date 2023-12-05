from speechkit import configure_credentials, creds, model_repository

from src.config.config import YANDEX_SPEECH_API_KEY


class AudioSynthesizer:
    def __init__(
        self,
    ):
        configure_credentials(
            yandex_credentials=creds.YandexCredentials(api_key=YANDEX_SPEECH_API_KEY)
        )

    async def synthesize(self, output_file_path, text):
        model = model_repository.synthesis_model()

        model.voice = "alena"
        model.role = "good"

        result = model.synthesize(text, raw_format=False)
        result.export(output_file_path, "wav")
