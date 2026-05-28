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

```{bash}
make
```

