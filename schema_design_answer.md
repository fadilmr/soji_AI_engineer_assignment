# Schema Design and Extraction Approach

## Deliverable 1: JSON Schema with Pydantic Models

### JSON Schema

The extracted rules (ad_rules.json) follow this structure:

```json
{
  "ad_id": "FAA-2025-23-53",
  "applicability_rules": {
    "aircraft_models": ["MD-11", "MD-11F", "DC-10-30F", ...],
    "msn_constraints": null,
    "excluded_if_modifications": [],
    "required_modifications": []
  }
}
```

## Deliverable 4: Schema Design and Extraction Approach

### 1. Schema Design

**Structure:**

- **ad_id**: Unique identifier (e.g., "FAA-2025-23-53")
- **applicability_rules**: Nested object containing:
  - **aircraft_models**: List of affected aircraft models (e.g., ["MD-11", "A320-214"])
  - **msn_constraints**: Serial number constraints (null = applies to all MSNs)
  - **excluded_if_modifications**: Modifications that exempt aircraft from this AD
  - **required_modifications**: Modifications required for AD to apply

### 2. Extraction Process

**Step 1: Document Acquisition**

1. Scrape AD webpage (HTML content)
2. Download attached PDF documents
3. Store in structured folders: `ad_data/{ad_name}/`

**Step 2: LLM-Based Extraction**

1. Parse PDF using OCR API (dotsOCR)
2. Send document text to LLM with structured prompt
3. LLM (deployed with vLLM) extracts applicability rules and returns JSON
4. Save results to `ad_rules.json`

**Why use LLM?**

- ADs have inconsistent formats (FAA vs EASA)
- Natural language understanding (interprets "embodied in production" vs "accomplished in service")
- No manual regex pattern maintenance
- Handles context and distinguishes exclusions from requirements


### 3. Testing & Validation

**Two Validation Methods:**

1. **Rule-based**: Fast, deterministic Python logic
2. **LLM-based**: Natural language reasoning for cross-validation

