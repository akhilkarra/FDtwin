import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

print(response.choices[0].message)