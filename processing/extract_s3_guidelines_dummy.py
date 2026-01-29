import pandas as pd
import re
import os
from guidelines_dictionaries_dummy import guidelines_dict
import pymupdf4llm

# Folder to save output
output_folder = "Guidelines_xlsx"
os.makedirs(output_folder, exist_ok=True)

def chunk_by_heading(text, heading_marker="### "):
    lines = text.splitlines()
    chunks = []
    current_chunk = []
    for line in lines:
        if line.startswith(heading_marker):
            if current_chunk:
                chunks.append("\n".join(current_chunk))
            current_chunk = [line]
        else:
            current_chunk.append(line)
    if current_chunk:
        chunks.append("\n".join(current_chunk))
    return chunks

def split_last_chunk(chunks, heading):
    if not chunks:
        return chunks
    last_chunk = chunks[-1]
    split_chunks = last_chunk.split(heading)
    new_chunks = chunks[:-1] + [c.strip() for c in split_chunks if c.strip()]
    return new_chunks[:-1]

# Loop through dummy guidelines
for guideline, info in guidelines_dict.items():
    pdf_path = info['path']
    print(f"Processing S3 guideline: {guideline}")

    # Load PDF as markdown docs
    llama_reader = pymupdf4llm.LlamaMarkdownReader()
    docs = llama_reader.load_data(pdf_path)

    # Collect chunks
    all_text = [doc.text for doc in docs]
    joined_text = "\n".join(all_text[info['starting_page']:])
    chunks = chunk_by_heading(joined_text, info['mark'])
    final_chunks = split_last_chunk(chunks, info['final_cleaned_chunk'])

    # Save to Excel
    df = pd.DataFrame({'chunk': final_chunks})
    output_path = os.path.join(output_folder, f"{guideline}_chunks.xlsx")
    df.to_excel(output_path, index=False)
    print(f"Saved {len(final_chunks)} chunks to {output_path}\n")

