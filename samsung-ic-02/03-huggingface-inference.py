from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=""
)

response = client.chat.completions.create(
    model="Qwen/Qwen2.5-72B-Instruct:fastest",
    messages=[
        {"role": "system", "content": "You are a rude unreasonable professor who is very opinionated and does not like to answer questions"},
        {"role": "user", "content": "Tell me about Voyager 1"}
    ],
    temperature=0.7,
    max_tokens=500
)

print(response.choices[0].message.content)