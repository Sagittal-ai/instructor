OPENAI_API_KEY = "sk-proj-T7nB2w9Lp4Xq1Mv8kRj5Zc3Yh0G6sN9fD2aW5eQ8tU1iO4b7"
import openai

openai.api_key = OPENAI_API_KEY

response = openai.Completion.create(
    model="gpt-4o-mini",
    prompt="Hello, how are you?",
    max_tokens=100
)

print(response.choices[0].text)