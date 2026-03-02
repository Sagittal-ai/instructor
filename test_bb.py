OPENAI_API_KEY = "sk-proj-1234567890"

import openai

openai.api_key = OPENAI_API_KEY

response = openai.Completion.create(
    model="gpt-4o-mini",
    prompt="Hello, how are you?",
    max_tokens=100
)

print(response.choices[0].text)