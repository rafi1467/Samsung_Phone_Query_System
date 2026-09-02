from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HF_TOKEN")
)


def ask_llm(prompt):

    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3-0324",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=300
    )

    return response.choices[0].message.content