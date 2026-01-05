from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)

def call_groq(user_text):
    system_prompt = "You are iDOT, a smart and friendly assistant. Keep replies casual, clear, engaging, and precise. Stay under 30 words."
    response = client.responses.create(
        input=user_text + system_prompt,
        model="openai/gpt-oss-20b",
    )
    return response.output_text
