from openai import OpenAI # type: ignore
def aiprocess(command):
    client = OpenAI(api_key="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")
    completion = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [
        { "role": "system", "content": "You are a helpful assistant." },
        {
            "role": "user","content": command
        }
    ]
)

    return completion.choices[0].message.content
