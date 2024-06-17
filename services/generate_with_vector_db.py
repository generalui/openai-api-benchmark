import os
import openai
import pprint

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_with_vector_db(prompt: str, context = "") -> str:
  run = openai.beta.threads.create_and_run_poll(
    assistant_id=os.getenv("OPENAI_ASSISTANT_ID"),
    instructions="Answer the following question accurately and concisely based on the provided context.",
    thread={
      "messages": [
        {
          "role": "user",
          "content": f"""
            Question: {prompt}
          """
        }
      ]
    }
  )
  if run.status == "completed":
    messages = openai.beta.threads.messages.list(
      thread_id=run.thread_id,
    )
    return messages.data[0].content[0].text.value, run.usage
  else:
    print(run.status)
