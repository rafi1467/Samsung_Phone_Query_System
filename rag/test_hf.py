from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)

response = client.chat_completion(
    model="Qwen/Qwen3-8B",
    messages=[
        {
            "role": "user",
            "content": "Tell me about Samsung Galaxy S24 Ultra"
        }
    ],
    max_tokens=200
)

print(response.choices[0].message.content)