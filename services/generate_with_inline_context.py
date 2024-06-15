import os
import openai
from typing import List, Dict

# Configure the OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

async def reply_to_message_with_inline_context(messages: List[Dict[str, str]], context: str = "") -> str:
    instructions = {
        "role": "system",
        "content": f"""
          You are a Slack bot called GenAI that belongs to the company GenUI.
          You can answer normal questions an all purpose LLM can answer, but you are also the expert at company specific information.

          Your task is to reply to the incoming message of this Slack thread between you and an employee:

          If the history is relevant to the incoming message, consider it to generate the reply. Otherwise, ignore it.
          For general questions and conversation, reply normally.
          For company related questions, use the extra context provided directly.

          Extra context: {context}
          """
    }

    chat_completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[instructions, *messages],
        temperature=1
    )

    return chat_completion['choices'][0]['message']['content'] if chat_completion['choices'] else ""

# Example usage (uncomment and run within an async context):
# messages = [{"role": "user", "content": "Hello, GenAI!"}]
# context = "Company-specific info here."
# response = await reply_to_message_with_inline_context(messages, context)
# print(response)