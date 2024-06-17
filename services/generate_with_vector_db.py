import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

async def generate_with_vector_db(prompt: str) -> str:
    run = openai.beta.threads.create_and_run_poll(
        assistant_id=os.getenv("OPENAI_ASSISTANT_ID"),
        instructions="Answer the following question accurately and concisely based on the provided context.",
        thread=[
            {
                "role": "user",
                "content": f"""
                  Question: {prompt}
                  """
            },
        ]
    )
    if run.status == "completed":
        messages = openai.beta.threads.messages.list(
            thread_id=run.thread_id,
        )
        print(messages)
    else:
        print(run.status)
