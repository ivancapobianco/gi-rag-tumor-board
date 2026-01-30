# gi-rag-tumor-board

Retrieval-Augmented Generation framework for gastrointestinal oncology tumor board decision support

This repository accompanies the manuscript:
"Toward AI Tumor Boards: Retrieval-Augmented Generation Improves Concordance in Gastrointestinal Oncology".

## Purpose

This repository provides full transparency of the methodological framework, prompting strategies, and retrieval pipelines used in the study.

Note: Due to patient privacy regulations and copyright restrictions, no real patient data or guideline documents are included.


## Repository Structure & Contents

| Folder / File           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `config`                | Contains hyperparameter files (`hyperparameters.yaml`) for experimental setups.                                                                                                                                                                                                                                                                                                                                                             |
| `data`                  | Contains **dummy patient cases** (`dummy_patients/`) and **synthetic guideline corpora** (`dummy_corpora/`), plus the guideline dictionary (`guideline_dictionary_dummy.py`).                                                                                                                                                                                                                                                                                   |
| `experiments`           | Includes configuration matrices and scripts for reproducing the 16 experimental setups (`configuration_matrix.yaml`).                                                                                                                                                                                                                                                                                                                       |
| `guidelines processing` | Contains scripts for processing guidelines, chunking PDFs, and generating JSON corpora.                                                                                                                                                                                                                                                                                                                                                     |
| `pipelines`             | All pipeline scripts: <br>- `framework_1_simple_request.py` – runs a single request prompt on a patient case <br>- `framework_2_chatgpt_assistant.py` – runs an assistant-style prompt using a pre-configured ChatGPT assistant <br>- `framework_3_RAG.py` – executes the custom RAG pipeline <br>- `rewrite.py` – rewrites patient cases into structured guideline-style format <br>- `embeddings.py` – embeds patient cases for retrieval |
| `prompts`               | Contains all prompt templates and examples for different experimental configurations (`README.md` inside prompts folder explains usage).                                                                                                                                                                                                                                                                                                    |
| `.gitignore`            | Git ignore file.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `LICENSE`               | Repository license.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `README.md`             | This main README.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `requirements.txt`      | All Python dependencies needed to run the pipelines.                                                                                                                                                                                                                                                                                                                                                                                        |

## Reproducibility

The repository enables methodological replication of the study design and prompt engineering strategies. Synthetic data demonstrate end-to-end execution of the pipelines.

- Dummy patient cases: data/dummy_patients/

- Dummy guideline corpora: data/dummy_corpora/

- Experimental configuration: experiments/configuration_matrix.yaml

You can run any of the three pipelines (framework_1, framework_2, framework_3) on the dummy data to reproduce retrieval, embedding, and RAG outputs.


## What Is Included

- Prompt templates and examples for all experimental setups

- Dummy patient cases and synthetic guideline corpora

- Guideline processing logic (PDF chunking → JSON → embeddings)

- Configuration matrix for the 16 experimental setups

- Retrieval and RAG orchestration logic

## What is Not Included

- Real patient-level clinical data

- Copyrighted guideline texts (German S3, NCCN)

- API keys or credentials


## Disclaimer

This code is for research purposes only and is not intended for clinical use.


---

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
