# SAMtools Analysis

## Input Formats

### SAM

SAM is a primary alignment input format accepted by SAMtools.

Repository evidence:

- `doc/samtools-view.1` documents SAM as an input format for `samtools view`.
- `sam_view.c` uses the SAMtools/HTSlib alignment-file reading interface.

Biological data type:

Sequence alignment records.

EDAM mapping:

SAM → `format_2573`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### BAM

BAM is a primary binary alignment input format accepted by SAMtools.

Repository evidence:

- `doc/samtools-view.1` documents BAM input.
- `bedcov.c` opens alignment files using `sam_open_format()`.

Biological data type:

Binary sequence alignment records.

EDAM mapping:

BAM → `format_2572`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### CRAM

CRAM is a primary reference-aware compressed alignment input format.

Repository evidence:

- `doc/samtools-view.1` documents CRAM input.
- `bam_plcmd.c` uses `sam_open_format()` and CRAM-specific options.

Biological data type:

Reference-aware sequence alignment records.

EDAM mapping:

CRAM → `format_3462`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### FASTQ

FASTQ is an input format for sequencing reads.

Repository evidence:

- `bam_import.c` implements the `samtools import` command.
- `doc/samtools-import.1` documents FASTQ input.
- Compressed FASTQ input is supported.

Biological data type:

Raw sequencing reads with per-base quality scores.

EDAM mapping:

FASTQ → `format_1930`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### FASTA

FASTA is used as a reference sequence input and for sequence-related operations.

Repository evidence:

- `faidx.c` implements FASTA indexing and sequence retrieval.
- `dict.c` reads FASTA files.
- `doc/samtools-dict.1` documents FASTA input.

Biological data type:

Reference nucleotide sequences.

EDAM mapping:

FASTA → `format_1929`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### BED

BED is used as an additional input for genomic-region based operations.

Repository evidence:

- `bedcov.c` reads BED files containing genomic regions.
- `doc/samtools-bedcov.1` documents BED input.
- BED records are parsed by the command implementation.

Biological data type:

Genomic regions or features.

EDAM mapping:

BED → `format_3003`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

## Supporting Input Formats

### FAI

FAI files are FASTA index files used as supporting files for indexed FASTA access.

Repository evidence:

- `faidx.c` implements FASTA indexing and retrieval.
- SAMtools uses FASTA index files for sequence access.

EDAM mapping:

No verified EDAM identifier was established.

Confidence: Medium.

---

### BAI

BAI is a BAM index format used to support indexed BAM access.

Repository evidence:

- `sam_index_load()` is used for alignment index loading.
- `doc/samtools-index.1` documents BAI indexes.

EDAM mapping:

BAI → `format_3327`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### CSI

CSI is a coordinate-sorted alignment index used as a supporting index.

Repository evidence:

- `doc/samtools-index.1` documents CSI indexes.
- SAMtools source code handles alignment index files through the indexing interfaces.

EDAM mapping:

No verified EDAM identifier was established.

Confidence: Medium.

---

### CRAI

CRAI is an index format associated with CRAM files.

Repository evidence:

- `doc/samtools-index.1` documents CRAI indexes.
- SAMtools source code handles CRAM index loading.

EDAM mapping:

No verified EDAM identifier was established.

Confidence: Medium.

---

## Output Formats

### BAM

BAM is a primary alignment output format.

Repository evidence:

- `doc/samtools-view.1` documents BAM output.
- `doc/samtools-sort.1` documents BAM output.
- `bam_sort.c` implements BAM file generation.

EDAM mapping:

BAM → `format_2572`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### SAM

SAM is a primary text-based alignment output format.

Repository evidence:

- `doc/samtools-view.1` documents SAM output.
- `doc/samtools-sort.1` lists SAM as an output format.
- `sam_view.c` handles SAM output.

EDAM mapping:

SAM → `format_2573`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### CRAM

CRAM is a primary compressed alignment output format.

Repository evidence:

- `doc/samtools-view.1` documents CRAM output.
- `doc/samtools-sort.1` lists CRAM as an output format.
- SAMtools uses HTSlib format handling for CRAM output.

EDAM mapping:

CRAM → `format_3462`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### FASTA

FASTA can be generated by sequence extraction and consensus-related commands.

Repository evidence:

- `doc/samtools-fasta.1` documents FASTA output.
- `doc/samtools-consensus.1` documents FASTA consensus output.
- `bam_fastq.c` implements sequence extraction.

EDAM mapping:

FASTA → `format_1929`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### FASTQ

FASTQ can be generated by sequence extraction and consensus-related commands.

Repository evidence:

- `doc/samtools-fasta.1` documents FASTQ output.
- `doc/samtools-consensus.1` documents FASTQ output.
- `bam_fastq.c` implements FASTQ output.

EDAM mapping:

FASTQ → `format_1930`

Verification:

Programmatically verified against the official EDAM ontology.

Confidence: High.

---

### Pileup

Pileup is a textual output representing positional information derived from alignments.

Repository evidence:

- `doc/samtools-consensus.1` documents pileup-related output.
- `bam_consensus.c` implements pileup generation.

EDAM mapping:

No verified EDAM identifier was established.

Confidence: Medium.

Manual verification is recommended before assigning an EDAM identifier.

---

### Sequence Dictionary

SAMtools can generate sequence dictionary files containing reference sequence metadata.

Repository evidence:

- `doc/samtools-dict.1` documents dictionary generation.
- `dict.c` implements dictionary output.

EDAM mapping:

No verified EDAM identifier was established.

Confidence: Medium.

Manual verification is recommended before assigning an EDAM identifier.

---

## Supporting and Internal Outputs

### BAI, CSI, CRAI and FAI

SAMtools can generate supporting index files associated with BAM, CRAM and FASTA data.

These files should be distinguished from the primary biological formats.

BAI has a verified EDAM mapping:

BAI → `format_3327`

No verified EDAM identifiers were established for CSI, CRAI or FAI.

---

### FQIDX

FQIDX is an auxiliary index associated with FASTQ processing.

Repository evidence:

- `doc/samtools-fqidx.1` documents FASTQ indexing.
- FASTQ indexing functionality is implemented in the repository.

No verified EDAM identifier was established for FQIDX.

The exact role of FQIDX as a supporting format should be manually verified before treating it as a confirmed standalone format.

---

### Temporary BAM Files

Sorting operations can create temporary BAM files during processing.

Repository evidence:

- `doc/samtools-sort.1`
- `bam_sort.c`

These files are internal processing artifacts rather than primary user-facing outputs.

---

## Textual Command Reports

Several SAMtools commands generate textual output, including:

- `stats`;
- `flagstat`;
- `idxstats`;
- `depth`;
- `coverage`;
- `mpileup`;
- `ampliconstats`;
- `checksum`;
- `cram-size`.

These should be treated as textual command outputs rather than automatically assigning them independent biological file-format EDAM identifiers.

Repository evidence:

- corresponding command documentation in `doc/`;
- corresponding source files.

---

## EDAM Verification

The EDAM mappings were verified programmatically against the official EDAM ontology.

The verification parsed the official `EDAM.owl` file and checked the existence and labels of proposed identifiers.

The following mappings were verified successfully:

| Item | EDAM ID | Type |
|---|---|---|
| SAM | `format_2573` | format |
| BAM | `format_2572` | format |
| CRAM | `format_3462` | format |
| FASTQ | `format_1930` | format |
| FASTA | `format_1929` | format |
| BED | `format_3003` | format |
| VCF | `format_3016` | format |
| BCF | `format_3020` | format |
| BAI | `format_3327` | format |
| Sequence alignment | `data_0863` | data type |
| Sequence | `data_2044` | data type |
| Nucleic acid sequence | `data_2977` | data type |
| Annotation track | `data_3002` | data type |

The current verification did not establish EDAM mappings for:

- FAI;
- CRAI;
- CSI;
- FQIDX;
- Pileup;
- Sequence Dictionary.

No EDAM identifiers should be guessed for these items.

---

## Confidence Assessment

The highest-confidence findings are the primary SAMtools input and output formats supported directly by documentation and source code:

- SAM;
- BAM;
- CRAM;
- FASTQ;
- FASTA;
- BED.

BAI is also strongly supported as a supporting index and has a verified EDAM mapping.

Supporting indexes such as FAI, CSI and CRAI should remain distinct from primary biological formats.

FQIDX requires additional manual verification concerning its exact role.

Temporary BAM files are internal processing artifacts and should not be treated as independent primary outputs.

Textual reports such as `stats`, `flagstat` and `depth` are command outputs rather than distinct biological file formats.

Pileup and Sequence Dictionary should not receive guessed EDAM identifiers because the current programmatic verification did not establish a valid mapping.

---

## Manual Verification Requirements

Manual verification is recommended for:

- the exact role of FQIDX as a supporting format;
- the distinction between primary and supporting outputs for individual SAMtools subcommands;
- the EDAM classification of Pileup;
- the EDAM classification of Sequence Dictionary;
- any format for which the current ontology verification returned no matching EDAM term.

---

## Final Conclusion

SAMtools supports several standard bioinformatics alignment and sequence formats.

The main input formats identified from repository evidence are SAM, BAM, CRAM, FASTQ, FASTA and BED. Supporting index files include FAI, BAI, CSI and CRAI.

The main output formats identified are BAM, SAM, CRAM, FASTA, FASTQ, Pileup and Sequence Dictionary. Supporting and internal outputs include alignment indexes, FASTQ indexes and temporary BAM files.

The EDAM verification confirms mappings for the principal standard formats and the BAI index. Items without verified mappings are intentionally left unmapped rather than being assigned guessed EDAM identifiers.

The analysis distinguishes between primary biological formats, supporting indexes, internal processing artifacts and textual command reports. This distinction is important when interpreting SAMtools outputs across its many subcommands.

The coding-agent findings should therefore be considered reliable where explicit repository evidence and programmatic EDAM verification are available, while the identified manual-verification items should not be accepted without further review.
