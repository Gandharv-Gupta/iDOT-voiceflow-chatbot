from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1",
)

def call_groq(user_text, chat_history=None):
    system_prompt = f"You are iDOT (pronounced eye-dot), a smart and friendly assistant. Keep replies casual, clear, engaging, and precise. This is the chat history: {chat_history}Stay under 30 words."
    if chat_history:
        system_prompt = system_prompt.format(chat_history)  
    response = client.responses.create(
        input=user_text + system_prompt,
        model="openai/gpt-oss-20b",
    )
    return response.output_text
