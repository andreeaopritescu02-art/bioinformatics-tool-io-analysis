# Bioinformatics Tool I/O Analysis

> **Project 4 – Using Coding Agents to Find Input and Output Formats of Bioinformatics Tools**

Exploring the use of **AI coding agents** to identify input and output formats of bioinformatics tools, collect repository-based evidence, and map the identified formats to the **EDAM ontology**.

## Overview

This project investigates whether AI coding agents, such as **GitHub Copilot**, can assist in identifying the input and output data formats supported by bioinformatics software.

The analysis is performed by exploring public source-code repositories and their documentation. AI-generated findings are then reviewed against repository evidence and mapped to relevant **EDAM ontology** concepts.

The project focuses on three bioinformatics tools:

* **FastQC**
* **BWA**
* **SAMtools**

The final results combine AI-assisted analysis, manual verification, and EDAM ontology validation.

## Objectives

* Explore public bioinformatics software repositories.
* Identify supported input and output formats.
* Collect supporting evidence from documentation and source code.
* Map identified formats to EDAM ontology terms.
* Verify AI-generated findings against repository evidence.
* Identify ambiguous or unsupported EDAM mappings.
* Document the analysis in a structured and reproducible way.

## Methodology

The analysis follows the workflow below:

```text
Bioinformatics tool repository
            ↓
     AI-assisted analysis
            ↓
 Input / output identification
            ↓
    Repository evidence
            ↓
    Manual verification
            ↓
      EDAM mapping
            ↓
  Mapping validation
            ↓
       Final results
```

AI-generated results are treated as **candidate findings** and are not considered final until they are supported by evidence from the analyzed repository.

## Tools Analyzed

| Tool         | Repository          | Analysis Status |
| ------------ | ------------------- | --------------- |
| **FastQC**   | `s-andrews/FastQC`  | ✅ Completed     |
| **BWA**      | `lh3/bwa`           | ✅ Completed     |
| **SAMtools** | `samtools/samtools` | ✅ Completed     |

All three selected tools have been analyzed for their supported input and output formats.

## EDAM Ontology

The identified formats are mapped to concepts from the **EDAM ontology**, including file formats and data types.

The mapping process distinguishes between:

* verified mappings;
* ambiguous mappings;
* concepts that could not be found;
* formats without a suitable EDAM mapping.

For SAMtools, an additional Python validation script was developed to automatically verify proposed EDAM mappings against the EDAM ontology.

## Repository Structure

```text
bioinformatics-tool-io-analysis/
│
├── README.md
│
├── tools/
│   ├── FastQC/
│   ├── BWA/
│   └── SAMtools/
│
├── results/
│
├── prompts/
│
├── report/
│
└── references/
```

Each tool directory contains the analysis and supporting files associated with that tool.

## Results

The project provides:

* identified input formats;
* identified output formats;
* repository evidence supporting the findings;
* EDAM ontology mappings;
* validation results;
* documentation of ambiguous or unresolved mappings.

Detailed results are available in the corresponding tool directories and project result files.

## SAMtools EDAM Validation

The SAMtools analysis includes an automated EDAM mapping verification script:

```text
tools/SAMtools/verify_edam_mappings.py
```

The script retrieves the EDAM ontology, parses its concepts, checks proposed mappings, and reports verified, ambiguous, missing, and unmapped concepts.

This provides an additional validation step beyond the AI-generated analysis.

## Project Status

**Analysis completed for all three selected tools.**

Current work focuses on:

* final consistency checks;
* reviewing EDAM mappings;
* resolving ambiguities where possible;
* cleaning generated files;
* improving documentation and repository presentation.

## Key Principle

> **AI-generated findings are treated as candidate results and must be supported by repository evidence and verified before being considered final.**

This approach helps evaluate the usefulness and reliability of AI coding agents for technical and scientific repository analysis.

## Technologies and Resources

* Python
* Git / GitHub
* GitHub Copilot
* EDAM Ontology
* Bioinformatics software repositories
* Markdown
* JSON
