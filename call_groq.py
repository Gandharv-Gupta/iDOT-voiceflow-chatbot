from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

groq_api_key=os.getenv("GROQ_API_KEY")



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
    response_length = 'Reply under 30 words'  # You can add instructions if needed
    response = client.responses.create(
        input=user_text + response_length,
        model="openai/gpt-oss-20b",
    )
    return response.output_text
