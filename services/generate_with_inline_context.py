import os
import openai
from typing import List, Dict

# Configure the OpenAI client
openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_with_inline_context(prompt: str, context: str = "") -> str:
    instructions = {
        "role": "system",
        "content": f"""
          Answer the following question accurately and concisely based on the provided context.
          Question: {prompt}

          Context: {context}
          """
    }

    chat_completion = openai.chat.completions.create(
        model="gpt-4o",
        messages=[instructions]
    )

    prompt_tokens = chat_completion.usage.prompt_tokens
    answer = chat_completion.choices[0].message.content

    return answer, prompt_tokens
