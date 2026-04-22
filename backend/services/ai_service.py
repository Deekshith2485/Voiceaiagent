from openai import OpenAI
from backend.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def get_ai_response(message, history=[]):
    messages = []

    for item in history:
        if "user:" in item:
            messages.append({"role": "user", "content": item.replace("user: ", "")})
        elif "ai:" in item:
            messages.append({"role": "assistant", "content": item.replace("ai: ", "")})

    messages.append({"role": "user", "content": message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )

    return response.choices[0].message.content