from src.llm.create_prompt import generate_prompt
from src.llm.yandex_gpt import process_prompt_yandex

question = "Привет, расскажи про рекламу в метро"
prompt = generate_prompt(question)

response = process_prompt_yandex(prompt)

print(response)
