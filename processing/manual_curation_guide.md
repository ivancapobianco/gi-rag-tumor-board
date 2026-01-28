# Manual Corpus Curation Guide

This document describes the manual curation steps applied to create the **Selected (Curated) Corpus** from the **Full Corpus**.

## Overview

After automated PDF extraction and chunking, we manually reviewed all guideline chunks to exclude content not relevant for treatment decision-making. This reduced retrieval noise and improved RAG performance.

## Curation Criteria

### ✅ INCLUDED Sections (Treatment-Relevant)

- **Treatment algorithms and decision trees**
- **Therapy recommendations** (surgery, systemic, radiation, multimodal)
- **Staging-specific treatment protocols**
- **Follow-up and surveillance guidelines**
- **Post-treatment monitoring**
- **Salvage therapy options**
- **Treatment modification criteria**

### ❌ EXCLUDED Sections (Non-Treatment)

- **Epidemiology and incidence data**
- **Risk factors and etiology**
- **Prevention strategies**
- **Screening recommendations** (not decision-relevant for diagnosed patients)
- **Initial diagnostic workup** (imaging, lab tests for diagnosis)
- **Pathology classification** (background knowledge, not decision-making)
- **Health economics and cost-effectiveness**
- **Quality of life assessments** (descriptive sections)
- **Methodology sections** (how guidelines were developed)

## Manual Review Process

### Step 1: Initial Automated Processing
1. Extract PDFs to markdown using `pymupdf4llm`
2. Clean and chunk text using `processing/extract_guidelines.py`
3. Parse tables to JSON using `processing/clean_chunks.py`
4. Save to Excel files

### Step 2: Manual Review (You Cannot Automate This)
1. Open each guideline Excel file
2. Read each chunk and classify as:
   - **KEEP** - Treatment-relevant
   - **REMOVE** - Background/non-treatment

3. Mark chunks for removal in a new column `curation_status`
4. Save as `{guideline}_chunks_curated.xlsx`

### Step 3: Create Two Corpora
- **Full Corpus**: All chunks from Step 1
- **Selected Corpus**: Only KEEP chunks from Step 2

## Statistics

| Corpus Type | Total Chunks | Avg Chunk Size | Tables | Figures |
|-------------|--------------|----------------|--------|---------|
| Full | 15,420 | 384 tokens | 247 | 189 |
| Selected | 10,683 | 412 tokens | 198 | 156 |

**Reduction**: ~31% of chunks removed as non-treatment-relevant

## Replication Instructions

To replicate our curation:

1. **Download guidelines** per `guidelines/README.md`
2. **Run automated processing**:
```bash
   python processing/extract_guidelines.py
   python processing/clean_chunks.py
```
3. **Manual review**: Review each chunk and decide KEEP/REMOVE
4. **Save curated corpus**: Mark chunks in Excel
5. **Create embeddings** for both full and curated corpora

**Note**: Manual curation is subjective and requires domain expertise. Your curation decisions may differ from ours, which is expected and acceptable.

## Example Curation Decisions

### Example 1: KEEP (Treatment-Relevant)
```
Chunk: "Bei lokal fortgeschrittenen Ösophaguskarzinomen (cT3-4) wird eine 
neoadjuvante Radiochemotherapie empfohlen, gefolgt von chirurgischer Resektion..."

Decision: KEEP - Direct treatment recommendation
```

### Example 2: REMOVE (Epidemiology)
```
Chunk: "Das Ösophaguskarzinom ist die achthäufigste Krebserkrankung weltweit. 
Die Inzidenz beträgt 5,2 pro 100.000 Einwohner..."

Decision: REMOVE - Epidemiological background, not treatment-relevant
```

### Example 3: REMOVE (Screening)
```
Chunk: "Bei Patienten mit Barrett-Ösophagus sollte eine endoskopische 
Überwachung alle 3-5 Jahre erfolgen..."

Decision: REMOVE - Screening recommendation for undiagnosed patients
```

## Files Structure After Curation
```
Guidelines_xlsx/
├── OE-CA_chunks_cleaned.xlsx              # Full corpus
├── OE-CA_chunks_curated.xlsx              # Selected corpus
├── OE-CA_chunks_cleaned_embeddings.xlsx   # Full corpus with embeddings
└── OE-CA_chunks_curated_embeddings.xlsx   # Selected corpus with embeddings
```

## Questions?

If you have questions about specific curation decisions, please open an issue in the repository.
