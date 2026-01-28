"""
Clinical case rewriting for pipeline.

This script uses the REWRITING_PROMPT template from prompts/prompts_templates.py
to standardize a patient case in a guideline-style format.

It calls chatgpt.py (also in prompts folder) for the model execution.
"""

import sys
import os

# -----------------------------
# Add the 'prompts' folder to sys.path
# -----------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
prompts_dir = os.path.abspath(os.path.join(current_dir, '..', 'prompts'))
sys.path.append(prompts_dir)

# -----------------------------
# Import the prompt template and chat function
# -----------------------------
from prompts_templates import REWRITING_PROMPT
from chatgpt import chatgpt_chat_completion


# -----------------------------
# Configuration
# -----------------------------
MODEL_NAME = "gpt-4o-mini"  # or another model of your choice

# -----------------------------
# Load original patient case from TXT file
# -----------------------------
case_txt_path = os.path.abspath(os.path.join(current_dir, '..', 'data', 'dummy_patients', 'example_case_de.txt'))

with open(case_txt_path, 'r', encoding='utf-8') as f:
    original_case = f.read().strip()

# -----------------------------
# Format the rewriting prompt
# -----------------------------
formatted_prompt = REWRITING_PROMPT.format(original_case=original_case)

# -----------------------------
# Call OpenAI chat completion
# -----------------------------
rewritten_case = chatgpt_chat_completion(formatted_prompt, model=MODEL_NAME)

# -----------------------------
# Output
# -----------------------------
print("=== Original Case ===")
print(original_case)
print("\n=== Rewritten Case ===")
print(rewritten_case)
