# Minimal dummy dictionary for S3 and NCCN guidelines
# !!! Please use only the keys esophageal, gastric, hepatic, pancreas, or colorectal for the pipelines to function correctly. !!!

guidelines_s3_dict = {
    'esophageal': {
        'path': "guidelines/NAME OF YOUR PDF.pdf", # Make sure the PDF is located in the guidelines folder, and specify its path in the dictionary in the format guidelines/file_name.pdf.
        'starting_page': 21,
        'final_cleaned_chunk': "### 15 Tabellenverzeichnis",
        'mark': "### ",
        'images_to_save': [22, 29, 48],
    },
    'gastric': {
        'path': "guidelines/NAME OF YOUR PDF.pdfF", # Make sure the PDF is located in the guidelines folder, and specify its path in the dictionary in the format guidelines/file_name.pdf.
        'starting_page': 28,
        'final_cleaned_chunk': "### 20 Tabellenverzeichnis",
        'mark': "### ",
        'images_to_save': [41],
    },
    'pancreatic' : {},
    'hepatic' : {},
    'colorectal' : {},
}

guidelines_nccn_dict = {
    'esophageal': {
        'path': "guidelines/NAME OF YOUR PDF.pdf", # Make sure the PDF is located in the guidelines folder, and specify its path in the dictionary in the format guidelines/file_name.pdf.
        'starting_page': 11,
        'final_page': 142,
        'mark': "### ",
        'images_to_save': [10, 11, 12, 13],
    },
    'gastric': {
        'path': "guidelines/NAME OF YOUR PDF.pdf", # Make sure the PDF is located in the guidelines folder, and specify its path in the dictionary in the format guidelines/file_name.pdf.
        'starting_page': 10,
        'final_page': 116,
        'mark': "### ",
        'images_to_save': [9, 11, 13],
    },
    'pancreatic' : {},
    'hepatic' : {},
    'colorectal' : {},
}
