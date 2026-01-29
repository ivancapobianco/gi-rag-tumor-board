# Dummy Guidelines PDF Extraction and JSON Generation

This repository contains scripts and dummy dictionaries to extract content from PDF guidelines (S3 and NCCN) and convert them into structured JSON format. The workflow is designed to support downstream processing, corpora selection, and manual curation.

---

## Folder Structure

gi-rag-tumor-board/
├── data/
│ └── dummy_corpora/
│ └── guideline_dictionary_dummy.py # Minimal dummy dictionary
├── processing/
│ ├── extract_s3_guidelines_to_json.py # S3 PDF extraction
│ └── extract_nccn_guidelines_to_json.py # NCCN PDF extraction
├── Documents/
│ ├── Guidelines_pdf/ # Place your S3 PDFs here
│ └── Guidelines_NCCN_pdf/ # Place your NCCN PDFs here


---

## Step 1: Prepare the Dummy Dictionary

1. Open `data/dummy_corpora/guideline_dictionary_dummy.py`.
2. Replace the `"PATH OF YOUR PDF"` placeholders with the correct **relative paths** to your PDF files in the `Documents/Guidelines_pdf/` or `Documents/Guidelines_NCCN_pdf/` folders.
3. Make sure each guideline has the correct `starting_page`, `final_cleaned_chunk` (for S3), `mark` (heading marker), and `images_to_save` (pages with images to skip).

**Example:**

```python
guidelines_dict = {
    'OE-CA': {
        'path': "../Documents/Guidelines_pdf/LL_Ösophaguskarzinom_Kurzversion_3.1.pdf",
        'starting_page': 21,
        'final_cleaned_chunk': "### 15 Tabellenverzeichnis",
        'mark': "### ",
        'images_to_save': [22, 29, 48],
    }
}

Step 2: Place PDFs

    S3 PDFs → Documents/Guidelines_pdf/

    NCCN PDFs → Documents/Guidelines_NCCN_pdf/

    Ensure the paths in the dummy dictionary point to these files correctly.

Step 3: Extract JSON from PDFs
S3 Guidelines

python processing/extract_s3_guidelines_to_json.py

    Extracts text starting from starting_page and splits chunks using the specified mark.

    Uses final_cleaned_chunk to remove trailing sections (e.g., tables).

    Output JSON files are saved in data/dummy_corpora/ with filenames like:

dummy_guidelines_OE_CA.json
dummy_guidelines_Magen_CA.json

NCCN Guidelines

python processing/extract_nccn_guidelines_to_json.py

    Creates one chunk per page between starting_page and final_page, skipping images_to_save pages.

    Output JSON files are saved in data/dummy_corpora/ with filenames like:

dummy_guidelines_OE_CA.json
dummy_guidelines_Magen_CA.json

Step 4: Manual Curation

After generating the JSON files, manual curation is required:

    Images and Tables:

        Extracted image/text combinations should be checked and rewritten if necessary.

        Ensure tables from figures are correctly represented in JSON.

    Selected Corpora:

        Open the JSON files and set "selected_corpora": 1 for chunks that should be included in the curated corpus.

        Default value is 0.

    Quality Check:

        Ensure text chunks are readable and headings are preserved where relevant.

        Remove any irrelevant footer or page numbering text if present.

Notes

    chunk_id is automatically assigned:

        S3 guidelines → start at 101

        NCCN guidelines → start at 201

    Ensure all paths in the dictionary are relative to the repository root.

    The mark variable is essential for S3 guidelines; NCCN guidelines usually work per-page without headings.

    The scripts rely on pymupdf4llm to read PDFs and convert them into markdown-like text.

Requirements

    Python 3.9+

    Packages: pymupdf4llm, pandas (optional for S3 chunk processing), json

    Install dependencies via pip:

pip install pandas pymupdf4llm

Workflow Summary

    Update the dummy dictionary with correct PDF paths and page info.

    Place PDFs in the corresponding folders.

    Run S3 and/or NCCN extraction scripts.

    Manually curate JSON outputs: update selected_corpora, rewrite images/tables, remove noise.

    Use curated JSON for downstream applications (e.g., corpora creation, NLP processing, etc.).


---

I can also make a **shorter, “quick start” version** if you want something even more compact for team members.  

Do you want me to do that next?
::contentReference[oaicite:0]{index=0}
