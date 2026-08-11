# FastQC Analysis

## Tool Overview

FastQC is a quality control application for high throughput sequencing data. It performs quality checks on sequencing files and generates quality reports.

Repository:
https://github.com/s-andrews/FastQC

The repository was analysed using two coding agents, GitHub Copilot and Antigravity, followed by manual verification against the FastQC source code and the EDAM ontology.

---

## Input Files

| Input                       | Format               | Data type                                      | Status    |
| --------------------------- | -------------------- | ---------------------------------------------- | --------- |
| Raw sequencing reads        | FASTQ                | Sequence reads with quality scores             | Confirmed |
| Compressed sequencing reads | FASTQ + gzip         | Compressed sequence reads                      | Confirmed |
| Compressed sequencing reads | FASTQ + bzip2        | Compressed sequence reads                      | Confirmed |
| Alignment files             | BAM                  | Sequence alignment                             | Confirmed |
| Alignment files             | SAM                  | Sequence alignment                             | Confirmed |
| Unmapped alignment files    | UBAM                 | Unmapped sequence alignment                    | Confirmed |
| Nanopore sequencing files   | FAST5                | HDF5-based sequencing data                     | Confirmed |
| Colorspace sequencing reads | csFASTQ              | SOLiD colorspace sequence data                 | Confirmed |
| Standard input              | stdin / FASTQ stream | Sequence reads supplied through standard input | Confirmed |

### Evidence

Manual verification:

* `FastQFile.java` implements FASTQ file processing and handles compressed FASTQ input.
* `SequenceFactory.java` identifies BAM, SAM, UBAM and FAST5 input files.
* `BAMFile.java` delegates BAM/SAM/UBAM parsing to HTSJDK.
* `Fast5File.java` opens FAST5 files using the HDF5 library and accesses internal sequencing data.
* `FastQFile.java` contains colorspace detection and conversion logic for csFASTQ.
* `OfflineRunner.java` supports input through standard input (`stdin`).

### Compression

FastQC supports:

* gzip compression through `.gz`;
* bzip2 compression through `.bz2`.

The underlying biological format remains FASTQ; compression is treated as a wrapper around the sequence data.

The `.bz` extension is not actually decompressed by the FASTQ parser, even if related extensions may appear in GUI filters.

---

## Comparison of Coding Agent Results

The FastQC repository was analysed independently using two coding agents: GitHub Copilot and Antigravity.

Both agents identified the main FastQC input and output formats, including FASTQ, BAM/SAM, FAST5, HTML and ZIP.

Antigravity provided a more detailed source-code-level analysis and identified additional formats and representations that were not included in the initial Copilot analysis, including:

* compressed FASTQ (`.gz` and `.bz2`);
* UBAM;
* csFASTQ / SOLiD colorspace;
* stdin input;
* archive contents such as SVG, PNG, TSV and XSL-FO files.

The independent Antigravity analysis also identified formats that should not be considered supported despite appearing in GUI filters, including:

* Goby;
* Compact Reads;
* `.bz` compression.

The main discrepancies between the two analyses concerned the completeness of the supported format list and some EDAM mappings. These discrepancies were resolved by checking the FastQC source code and the EDAM ontology manually.

The final `analysis.md` therefore reports only formats and mappings supported by repository evidence and manual verification.

---

## Output Files

### Primary Outputs

| Output                 | Format | Data type                    |
| ---------------------- | ------ | ---------------------------- |
| Quality control report | HTML   | Interactive QC report        |
| Results archive        | ZIP    | Compressed QC report archive |

### Evidence

Manual verification:

* `HTMLReportArchive.java` creates the HTML report.
* `HTMLReportArchive.java` creates the ZIP archive.
* The output process generates:

  * `<sample>_fastqc.html`
  * `<sample>_fastqc.zip`

The HTML report is the primary human-readable output, while the ZIP archive contains the detailed report data and supporting files.

---

## ZIP Archive Contents

The following files are contents of the ZIP archive rather than separate primary outputs:

| Archive content      | Format       | Purpose                               |
| -------------------- | ------------ | ------------------------------------- |
| `fastqc_report.html` | HTML         | Copy of the main HTML report          |
| `fastqc_data.txt`    | TSV          | Raw numerical QC module metrics       |
| `summary.txt`        | TSV          | PASS/WARN/FAIL summary for QC modules |
| `fastqc.fo`          | XML / XSL-FO | Report formatting representation      |
| SVG plots            | SVG          | Vector QC plots                       |
| PNG plots            | PNG          | Raster QC plots                       |
| Report icons         | PNG          | Status and report icons               |

### Evidence

The archive contents were verified in `HTMLReportArchive.java` and `AbstractQCModule.java`.

* `HTMLReportArchive.java` writes `fastqc_data.txt` and `summary.txt`.
* `HTMLReportArchive.java` generates the `fastqc.fo` file when the corresponding XSL template is available.
* `AbstractQCModule.java` generates SVG and PNG plot files.
* `HTMLReportArchive.java` copies PNG report icons into the archive.

---

## Coding Agent Analysis

### GitHub Copilot

GitHub Copilot was initially used to inspect the FastQC repository.

The detailed AI outputs and prompts are available in:

`ai_analysis.md`

### Prompts used

**Prompt 1:**
Identify all input file formats accepted by FastQC and provide evidence from the repository.

**Prompt 2:**
Identify all output files generated by FastQC and provide evidence from the repository.

**Prompt 3:**
Suggest appropriate EDAM ontology terms for all identified inputs and outputs.

The initial Copilot analysis identified:

* FASTQ;
* BAM/SAM;
* FAST5;
* HTML;
* ZIP;
* TXT outputs;
* additional formats such as Compact Reads and Goby.

The agent provided evidence from:

* README files;
* documentation;
* source code;
* integration tests.

### Antigravity

Antigravity was subsequently used as an independent local coding agent to perform a second source-code audit of the FastQC repository.

The detailed independent analysis is available in:

`antigravity_analysis.md`

Antigravity identified additional implementation details, including:

* gzip and bzip2 handling;
* UBAM;
* csFASTQ/colorspace processing;
* stdin support;
* SVG and PNG archive contents;
* XSL-FO output;
* unsupported GUI-only formats.

The second analysis was used to identify possible discrepancies and improve the completeness of the final format inventory.

---

## Manual Verification

| Item                   | Copilot result         | Antigravity result | Final verification                        |
| ---------------------- | ---------------------- | ------------------ | ----------------------------------------- |
| FASTQ                  | Identified             | Identified         | Confirmed                                 |
| gzip-compressed FASTQ  | Not detailed           | Identified         | Confirmed                                 |
| bzip2-compressed FASTQ | Not detailed           | Identified         | Confirmed                                 |
| BAM                    | Identified             | Identified         | Confirmed                                 |
| SAM                    | Identified             | Identified         | Confirmed                                 |
| UBAM                   | Not clearly identified | Identified         | Confirmed                                 |
| FAST5                  | Identified             | Identified         | Confirmed                                 |
| csFASTQ                | Not clearly identified | Identified         | Confirmed                                 |
| stdin                  | Not clearly identified | Identified         | Confirmed as input mechanism              |
| HTML output            | Identified             | Identified         | Confirmed                                 |
| ZIP output             | Identified             | Identified         | Confirmed                                 |
| `fastqc_data.txt`      | Identified             | Identified         | Confirmed                                 |
| `summary.txt`          | Identified             | Identified         | Confirmed                                 |
| SVG plots              | Not detailed           | Identified         | Confirmed as archive contents             |
| PNG plots              | Not detailed           | Identified         | Confirmed as archive contents             |
| `fastqc.fo`            | Not detailed           | Identified         | Confirmed as archive content              |
| Compact Reads          | Identified             | Identified         | Excluded: no parser implementation        |
| Goby                   | Identified             | Identified         | Excluded: no parser implementation        |
| `.bz` compression      | Not clearly resolved   | Identified         | Excluded: parser checks `.bz2`, not `.bz` |

---

## EDAM Mapping

| Input/Output      | EDAM term  | EDAM ID       | Match type              | Confidence |
| ----------------- | ---------- | ------------- | ----------------------- | ---------- |
| FASTQ             | FASTQ      | `format_1930` | Exact                   | High       |
| BAM               | BAM        | `format_2572` | Exact                   | High       |
| SAM               | SAM        | `format_2573` | Exact                   | High       |
| UBAM              | BAM        | `format_2572` | Broader concept         | High       |
| FAST5             | HDF5       | `format_3590` | Broader concept         | High       |
| csFASTQ           | FASTQ      | `format_1930` | Related concept         | High       |
| stdin             | N/A        | N/A           | No suitable format term | High       |
| HTML report       | HTML       | `format_2331` | Exact                   | High       |
| ZIP archive       | ZIP format | `format_3987` | Exact                   | High       |
| `fastqc_data.txt` | TSV        | `format_3475` | Exact                   | High       |
| `summary.txt`     | TSV        | `format_3475` | Exact                   | High       |
| SVG plots         | SVG        | `format_3604` | Exact                   | High       |
| PNG plots         | PNG        | `format_3603` | Exact                   | High       |
| Report icons      | PNG        | `format_3603` | Exact                   | High       |
| `fastqc.fo`       | XML        | `format_2332` | Broader concept         | High       |

### EDAM Mapping Limitations

* **FAST5 → HDF5 (`format_3590`)** is a broader mapping because no FAST5-specific EDAM format term was identified.
* **csFASTQ → FASTQ (`format_1930`)** is a related mapping because EDAM contains a csFASTA term but no specific colorspace FASTQ term.
* **UBAM → BAM (`format_2572`)** is a broader mapping because there is no separate UBAM EDAM term.
* **stdin** is an input/transport mechanism rather than a biological data format and therefore has no EDAM format identifier.
* **`fastqc.fo` → XML (`format_2332`)** is a broader mapping because no specific XSL-FO EDAM format term was identified.

---

## Unsupported / Excluded Formats

### FASTA

FASTA is not accepted as a valid input format because it does not contain the quality score lines required by the FASTQ parser.

A FASTA sequence beginning with `>` is therefore expected to fail FASTQ parsing.

### Goby

Goby is listed in some GUI file filters, but no corresponding Goby parser implementation or required dependencies were identified in the repository.

It is therefore excluded from the verified supported input formats.

### Compact Reads

Compact Reads is also present in GUI-related file filters but lacks an implemented parser in the repository.

It is therefore excluded from the verified supported input formats.

### `.bz` compression

The FASTQ parser explicitly handles `.bz2` compression but does not decompress files ending in `.bz`.

Therefore `.bz` is excluded from the verified compression formats.

---

## AI Evaluation

The two coding agents were useful for complementary purposes.

GitHub Copilot successfully identified the main input and output formats and provided an initial overview of the relevant source files.

Antigravity provided a more detailed independent source-code audit and identified additional implementation details that were not present in the initial Copilot analysis, including compressed FASTQ, UBAM, csFASTQ, stdin and archive-level outputs.

The comparison also revealed discrepancies that required manual verification. In particular, EDAM mappings suggested by an AI agent were not accepted automatically and were checked against the ontology.

One important correction concerned FAST5. The final mapping uses the broader HDF5 EDAM term (`format_3590`) rather than treating FAST5 as an exact EDAM format.

Another important correction concerned `.bz` compression. Although related extensions may appear in GUI filters, the parser implementation checks for `.bz2`, not `.bz`.

This demonstrates that coding agents are useful for repository exploration and discovery, but their results must be manually validated against the actual source code and the relevant ontology.

---

## Final Conclusion

FastQC accepts a range of sequencing and alignment inputs, including FASTQ, compressed FASTQ, BAM, SAM, UBAM, FAST5, csFASTQ and FASTQ data supplied through stdin.

The primary outputs are an HTML quality control report and a ZIP archive containing detailed QC data, summaries, plots, icons and supporting report files.

The repository was analysed using two independent coding agents, GitHub Copilot and Antigravity. Their findings were compared and subsequently verified against the FastQC source code and EDAM ontology.

The final analysis distinguishes between:

* directly verified formats;
* broader or related EDAM mappings;
* archive-level output files;
* unsupported or GUI-only formats.

This combined approach reduced the risk of relying on undocumented functionality or incorrect AI-generated ontology mappings and provided a more complete and evidence-based description of FastQC input and output formats.
