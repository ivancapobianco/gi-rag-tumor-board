## Dummy Guideline Corpora

This folder contains fully synthetic guideline excerpts provided solely to demonstrate
the structure and functionality of the retrieval pipeline.

No copyrighted guideline text is included.
No clinical use is intended.

The real study used German S3 and NCCN clinical practice guidelines accessed under
institutional licenses.

The `dummy_guidelines_with_embeddings.json` file contains the same chunks with
**dummy embeddings** added for demonstration purposes. These embeddings are placeholders
and do not reflect real semantic vectors.

The code to generate real embeddings for the JSON corpora is located in the
`processing` folder (`embedding.py`).

## Note

Some corpus chunks intentionally include `<chart>` tags and embedded JSON tables.
Text within `<chart>` tags represents content manually transcribed or described
from guideline figures originally presented as images.
Embedded JSON tables represent tabular guideline content automatically extracted
and structured via table parsing.

This heterogeneous formatting reflects real-world multimodal guideline documents
and is preserved to demonstrate the robustness of the retrieval pipeline.
