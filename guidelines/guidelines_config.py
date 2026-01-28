"""
Configuration dictionaries for German S3 and NCCN guideline processing.

These dictionaries specify:
- PDF file paths (local only - download per README.md)
- Starting/ending pages for content extraction
- Markdown heading markers for chunking
- Image pages that require OCR/transcription
"""

# =============================================================================
# GERMAN S3 GUIDELINES CONFIGURATION
# =============================================================================

guidelines_dict = {
    'OE-CA': {
        'full_name': 'Ösophaguskarzinom (Esophageal Cancer)',
        'path': "guidelines/german_s3/LL_Ösophaguskarzinom_Kurzversion_3.1.pdf",
        'version': '3.1',
        'awmf_registry': '021/023OL',
        'starting_page': 21,
        'final_cleaned_chunk': "### 15 Tabellenverzeichnis",
        'mark': "### ",
        'images_to_save': [22, 29, 48, 49, 58, 60],
    },
    'Magen-CA': {
        'full_name': 'Magenkarzinom (Gastric Cancer)',
        'path': "guidelines/german_s3/LL_Magenkarzinom_Kurzversion_2.0.pdf",
        'version': '2.0',
        'awmf_registry': '032/009OL',
        'starting_page': 28,
        'final_cleaned_chunk': "### 20 Tabellenverzeichnis",
        'mark': "### ",
        'images_to_save': [41],
    },
    'HCC': {
        'full_name': 'Hepatozelluläres Karzinom (Hepatocellular Carcinoma)',
        'path': "guidelines/german_s3/LL_Hepatozelluläres_Karzinom_und_biliäre_Karzinome_Kurzversion_3.0.pdf",
        'version': '3.0',
        'awmf_registry': '032/053OL',
        'starting_page': 7,
        'final_cleaned_chunk': "### 7 Tabellenverzeichnis",
        'mark': "#### ",
        'images_to_save': [21, 27, 28, 31, 38],
    },
    'Pankreas-CA': {
        'full_name': 'Pankreaskarzinom (Pancreatic Cancer)',
        'path': "guidelines/german_s3/LL_Pankreaskarzinom_Kurzversion_2.0.pdf",
        'version': '2.0',
        'awmf_registry': '032/010OL',
        'starting_page': 27,
        'final_cleaned_chunk': "### 12 Tabellenverzeichnis",
        'mark': "### ",
        'images_to_save': [43, 64],
    },
    'CRC': {
        'full_name': 'Kolorektales Karzinom (Colorectal Cancer)',
        'path': "guidelines/german_s3/LL_KRK_Kurzversion_2.1.pdf",
        'version': '2.1',
        'awmf_registry': '021/007OL',
        'starting_page': 20,
        'final_cleaned_chunk': "### 13 Tabellenverzeichnis",
        'mark': "###### ",
        'images_to_save': [37, 38, 70],
    },
}

# =============================================================================
# NCCN GUIDELINES CONFIGURATION
# =============================================================================

guidelines_nccn_dict = {
    'OE-CA': {
        'full_name': 'Esophageal and Esophagogastric Junction Cancers',
        'path': "guidelines/nccn/esophageal.pdf",
        'version': 'Version 2.2024',
        'starting_page': 11,
        'final_page': 142,
        'mark': "### ",
        'images_to_save': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 31, 32],
    },
    'Magen-CA': {
        'full_name': 'Gastric Cancer',
        'path': "guidelines/nccn/gastric.pdf",
        'version': 'Version 1.2024',
        'starting_page': 10,
        'final_page': 116,
        'mark': "### ",
        'images_to_save': [9, 11, 13, 14, 15, 16, 17, 18, 19, 20, 22],
    },
    'HCC': {
        'full_name': 'Hepatocellular Carcinoma',
        'path': "guidelines/nccn/hcc.pdf",
        'version': 'Version 1.2024',
        'starting_page': 8,
        'final_page': 75,
        'mark': "#### ",
        'images_to_save': [7, 8, 9, 10, 11, 12],
    },
    'Bile Ducts': {
        'full_name': 'Biliary Tract Cancers',
        'path': "guidelines/nccn/btc.pdf",
        'version': 'Version 2.2024',
        'starting_page': 8,
        'final_page': 79,
        'mark': "#### ",
        'images_to_save': [7, 8, 9, 10, 11, 12, 16, 17, 23, 24],
    },
    'Pankreas-CA': {
        'full_name': 'Pancreatic Adenocarcinoma',
        'path': "guidelines/nccn/pancreatic.pdf",
        'version': 'Version 2.2024',
        'starting_page': 10,
        'final_page': 116,
        'mark': "### ",
        'images_to_save': [9, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22],
    },
    'Colon-Ca': {
        'full_name': 'Colon Cancer',
        'path': "guidelines/nccn/colon.pdf",
        'version': 'Version 1.2024',
        'starting_page': 9,
        'final_page': 155,
        'mark': "###### ",
        'images_to_save': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 41, 42, 43],
    },
    'Rectal-CA': {
        'full_name': 'Rectal Cancer',
        'path': "guidelines/nccn/rectal.pdf",
        'version': 'Version 3.2023',
        'starting_page': 11,
        'final_page': 129,
        'mark': "## ",
        'images_to_save': [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 26, 27, 28, 56, 58],
    },
}

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def get_guideline_info(guideline_key: str, source: str = 's3'):
    """
    Get configuration for a specific guideline.
    
    Args:
        guideline_key: Key from guidelines_dict or guidelines_nccn_dict
        source: 's3' or 'nccn'
        
    Returns:
        Dictionary with guideline configuration
    """
    if source == 's3':
        return guidelines_dict.get(guideline_key)
    elif source == 'nccn':
        return guidelines_nccn_dict.get(guideline_key)
    else:
        raise ValueError(f"Invalid source: {source}. Must be 's3' or 'nccn'")


def list_all_guidelines():
    """Print all available guidelines."""
    print("=== GERMAN S3 GUIDELINES ===")
    for key, info in guidelines_dict.items():
        print(f"{key}: {info['full_name']} (v{info['version']})")
    
    print("\n=== NCCN GUIDELINES ===")
    for key, info in guidelines_nccn_dict.items():
        print(f"{key}: {info['full_name']} ({info['version']})")


if __name__ == "__main__":
    list_all_guidelines()
```

5. Click **"Commit new file"**

---

## STEP 2: Create `requirements.txt`

**In GitHub:**
1. Go to root of repository
2. Click **"Add file"** → **"Create new file"**
3. Name it: `requirements.txt`
4. Paste:
```
# Core dependencies
python>=3.11.0

# PDF processing
pymupdf4llm==1.2.3
PyPDF2==3.0.1

# Data manipulation
pandas==2.1.4
numpy==1.26.2
openpyxl==3.1.2

# LlamaIndex and embeddings
llama-index==0.9.48
llama-index-core==0.9.48
llama-index-embeddings-huggingface==0.1.4

# Embeddings model
transformers==4.35.2
sentence-transformers==2.2.2

# OpenAI API (for prompting)
openai==1.3.5

# Statistical analysis
scipy==1.11.4
statsmodels==0.14.0

# Utilities
pyperclip==1.8.2
