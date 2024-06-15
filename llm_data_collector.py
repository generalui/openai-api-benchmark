import asyncio

import jsonlines
from dotenv import load_dotenv

from utils import process_pdfs
from services import generate_with_inline_context

load_dotenv()

async def main():
    context = await process_pdfs()

    with jsonlines.open('./prompts/prompts.jsonl') as reader:
        for obj in reader:
            question = obj['question']
            answer, prompt_tokens = await generate_with_inline_context(question, context)
            print(f"answer: {answer}")
            break

if __name__ == "__main__":
    asyncio.run(main())