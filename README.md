# chat-bot-with-voice

Chat bot uses Yandex SpeechKit to recognize speech to text and text to speech and Yandex GPT 2 to generate answers.

Chat bot is dedicated to answer question about advertisement.

1. Create virtual environment
2. Activate virtual environment
3. Copy .env.template to .env and fill in the values YANDEX_SPEECH_API_KEY and YANDEX_GPT_API_KEY. Check yandex cloud documentation to get the keys.
4. Install requirements `pip install -r requirements.txt`
5. Run `streamlit run chat.py` to start the app in the browser