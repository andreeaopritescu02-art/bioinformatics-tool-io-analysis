# FastQC AI Analysis

## Coding Agent

GitHub Copilot

## Prompt

Analyze this repository and identify all input file formats accepted by FastQC.

For each input:
- provide the file format;
- describe the biological data type;
- provide evidence from README files, documentation, examples, tests, or source code.

---

## AI Results

### FASTQ

Biological data:
Raw sequencing reads with per-base quality scores.

Evidence found by AI:
- README.md mentions FastQ files.
- INSTALL.md provides FASTQ usage examples.
- FastQFile.java implements FASTQ reading.

---

### BAM / SAM / UBAM

Biological data:
Aligned or unaligned sequencing reads.

Evidence found by AI:
- README.md mentions BAM input.
- SequenceFactory.java detects BAM/SAM/UBAM extensions.
- fastqc.pl supports bam and sam modes.

---

### FAST5

Biological data:
Oxford Nanopore sequencing files.

Evidence found by AI:
- INSTALL.md describes nanopore FAST5 processing.
- Fast5File.java handles FAST5 files.

---

### Other formats

AI identified:
- .compact-reads
- .goby
- stdin streaming

These require additional verification.

---

## AI Evaluation

The coding agent successfully identified the main input formats and provided evidence from multiple repository locations.

# FastQC AI Analysis

## Output File Analysis

### Main outputs identified by GitHub Copilot

| Output | Format | Purpose | Evidence |
|---|---|---|---|
| <sample>_fastqc.html | HTML | Interactive quality control report | HTMLReportArchive.java, integration tests |
| <sample>_fastqc.zip | ZIP | Archive containing the complete QC report | HTMLReportArchive.java |
| fastqc_data.txt | TXT | Machine-readable QC results | HTMLReportArchive.java, test snapshots |
| summary.txt | TXT | Summary of module results | HTMLReportArchive.java |

### Additional generated files

The coding agent also identified supporting files generated inside the report archive:

- PNG and SVG images used for plots.
- PNG icons used in the HTML report.
- Optional XSL-FO file for report conversion.

These were considered secondary outputs because they are components of the main QC report.
## EDAM Suggestions

The coding agent was asked to suggest EDAM terms for identified inputs and outputs.

Suggested mappings:

| Item | EDAM term | EDAM ID | Confidence |
|---|---|---|---|
| FASTQ | FASTQ | EDAM:format_1930 | High |
| BAM | BAM | EDAM:format_2572 | High |
| SAM | SAM | EDAM:format_2573 | High |
| FAST5 | FAST5 | EDAM:format_3854 | Medium |
| HTML report | HTML | EDAM:format_2332 | High |
| ZIP archive | ZIP | EDAM:format_3987 | High |

The agent recommended manual verification for uncertain data-type mappings.

Manual verification is required before accepting all suggested formats.
