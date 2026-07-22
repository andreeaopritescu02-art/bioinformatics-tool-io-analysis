# FastQC Analysis

## Tool Overview

FastQC is a quality control application for high throughput sequencing data. It performs quality checks on raw sequencing files and generates quality reports.

Repository:
https://github.com/s-andrews/FastQC

---

## Input Files

| Input | Format | Data type |
|---|---|---|
| Raw sequencing reads | FASTQ | Sequence reads |
| Alignment files | BAM/SAM | Sequence alignment |
| Nanopore sequencing reads | FAST5 | Sequence reads |

### Evidence

Manual verification:

- README.md states that FastQC analyzes raw sequence files in FASTQ or BAM format.
- `FastQFile.java` implements FASTQ file processing.
- `SequenceFactory.java` identifies BAM and SAM input files.
- `Fast5File.java` implements FAST5 file handling.

---

## Output Files

| Output | Format | Data type |
|---|---|---|
| Quality control report | HTML | Report |
| Results archive | ZIP | Report archive |
| Detailed QC data | TXT | Quality control data |
| Summary results | TXT | Summary report |

### Evidence

Manual verification:

- `HTMLReportArchive.java` creates HTML reports and ZIP archives.
- The same class generates:
  - `fastqc_report.html`
  - `<sample>_fastqc.html`
  - `<sample>_fastqc.zip`
  - `fastqc_data.txt`
  - `summary.txt`

Integration tests confirm the generated report structure.

---

## Coding Agent Analysis

The coding agent (GitHub Copilot) was used to inspect the FastQC repository.

The detailed AI output and prompts are available in:

`ai_analysis.md`

The agent identified:
- FASTQ, BAM/SAM, and FAST5 input formats;
- HTML, ZIP, TXT output files;
- additional internal formats such as compact-reads and goby.

The agent provided evidence from:
- README files;
- documentation;
- source code;
- integration tests.

---

## Manual Verification

| Item | AI suggestion | Manual evidence | Result |
|---|---|---|---|
| FASTQ input | Identified | README.md, FastQFile.java | Confirmed |
| BAM/SAM input | Identified | SequenceFactory.java | Confirmed |
| FAST5 input | Identified | Fast5File.java | Confirmed |
| HTML output | Identified | HTMLReportArchive.java | Confirmed |
| ZIP output | Identified | HTMLReportArchive.java | Confirmed |
| fastqc_data.txt | Identified | HTMLReportArchive.java | Confirmed |
| summary.txt | Identified | HTMLReportArchive.java | Confirmed |
| compact-reads | Identified | SequenceFileFilter.java | Partially confirmed |
| goby | Identified | SequenceFileFilter.java | Partially confirmed |

---

## EDAM Mapping

| Input/Output | EDAM term | EDAM ID | Type | Confidence |
|---|---|---|---|---|
| FASTQ | FASTQ | EDAM:format_1930 | Format | High |
| BAM | BAM | EDAM:format_2572 | Format | High |
| SAM | SAM | EDAM:format_2573 | Format | High |
| FAST5 | FAST5 | EDAM:format_3854 | Format | Medium |
| HTML report | HTML | EDAM:format_2332 | Format | High |
| ZIP archive | ZIP | EDAM:format_3987 | Format | High |
| fastqc_data.txt | Plain text + QC report | Requires data term verification | Format + Data | Medium |
| summary.txt | Plain text + QC summary | Requires data term verification | Format + Data | Medium |

---

## AI Evaluation

The coding agent successfully identified the main input and output formats of FastQC by analysing documentation, source code and tests.

The agent performed well when formats were explicitly defined in:
- README files;
- command-line options;
- parser classes;
- output generation code.

For less standardized outputs, such as FastQC internal text reports, the agent correctly identified that both:
- a file format annotation;
- a semantic data type annotation

are required.

However, some EDAM data identifiers required additional manual verification.
