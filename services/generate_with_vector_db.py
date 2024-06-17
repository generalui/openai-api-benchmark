import os
import openai
import backoff 

openai.api_key = os.getenv("OPENAI_API_KEY")

@backoff.on_predicate(backoff.expo, lambda x: x == "failed", max_time=160)
def create_and_run_poll_with_backoff(**kwargs):
  return openai.beta.threads.create_and_run_poll(**kwargs)

async def generate_with_vector_db(prompt: str, context = "") -> str:
  run = create_and_run_poll_with_backoff(
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
    return run.status
