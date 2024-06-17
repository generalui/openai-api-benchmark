import asyncio

import jsonlines
from dotenv import load_dotenv

from utils import process_pdfs
from services import generate_with_inline_context

load_dotenv()

async def main():
    context = await process_pdfs()

    with jsonlines.open('./benchmark_data/prompts.jsonl') as reader:
        for obj in reader:
            question = obj['question']
            answer, usage = await generate_with_inline_context(question, context)
            
            # append to jsonl file with answer and usage
            with jsonlines.open('./benchmark_data/answers.jsonl', mode='a') as writer:
                writer.write({
                    "answer": answer,
                    "completion_tokens": usage.completion_tokens,
                    "prompt_tokens": usage.prompt_tokens,
                    "total_tokens": usage.total_tokens,
                })

if __name__ == "__main__":
    asyncio.run(main())