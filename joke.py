import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "",
        },
        {
            "role": "user",
            "content": """Explain this joke: I was going to fly to vist my family on May 3rd. My mom said "Oh gread, your dad's poetry reading is that night!" So I'm flying in on May 4th.""",
        }
    ],
    temperature=1,
    top_p=1,
    model=model
)

print(response.choices[0].message.content)

