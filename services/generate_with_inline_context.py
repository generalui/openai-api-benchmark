import os
import openai

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

    usage = chat_completion.usage
    answer = chat_completion.choices[0].message.content

    return answer, usage
