import jsonlines
from dotenv import load_dotenv

load_dotenv()

with jsonlines.open('./prompts/prompts.jsonl') as reader:
    for obj in reader:
        print(obj)