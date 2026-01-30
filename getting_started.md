## Getting Started

These instructions will help you run the pipelines on **dummy patient cases** and optionally switch to **real guideline corpora** if already digested.

### 1. Install Dependencies

Make sure you are using the provided virtual environment or install dependencies with:

```bash
pip install -r requirements.txt
```

### 2. Dummy Patient Cases & Guidelines

- Dummy patient cases: data/dummy_patients/
- Dummy guideline corpora: data/dummy_corpora/

All pipelines can be run directly on these files for demonstration purposes.

### 3. Pipelines Overview
| Pipeline                           | Description                                                                 | Example Command                                     |
| ---------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------- |
| `framework_1_simple_request.py`    | Single-request prompt on a patient case (original or rewritten)             | `python pipelines/framework_1_simple_request.py`    |
| `framework_2_chatgpt_assistant.py` | Assistant-style prompt using a pre-configured ChatGPT Assistant             | `python pipelines/framework_2_chatgpt_assistant.py` |
| `framework_3_RAG.py`               | Custom RAG pipeline with local similarity search and prompt-based inference | `python pipelines/framework_3_RAG.py`               |

### 4. Switching Between Dummy and Real Guidelines (RAG Pipeline)

When running framework_3_RAG.py:
1. By default, the pipeline uses the dummy guideline corpus.
2. You will see a warning:
```rust
WARNING: You are about to use the dummy guideline corpus for demonstration.
```
3. To use real guidelines that have already been digested:

- Enter y when prompted.

- Select the organ/system: esophageal, gastric, hepatic, pancreas, or colorectal.

- The script will automatically load all JSON files containing that keyword in data/dummy_corpora/ and merge them.

- If you abort or enter an invalid choice, the pipeline will fallback to the dummy corpus.

4. Optionally, you can filter by **selected corpora** chunks when prompted.

### 5. Optional: Rewriting Patient Cases

All pipelines support using rewritten patient cases:

- When prompted: `Use rewritten case? (y/n)`

- If yes, the `rewrite.py` function reformats the case in a standardized, guideline-style format before processing.

- Make sure `rewrite.py` is available in the `pipelines/` folder.

### 6. Output

- The RAG pipeline prints:

  - Patient case (original or rewritten)

  - Retrieved guideline chunks with similarity scores

  - Generated RAG output

- Other pipelines print the prompt output directly in the console.
