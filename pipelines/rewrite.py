from prompts_templates import REWRITING_PROMPT
from chatgpt import run_prompt

# Original clinical case (German or free text)
original_case = """64-jähriger Patient mit ösophagealem Adenokarzinom, cT3 cN1 M0. 
Neoadjuvante Chemoradiotherapie vor 6 Wochen abgeschlossen. 
Restaging zeigt partielle Tumorantwort."""

# Format the rewriting prompt
formatted_prompt = REWRITING_PROMPT.format(original_case=original_case)

# Run prompt via chatgpt.py
rewritten_case = run_prompt(formatted_prompt)

print("=== Rewritten Case ===")
print(rewritten_case)
