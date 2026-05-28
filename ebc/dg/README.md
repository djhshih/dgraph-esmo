# Decision graphs for EBC

This directory contains decision-graph source files for early breast cancer (EBC) workflows, written in Python using the `dgraph` API.

## Contents

- `ebc-dx.dg` - diagnosis and staging of EBC
- `ebc.dg` - high-level overview of EBC treatment
- `ebc-aln.dg` - management of axillary lymph node (ALN) involvement in EBC
- `ebc-her2-pos.dg` - HER2-positive EBC treatment pathway
- `ebc-hr-pos.dg` - adjuvant endocrine therapy in HR-positive EBC
- `ebc-tnbc.dg` - early triple-negative breast cancer (TNBC) pathway
- `Makefile` - converts DOT files from `../dot/` into `.dg` files

## Current structure

The `.dg` files define graphs with the `dgraph` package:

- `from dgraph.graph import branch, chain, node`
- `import dgraph.condition as dc`

Common construction patterns used in this directory:

- `node(label, ...)` for a graph node
- `chain(a, b, c)` for a linear sequence of nodes
- `branch(label, condition, subtree)` for condition-driven branching
- `dc.has(...)`, `dc.has_any(...)`, and `dc.has_all(...)` for branch conditions

## Build flow

These files are currently generated from DOT sources in `../dot/`.

`Makefile` uses:

```make
indir = ../dot

all: ebc.dg ebc-aln.dg ebc-dx.dg ebc-her2-pos.dg ebc-hr-pos.dg ebc-tnbc.dg

%.dg: $(indir)/%.dot
	dot2dg.py -o $@ $<
```

So the workflow is:

1. Maintain or extract the source graph in DOT format under `../dot/`
2. Run `make` in this directory
3. Generate the corresponding `.dg` files with `dot2dg.py`

To clean generated files:

```sh
make clean
```

## Graph summaries

### `ebc-dx.dg`
Diagnosis and staging flow for EBC, including:

- bilateral mammogram and ultrasound
- biopsy and confirmed diagnosis
- biomarker assessment: ER, PgR, HER2, Ki-67
- optional gene expression assays and gBRCA1/2 testing when relevant
- staging, history, physical exam, blood work-up, and imaging
- clip marking when neoadjuvant treatment and BCS are planned

### `ebc.dg`
Top-level treatment overview with branches for:

- `HR+` -> endocrine therapy
- `premenopausal receiving_ofs` or `postmenopausal` -> adjuvant bisphosphonates
- `HR+/HER2-` -> neoadjuvant therapy -> surgery +/- RT -> systemic treatment
- `HER2+`
  - `cT1 N0` -> surgery +/- RT -> systemic treatment
  - `>=cT2` or `cN+` -> neoadjuvant therapy -> surgery +/- RT -> systemic treatment
- `TNBC`
  - `cT1a` or `cT1b N0` -> surgery +/- RT -> systemic treatment
  - `cT1c-4` or `N+` -> neoadjuvant therapy -> surgery +/- RT -> systemic treatment

### `ebc-aln.dg`
Management of axillary lymph node involvement in EBC, covering:

- primary surgery indicated vs PST indicated
- `cN0/iN0` and `cN+/iN+` pathways
- SLNB, ALND, RT, AMAROS, and ACOSOG-Z0011 decision branches
- post-neoadjuvant handling of `ycN0/ypN0` and `ycN+/ypN+`
- SLN/TAD-based escalation or de-escalation of regional treatment

Note: this file currently contains some repeated subtrees for PST-related logic.

### `ebc-her2-pos.dg`
HER2-positive EBC pathway with branches for:

- `cT1 cN0`
  - surgery and locoregional RT if indicated
  - adjuvant therapy based on `pT1 pN0`, `>=pT2 pN0`, or `pN+`
- `>=cT2` or `cN+`
  - neoadjuvant `ChT-HP`
  - surgery and RT if indicated
  - post-surgical management for `pCR` vs residual invasive disease
  - trastuzumab / HP continuation or `T-DM1`
  - adjuvant ET when HR-positive

### `ebc-hr-pos.dg`
Adjuvant endocrine therapy in HR-positive EBC:

- premenopausal
  - Luminal A-like stage I -> tamoxifen
  - Luminal A-like stage II-III or Luminal B-like stage I-III -> OFS-tamoxifen or OFS-AI
- postmenopausal
  - tamoxifen followed by AI
  - AI
  - AI followed by tamoxifen
  - tamoxifen

### `ebc-tnbc.dg`
Early TNBC pathway, including:

- `gBRCA1/2` testing
- `cT1a` or `cT1b N0`
  - surgery and whole breast RT if indicated
  - management for `pT1a pN0`, `pT1b pN0`, and `>pT1b any pN`
- `cT1c-T4` or `N+`
  - branches for `<cT2 N0` and `>=cT2 or N+`
  - taxane-(carbo)platin-AC/EC neoadjuvant treatment
  - surgery and locoregional RT if indicated
  - management of `pCR` vs residual disease
  - pembrolizumab, capecitabine, or olaparib depending on response and `gBRCA1/2` status

## Notes

- These `.dg` files appear to be generated artifacts rather than hand-authored source.
- The authoritative editable graph inputs for this directory are the DOT files in `../dot/`.
- PDFs are built from DOT files in `../dot/Makefile`, and rendered outputs exist under `../dot/pdf/`.
- The extraction prompt used for DOT generation is stored in `../dot/prompt.txt`.
