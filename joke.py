# Import necessary libraries
import os
from openai import OpenAI

# Retrieve the GitHub token from environment variables
# Ensure the "GITHUB_TOKEN" is set in your environment
token = os.environ["GITHUB_TOKEN"]

# Define the endpoint URL for the OpenAI API
endpoint = "https://models.github.ai/inference"

# Specify the model to be used
model = "openai/gpt-4.1"

# Initialize the OpenAI client with the API endpoint and token
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# Create a chat completion request with the specified inputs
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",  # System role to provide context or instructions (empty here)
            "content": "",
        },
        {
            "role": "user",  # User role specifies the input message
            "content": """Explain this joke: I was going to fly to visit my family on May 3rd. My mom said "Oh great, your dad's poetry reading is that night!" So I'm flying in on May 4th.""",
        }
    ],
    temperature=1,  # Controls randomness in the output (higher value = more random)
    top_p=1,  # Controls diversity via nucleus sampling (1 means no truncation)
    model=model  # Specify the model to be used for the request
)

# Print the content of the first choice in the response
print(response.choices[0].message.content)
