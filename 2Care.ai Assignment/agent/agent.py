import openai
import json
from agent.prompt import SYSTEM_PROMPT
from agent.tools import handle_tool

openai.api_key = "YOUR_OPENAI_KEY"

def process_request(user_text, language):

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ]
    )

    message = response["choices"][0]["message"]["content"]

    try:
        data = json.loads(message)

    except:
        return "Sorry, I couldn't understand your request."

    return handle_tool(data)