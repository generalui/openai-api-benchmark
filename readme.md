# OpenAI API Benchmark

This repository contains the code and data used to evaluate the effectiveness of larger context windows in modern Large Language Models (LLMs) compared to Retrieval-Augmented Generation (RAG). Specifically, it compares two methods for grounding LLM responses: using inline context and utilizing vector databases for retrieval. The results discussed in the article “Do Larger Context Windows Remove the Need for RAG?” are computed using this codebase.

# Directory and File Descriptions

- benchmark_data/: Contains the JSONL files with the inline context answers, vector DB answers, target answers, and questions used for benchmarking.
  - answers_inline_context.jsonl: Generated answers using inline context.
  - answers_target.jsonl: Reference answers.
  - answers_vector_db.jsonl: Generated answers using vector DB.
  - questions.jsonl: Set of questions used for evaluation.
- files/: Contains PDF documents that provide context for the benchmarking questions.
- .env.example: Example environment variable configuration file.
- benchmark.ipynb: Jupyter notebook used for running the benchmark and visualizing results.
- llm_data_collector.py: Script for collecting data from LLMs.

# Getting Started

## Prerequisites

Ensure you have Python 3.8+ installed. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Setting Up Environment Variables

Copy the .env.example to .env and fill in you OpenAI API keys

```bash
cp .env.example .env
```

# Running the Benchmark

1. Generate Answers:
   `python llm_data_collector.py`

2. Run the Jupyter Notebook: Open and run benchmark.ipynb to compute the BLEU and ROUGE scores, and perform cost analysis.

# Contributing

If you wish to contribute to this project, please fork the repository and create a pull request with your changes. Ensure that your code follows the project’s style guidelines and includes appropriate tests.

# License

This project is licensed under the MIT License. See the LICENSE file for details.

# References

For more details, refer to the article “Do Larger Context Windows Remove the Need for RAG?.”

Feel free to reach out if you have any questions or need further assistance.
