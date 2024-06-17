import asyncio

import jsonlines
from dotenv import load_dotenv

from utils import process_pdfs
from services import generate_with_inline_context, generate_with_vector_db

load_dotenv()

experiments = [
    {
        "name": "inline_context",
        "generate_fn": generate_with_inline_context
    },
    {
        "name": "vector_db",
        "generate_fn": generate_with_vector_db
    
    }
]

async def collect_answers(experiment, question, context):
    generate_fn = experiment["generate_fn"]
    answer, usage = await generate_fn(question, context)
    with jsonlines.open(f'./benchmark_data/answers_{experiment["name"]}.jsonl', mode='a') as writer:
        writer.write({
            "answer": answer,
            "completion_tokens": usage.completion_tokens,
            "prompt_tokens": usage.prompt_tokens,
            "total_tokens": usage.total_tokens,
        })

async def main():
    context = await process_pdfs()

    with jsonlines.open('./benchmark_data/questions.jsonl') as reader:
        for obj in reader:
            question = obj['question']
            
            for experiment in experiments:
                await collect_answers(experiment, question, context)

if __name__ == "__main__":
    asyncio.run(main())