# FastQC Analysis

## Tool Overview

FastQC is a quality control application for high throughput sequencing data.
It performs quality checks on raw sequencing files and generates quality reports.

## Input Files

| Input | Format | Data type |
|---|---|---|
| Raw sequencing reads | FASTQ | Sequence reads |
| Alignment files | BAM | Sequence alignment |

Evidence:

FastQC README states that the tool analyzes raw sequence files in FASTQ or BAM format.

## Output Files

| Output | Format | Data type |
|---|---|---|
| Quality control report | HTML | Report |
| Results archive | ZIP | Report package |

Evidence:

FastQC README states that the program generates HTML reports for processed files.

## EDAM Mapping

## EDAM Mapping

| Input/Output | EDAM term | EDAM ID | Type | Confidence |
|---|---|---|---|---|
| FASTQ | FASTQ | EDAM:format_1930 | Format | High |
| BAM | BAM | EDAM:format_2572 | Format | High |
| SAM | SAM | EDAM:format_2573 | Format | High |
| FAST5 | FAST5 | EDAM:format_3854 | Format | Medium |
| HTML report | HTML | EDAM:format_2332 | Format | High |
| ZIP archive | ZIP | EDAM:format_3987 | Format | High |
| fastqc_data.txt | Plain text + QC report | EDAM format/data terms | Format + Data | Medium |
| summary.txt | Plain text + QC summary | EDAM format/data terms | Format + Data | Medium |

## AI Evaluation

## AI Evaluation

The coding agent was able to suggest suitable EDAM format terms for common file formats such as FASTQ, BAM, SAM, HTML and ZIP.

For less standardized outputs, such as FastQC internal text reports, the agent correctly identified the need for both:
- a file format annotation;
- a semantic data type annotation.

However, the agent showed uncertainty for some EDAM data identifiers and recommended manual verification.
