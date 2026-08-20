# SAMtools AI Analysis

## Coding Agent

GitHub Copilot

---

## Prompt 1 - Input File Analysis

Analyze this repository and identify all input file formats accepted by SAMtools.

For each input:

- provide the file format;
- describe the biological data type;
- provide evidence from README files, documentation, examples, tests, or source code.

Repository analyzed:

https://github.com/samtools/samtools

---

## AI Results

### SAM

Biological data: Sequence alignment records in the text-based Sequence Alignment/Map format.

Evidence found by AI:

- README mentions SAM as a supported alignment format.
- `doc/samtools-view.1` describes SAM input.
- `sam_view.c` uses the SAMtools/HTSlib alignment-file reading interface.

### BAM

Biological data: Binary compressed alignment records.

Evidence found by AI:

- README mentions BAM as a supported alignment format.
- `doc/samtools-view.1` documents BAM input.
- `bedcov.c` opens alignment files using `sam_open_format()`.

### CRAM

Biological data: Reference-aware compressed alignment records.

Evidence found by AI:

- README mentions CRAM as a supported alignment format.
- `doc/samtools-view.1` documents CRAM input.
- `bam_plcmd.c` uses `sam_open_format()` and CRAM-specific options.

### FASTQ

Biological data: Sequencing reads with per-base quality scores.

Evidence found by AI:

- `bam_import.c` implements the `samtools import` command.
- `doc/samtools-import.1` describes reading FASTQ files.
- Compressed FASTQ input is supported.

### FASTA

Biological data: Reference nucleotide sequences.

Evidence found by AI:

- `faidx.c` implements FASTA indexing and sequence retrieval.
- `dict.c` reads FASTA files using `gzopen()`.
- `doc/samtools-dict.1` documents FASTA input.

### BED

Biological data: Genomic regions or features.

Evidence found by AI:

- `bedcov.c` reads BED files containing genomic regions.
- `doc/samtools-bedcov.1` documents BED input.
- BED records are parsed directly by the command implementation.

### Auxiliary index files

AI also identified several auxiliary files used by SAMtools:

- FAI (`.fa.fai`, `.fasta.fai`) - FASTA index files.
- BAI (`.bam.bai`) - BAM index files.
- CSI (`.bam.csi`) - coordinate-sorted index files.
- CRAI (`.cram.crai`) - CRAM index files.

Evidence found by AI:

- `bam_tview.c` and other source files use `fai_load()` and `sam_index_load()`.
- `sam_utils.c` handles index suffixes.
- `doc/samtools-index.1` documents BAI, CSI and CRAI indexes.

FQI (`.fq.fai`) was not included because the agent did not find sufficient evidence that it is read as a standalone auxiliary input.

---

## AI Evaluation

The coding agent successfully identified the main SAMtools input formats and provided repository-based evidence.

The main formats identified were:

- SAM;
- BAM;
- CRAM;
- FASTQ;
- FASTA;
- BED.

The agent also identified auxiliary/index files used during processing:

- FAI;
- BAI;
- CSI;
- CRAI.

The analysis performed well when information was explicitly available in:

- README files;
- command documentation;
- source code;
- HTSlib-related file handling.

Manual verification was still required to distinguish primary input formats from auxiliary/index files and to exclude FQI where sufficient repository evidence was not found.

## Manual verification is required before accepting all suggested formats.