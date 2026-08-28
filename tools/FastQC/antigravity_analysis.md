# Antigravity Analysis – FastQC Input and Output Formats

## 1. Independent Evidence Matrix

| Item                           | I/O    | Extension/Representation                                           | Source File                               | Class                           | Method                                         | Code Evidence                                                                                                                                 | EDAM Term  | EDAM ID       | Match Type                         | Confidence | Caveat                                                                                        |
| ------------------------------ | ------ | ------------------------------------------------------------------ | ----------------------------------------- | ------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------- | ---------------------------------- | ---------- | --------------------------------------------------------------------------------------------- |
| **FASTQ**                      | Input  | `.fastq`<br>`.fq`<br>`.txt`                                        | `SequenceFactory.java` / `FastQFile.java` | `SequenceFactory` / `FastQFile` | `getSequenceFile` / `<init>`                   | `SequenceFactory` routes unrecognized file extensions to `FastQFile`. `FastQFile` wraps the file stream in a `BufferedReader`.                | FASTQ      | `format_1930` | exact EDAM format match            | High       | None                                                                                          |
| **FASTQ + gzip**               | Input  | `.fastq.gz`<br>`.fq.gz`<br>`.txt.gz`                               | `FastQFile.java`                          | `FastQFile`                     | `<init>`                                       | Checks whether the filename ends with `.gz` or has a gzip MIME type, then instantiates `MultiMemberGZIPInputStream`.                          | FASTQ      | `format_1930` | exact EDAM format match            | High       | Gzip is a compression method and is separated from the underlying biological format in EDAM.  |
| **FASTQ + bzip2**              | Input  | `.fastq.bz2`<br>`.fq.bz2`<br>`.fastq.bz`<br>`.fq.bz`<br>`.txt.bz2` | `FastQFile.java`                          | `FastQFile`                     | `<init>`                                       | Checks for the `.bz2` extension and instantiates `BZip2CompressorInputStream`.                                                                | FASTQ      | `format_1930` | exact EDAM format match            | High       | Bzip2 is a compression method and is separated from the underlying biological format in EDAM. |
| **BAM**                        | Input  | `.bam`                                                             | `SequenceFactory.java` / `BAMFile.java`   | `SequenceFactory` / `BAMFile`   | `getSequenceFile` / `<init>`                   | `SequenceFactory` detects `.bam` extensions. `BAMFile` opens the stream using HTSJDK's `SamReaderFactory`.                                    | BAM        | `format_2572` | exact EDAM format match            | High       | Low-level binary decoding is delegated entirely to the HTSJDK library.                        |
| **SAM**                        | Input  | `.sam`                                                             | `SequenceFactory.java` / `BAMFile.java`   | `SequenceFactory` / `BAMFile`   | `getSequenceFile` / `<init>`                   | `SequenceFactory` detects `.sam` extensions. `BAMFile` parses the files using HTSJDK's `SamReaderFactory`.                                    | SAM        | `format_2573` | exact EDAM format match            | High       | Low-level parsing is delegated entirely to the HTSJDK library.                                |
| **UBAM**                       | Input  | `.ubam`                                                            | `SequenceFactory.java` / `BAMFile.java`   | `SequenceFactory` / `BAMFile`   | `getSequenceFile` / `<init>`                   | `SequenceFactory` detects `.ubam` extensions. `BAMFile` instantiates the HTSJDK parser on the stream.                                         | BAM        | `format_2572` | broader EDAM concept               | High       | Mapped to the broader BAM format because there is no separate UBAM EDAM term.                 |
| **FAST5**                      | Input  | `.fast5`                                                           | `SequenceFactory.java` / `Fast5File.java` | `SequenceFactory` / `Fast5File` | `getSequenceFile` / `<init>`                   | `SequenceFactory` detects `.fast5` extensions. `Fast5File` opens the file via `HDF5Factory.openForReading` to parse HDF5 structures.          | HDF5       | `format_3590` | broader EDAM concept               | High       | Mapped to HDF5 because a FAST5-specific EDAM term was not identified.                         |
| **csFASTQ / SOLiD colorspace** | Input  | `.csfastq`                                                         | `FastQFile.java`                          | `FastQFile`                     | `checkColorspace` / `convertColorspaceToBases` | `FastQFile` evaluates the first read using a regex for color-space sequence values and decodes color codes to nucleotides for quality checks. | FASTQ      | `format_1930` | related EDAM concept               | High       | csFASTQ is mapped to FASTQ as a related concept, not an exact EDAM match.                     |
| **stdin**                      | Input  | `stdin`                                                            | `OfflineRunner.java` / `FastQFile.java`   | `OfflineRunner` / `FastQFile`   | `<init>`                                       | `OfflineRunner` checks for input named `"stdin"`. `FastQFile` wraps standard input `System.in` in a `BufferedReader`.                         | N/A        | N/A           | no suitable EDAM format term found | High       | stdin is a transport/input mechanism rather than a file/data format.                          |
| **HTML report**                | Output | `.html`                                                            | `HTMLReportArchive.java`                  | `HTMLReportArchive`             | `<init>`                                       | Writes a standalone interactive HTML report directly to disk using `PrintWriter`.                                                             | HTML       | `format_2331` | exact EDAM format match            | High       | Primary output file written directly to disk.                                                 |
| **ZIP archive**                | Output | `.zip`                                                             | `HTMLReportArchive.java`                  | `HTMLReportArchive`             | `<init>`                                       | Instantiates a `ZipOutputStream` to generate a compressed ZIP file directly on disk.                                                          | ZIP format | `format_3987` | exact EDAM format match            | High       | Primary output file written directly to disk.                                                 |
| **fastqc_data.txt**            | Output | `fastqc_data.txt`                                                  | `HTMLReportArchive.java`                  | `HTMLReportArchive`             | `<init>`                                       | Writes raw, tab-delimited module metrics directly into the `ZipOutputStream` entry.                                                           | TSV        | `format_3475` | exact EDAM format match            | High       | Archive content.                                                                              |
| **summary.txt**                | Output | `summary.txt`                                                      | `HTMLReportArchive.java`                  | `HTMLReportArchive`             | `<init>`                                       | Writes overall check statuses (PASS/WARN/FAIL) to a tab-separated `ZipOutputStream` entry.                                                    | TSV        | `format_3475` | exact EDAM format match            | High       | Archive content.                                                                              |
| **SVG plots**                  | Output | `.svg`                                                             | `AbstractQCModule.java`                   | `AbstractQCModule`              | `writeDefaultImage` / `writeSpecificImage`     | Generates and saves SVG plots inside the ZIP's `Images/` folder using `SVGImageSaver`.                                                        | SVG        | `format_3604` | exact EDAM format match            | High       | Archive content.                                                                              |
| **PNG plots**                  | Output | `.png`                                                             | `AbstractQCModule.java`                   | `AbstractQCModule`              | `writeDefaultImage` / `writeSpecificImage`     | Generates and saves PNG plots inside the ZIP's `Images/` folder using `ImageIO.write`.                                                        | PNG        | `format_3603` | exact EDAM format match            | High       | Archive content.                                                                              |
| **report icons**               | Output | `.png`                                                             | `HTMLReportArchive.java`                  | `HTMLReportArchive`             | `startDocument`                                | Copies check icons from resources into the ZIP's `Icons/` subdirectory.                                                                       | PNG        | `format_3603` | exact EDAM format match            | High       | Archive content.                                                                              |
| **fastqc.fo**                  | Output | `.fo`                                                              | `HTMLReportArchive.java`                  | `HTMLReportArchive`             | `<init>`                                       | Transforms XHTML to XSL-FO inside the ZIP when template `fastqc2fo.xsl` is available in resources.                                            | XML        | `format_2332` | broader EDAM concept               | High       | Archive content. Mapped to the broader XML concept.                                           |

---

## 2. Verified Input Formats

* **FASTQ** (`.fastq`, `.fq`, `.txt`): Raw nucleotide sequences with base quality scores. Parsed line-by-line using a standard four-line record schema.
* **Gzipped FASTQ** (`.gz` extensions or gzip MIME type): Gzip-wrapped FASTQ sequences decompressed via `MultiMemberGZIPInputStream`.
* **Bzip2 compressed FASTQ** (`.bz2` or `.bz` extensions): Bzip2-wrapped FASTQ sequences decompressed via `BZip2CompressorInputStream`.
* **BAM** (`.bam`): Binary sequence alignment file parsed via HTSJDK `SamReader`.
* **SAM** (`.sam`): Text-based sequence alignment file parsed via HTSJDK `SamReader`.
* **UBAM** (`.ubam`): Unmapped sequence alignment file in BAM format parsed via HTSJDK `SamReader`.
* **FAST5** (`.fast5`): Raw Oxford Nanopore HDF5 signal container parsed via the `cisd-jhdf5` library to locate basecalled FASTQ dataset blocks.
* **csFASTQ / Colorspace** (`.csfastq`): ABI SOLiD color-transition sequence data handled inside the FASTQ parser, with digits translated to standard nucleotides.
* **Standard Input (stdin)**: Piping uncompressed FASTQ sequence data directly from a shell pipe into standard input (`System.in`).

---

## 3. Verified Primary Outputs

* **HTML Report** (`.html`): A standalone, styled document containing diagnostic check summaries, stylesheets, and base64-encoded plot figures written directly to the target directory.
* **ZIP Archive** (`.zip`): A compressed archive container containing diagnostic logs, raw statistics, stylesheets, and individual graphic panels written directly to the target directory.

---

## 4. Archive Contents

The following files exist as contents of the ZIP archive:

* `fastqc_report.html`: A duplicate copy of the main interactive HTML report stored inside the archive.
* `fastqc_data.txt`: Tab-delimited text documenting raw module metrics for downstream parsing.
* `summary.txt`: Tab-delimited status evaluations (PASS/WARN/FAIL) and module metadata.
* `fastqc.fo`: XSL Formatting Objects XML representation of the report formatting layout.
* `Images/` (`.svg` and `.png` plots): Subdirectory containing vector and raster graphic charts generated by each analysis module.
* `Icons/` (`.png` files): Subdirectory containing status check and brand icons.

---

## 5. EDAM Mapping

| FastQC Item           | EDAM Term  | EDAM ID       | Match Type                         |
| --------------------- | ---------- | ------------- | ---------------------------------- |
| **FASTQ**             | FASTQ      | `format_1930` | exact EDAM format match            |
| **BAM**               | BAM        | `format_2572` | exact EDAM format match            |
| **SAM**               | SAM        | `format_2573` | exact EDAM format match            |
| **UBAM**              | BAM        | `format_2572` | broader EDAM concept               |
| **FAST5**             | HDF5       | `format_3590` | broader EDAM concept               |
| **csFASTQ**           | FASTQ      | `format_1930` | related EDAM concept               |
| **stdin**             | N/A        | N/A           | no suitable EDAM format term found |
| **HTML Report**       | HTML       | `format_2331` | exact EDAM format match            |
| **ZIP Archive**       | ZIP format | `format_3987` | exact EDAM format match            |
| **`fastqc_data.txt`** | TSV        | `format_3475` | exact EDAM format match            |
| **`summary.txt`**     | TSV        | `format_3475` | exact EDAM format match            |
| **SVG plots**         | SVG        | `format_3604` | exact EDAM format match            |
| **PNG plots**         | PNG        | `format_3603` | exact EDAM format match            |
| **report icons**      | PNG        | `format_3603` | exact EDAM format match            |
| **`fastqc.fo`**       | XML        | `format_2332` | broader EDAM concept               |

---

## 6. Unsupported / Excluded Formats

### FASTA

**FASTA** (`.fasta` / `.fa`) is explicitly rejected.

FastQC requires base quality scores. Passing a sequence header beginning with `>` causes a `SequenceFormatException` inside `FastQFile` and terminates execution.

### Goby

**Goby** (`.goby`) is unsupported.

Although it appears in GUI-related file filters, there is no Goby parser implementation or corresponding library dependency in the repository. Goby selection therefore falls back to the FASTQ text reader and fails.

### Compact Reads

**Compact Reads** (`.compact-reads`) is unsupported.

The extension appears in GUI chooser filters, but no parser implementation exists. Selection falls back to the standard FASTQ reader and fails.

### `.bz` Compression

**`.bz` compression** is unsupported by the parser.

Although `.bz` may appear in related file filters, `FastQFile` specifically checks for `.bz2`. Files ending in `.bz` therefore fall back to uncompressed plain-text reading and fail.

---

## 7. EDAM Mapping Limitations

* **FAST5 → HDF5 (`format_3590`)** is a broader mapping, not an exact FAST5 EDAM term, because a FAST5-specific EDAM term was not identified.
* **csFASTQ → FASTQ (`format_1930`)** is a related mapping, not an exact csFASTQ term. The ontology includes csFASTA (`format_3589`) but lacks a dedicated colorspace FASTQ term.
* **UBAM → BAM (`format_2572`)** is a broader mapping because there is no separate UBAM EDAM term.
* **stdin** is an input mechanism rather than a data format and therefore has no mapped EDAM format ID.
* **`fastqc.fo` → XML (`format_2332`)** is a broader mapping because no specific XSL-FO EDAM term was identified.
* **`.bz`** is not decompressed by FastQC even though related extensions may appear in GUI filters, leading to parser errors upon selection.

---

## 8. Final Conclusion

FastQC accepts unaligned and aligned sequence datasets, including:

* FASTQ with supported compression schemes
* BAM
* SAM
* UBAM
* FAST5
* csFASTQ
* FASTQ supplied through standard input

It generates:

* a standalone interactive HTML report
* a structured ZIP archive containing additional report data and graphics

The input and output formats were traced to the FastQC source-code implementation. EDAM ontology identifiers were mapped to the identified formats and classified as exact, broader, or related mappings where appropriate.

Unparseable or unimplemented formats, including FASTA, Goby, Compact Reads, and `.bz` compression, were identified and excluded.

---

## 9. Analysis Scope

This document contains the format analysis produced by **Antigravity**, run locally against the FastQC source repository.

The analysis focused on:

1. Source-code-based format detection.
2. Input parser implementation.
3. Compression handling.
4. Output generation.
5. ZIP archive contents.
6. EDAM format classification.
7. Identification of unsupported or incorrectly advertised formats.

The results were generated from inspection of the FastQC Java source code and associated implementation classes.
