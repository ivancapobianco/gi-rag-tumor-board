# Dummy Guidelines PDF Extraction and JSON Generation

This repository contains scripts and dummy dictionaries to extract content from PDF guidelines (S3 and NCCN) and convert them into structured JSON format. The workflow is designed to support downstream processing, corpora selection, and manual curation.

## Step 1: Prepare the Dummy Dictionary

1. Open `data/dummy_corpora/guideline_dictionary_dummy.py`.
2. Replace the `"PATH OF YOUR PDF"` placeholders with the correct **relative paths** to your PDF files in the `data/dummy_corpora/guidelines` folder.
3. Make sure each guideline has the correct `starting_page`, `final_cleaned_chunk` (for S3), `mark` (heading marker, for S3), and `images_to_save` (pages with images to skip).

**Example:**

```python
guidelines_dict = {
    'OE-CA': {
        'path': "../data/dummy_corpora/guidelines/LL_Ösophaguskarzinom_Kurzversion_3.1.pdf",
        'starting_page': 21,
        'final_cleaned_chunk': "### 15 Tabellenverzeichnis",
        'mark': "### ",
        'images_to_save': [22, 29, 48],
    }
}
```


## Step 2: Place PDFs

PDFs → data/dummy_corpora/guidelines

Ensure the paths in the dummy dictionary point to these files correctly.

## Step 3: Extract JSON from PDFs

### S3 Guidelines

Given the structure of the German S3 Guidelines, we decided to create one chunk per chapters (determined by the specified mark).

Use python processing/extract_s3_guidelines_to_json.py
- Extracts text starting from starting_page and splits chunks using the specified mark.
- Uses final_cleaned_chunk to remove trailing sections (e.g., tables).
- Output JSON files are saved in data/dummy_corpora/ with filenames like:

```text
    dummy_S3_guidelines_esophageal.json
    dummy_S3_guidelines_gastric.json
```

### NCCN Guidelines

Given the structure of the German S3 Guidelines, we decided to create one chunk per slide.

Use python processing/extract_nccn_guidelines_to_json.py
- Creates one chunk per page between starting_page and final_page, skipping images_to_save pages.
- Output JSON files are saved in data/dummy_corpora/ with filenames like:

```text
    dummy_NCCN_guidelines_esophageal.json
    dummy_NCCN_guidelines_gastric.json
```

PS: PS: Honestly, this step could be replaced by a simple copy-paste of the PDFs. Not elegant, but it would achieve the same goal.


## Step 4: Manual Curation

After generating the JSON files, manual curation is required:

- Images and Tables:
    
        Images should be rewritten in plain text. We usually enclose them in the tag <chart>image description</chart>.
    
        For the paper we convert every markdown table to a written JSON format. If this is absolutely necessary, it is to be questioned.
    
- Selected Corpora:
    
        Open the JSON files and set "selected_corpora": 1 for chunks that should be included in the curated corpus.
    
        The default value is 0.
    
- Quality Check:
    
        Ensure text chunks are readable and headings are preserved where relevant.
    
        Remove any irrelevant footer or page numbering text if present.

## Notes

chunk_id is automatically assigned:

```text
        S3 guidelines → start at 101
        NCCN guidelines → start at 501
```

Ensure all paths in the dictionary are relative to the repository root.

The mark variable is essential for S3 guidelines; NCCN guidelines usually work per-page without headings.

The scripts rely on pymupdf4llm to read PDFs and convert them into markdown-like text.





# Workflow Summary

1. Update the dummy dictionary with correct PDF paths and page info.
2. Place PDFs in the corresponding folders.
3. Run S3 and/or NCCN extraction scripts.
4. Manually curate JSON outputs: update selected_corpora, rewrite images/tables, remove noise.
5. Use curated JSON for downstream applications (e.g., corpora creation, NLP processing, etc.).


