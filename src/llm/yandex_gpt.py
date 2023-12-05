import asyncio
import json

import aiohttp

from src.config.config import YANDEX_GPT_API_KEY


async def chat_with_yandex_async(model, temperature, max_tokens, role, text):
    url = "https://llm.api.cloud.yandex.net/llm/v1alpha/chat"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Api-Key " + YANDEX_GPT_API_KEY,
    }

    data = {
        "model": model,
        "generationOptions": {
            "partialResults": False,
            "temperature": temperature,
            "maxTokens": max_tokens,
        },
        "messages": [{"role": role, "text": text}],
    }

    async with aiohttp.ClientSession() as session:
        print("Sending request to Yandex LLM")
        async with session.post(
            url, headers=headers, data=json.dumps(data)
        ) as response:
            print("Received response from Yandex LLM", response)
            if response.status == 200:
                raw_response = await response.text()
                response_data = json.loads(raw_response)
                return response_data["result"]["message"]["text"]
            else:
                return None


def process_prompt_yandex(prompt: str) -> str:
    response = asyncio.run(
        chat_with_yandex_async(
            model="general", temperature=0.5, max_tokens=500, role="user", text=prompt
        )
    )
    return response
