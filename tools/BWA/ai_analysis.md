# BWA AI Analysis

## Prompt 1 - Identify input formats

**Repository analyzed:** https://github.com/lh3/bwa

The coding agent was asked to analyze the BWA repository and identify all file formats accepted as input, providing repository-based evidence for each format.

## Raw AI Result

The coding agent identified the following candidate input formats:

```json
{
  "repository": "lh3/bwa",
  "analysis_date": "2026-08-17",
  "input_formats": [
    {
      "format_name": "FASTQ",
      "file_extensions": [".fq", ".fastq", ".fq.gz", ".fastq.gz"],
      "data_type": "DNA sequence reads with quality scores",
      "primary_or_additional": "PRIMARY",
      "use_case": "Most common input format for mapping short to long reads",
      "evidence": [
        {
          "source_file": "bwa.1",
          "location": "Lines 9-11, 269",
          "evidence_text": "bwa mem ref.fa reads.fq > aln-se.sam; bwa mem ref.fa read1.fq read2.fq > aln-pe.sam; Usage: bwa mem [options] <idxbase> <in1.fq> [in2.fq]"
        },
        {
          "source_file": "fastmap.c",
          "location": "Line 432",
          "evidence_text": "Usage: bwa fastmap [options] <idxbase> <in.fq>"
        },
        {
          "source_file": "bwakit/run-bwamem",
          "location": "Line 87",
          "evidence_text": "Recognizes fastq/fq and their compressed variants."
        },
        {
          "source_file": "README.md",
          "location": "Lines 21-22, 96-118",
          "evidence_text": "./bwa mem ref.fa read-se.fq.gz | gzip -3 > aln-se.sam.gz"
        }
      ]
    },
    {
      "format_name": "FASTA",
      "file_extensions": [".fa", ".fasta", ".fa.gz", ".fasta.gz"],
      "data_type": "DNA sequence data without quality scores",
      "primary_or_additional": "PRIMARY",
      "use_case": "Reference genome sequences and assembly contigs",
      "evidence": [
        {
          "source_file": "bwa.1",
          "location": "Line 52",
          "evidence_text": "Index database sequences in the FASTA format."
        },
        {
          "source_file": "README.md",
          "location": "Line 20",
          "evidence_text": "./bwa index ref.fa"
        }
      ]
    },
    {
      "format_name": "SAI",
      "file_extensions": [".sai"],
      "data_type": "BWA alignment index",
      "primary_or_additional": "ADDITIONAL",
      "use_case": "Intermediate format in the BWA-backtrack aln/samse/sampe workflow",
      "evidence": [
        {
          "source_file": "bwa.1",
          "location": "Lines 13-17, 501, 521",
          "evidence_text": "bwa aln ref.fa short_read.fq > aln_sa.sai; bwa samse ref.fa aln_sa.sai short_read.fq > aln-se.sam"
        },
        {
          "source_file": "README.md",
          "location": "Lines 103-112",
          "evidence_text": "bwa aln ref.fa reads.fq > reads.sai; bwa samse ref.fa reads.sai reads.fq > aln-se.sam"
        }
      ]
    },
    {
      "format_name": "BAM",
      "file_extensions": [".bam"],
      "data_type": "Binary sequence/alignment data",
      "primary_or_additional": "PRIMARY",
      "use_case": "Input read sequence file for bwa aln using the -b option",
      "evidence": [
        {
          "source_file": "bwa.1",
          "location": "Lines 468-479",
          "evidence_text": "-b Specify the input read sequence file is the BAM format."
        },
        {
          "source_file": "ChangeLog",
          "location": "r1541",
          "evidence_text": "preliminary BAM input support"
        }
      ]
    },
    {
      "format_name": "SAM",
      "file_extensions": [".sam", ".sam.gz"],
      "data_type": "Text-based sequence alignment data",
      "primary_or_additional": "ADDITIONAL",
      "use_case": "Recognized by the bwakit run-bwamem auxiliary script",
      "evidence": [
        {
          "source_file": "bwakit/run-bwamem",
          "location": "Line 56",
          "evidence_text": "Recognizes input files with .bam, .sam and .sam.gz extensions."
        }
      ]
    },
    {
      "format_name": "BWA Index Files",
      "file_extensions": [".bwt", ".pac", ".sa", ".ann", ".amb"],
      "data_type": "Reference index data",
      "primary_or_additional": "PRIMARY",
      "use_case": "Reference index required by BWA alignment operations",
      "evidence": [
        {
          "source_file": "bwa.c",
          "location": "Lines 245-268",
          "evidence_text": "Checks for .bwt and related BWA index files."
        },
        {
          "source_file": "bwakit/run-bwamem",
          "location": "Lines 51-52",
          "evidence_text": "Checks for .bwt, .pac, .sa, .ann and .amb index files."
        },
        {
          "source_file": "README.md",
          "location": "Line 20",
          "evidence_text": "./bwa index ref.fa"
        }
      ]
    },
    {
      "format_name": "ALT Contigs Index File",
      "file_extensions": [".alt"],
      "data_type": "ALT contig mapping information",
      "primary_or_additional": "ADDITIONAL",
      "use_case": "Optional ALT-aware mapping",
      "evidence": [
        {
          "source_file": "bwa.1",
          "location": "Lines 331-334",
          "evidence_text": "-j Treat ALT contigs as part of the primary assembly."
        },
        {
          "source_file": "README.md",
          "location": "Lines 152-159",
          "evidence_text": "BWA-MEM supports mapping to GRCh38+ALT."
        }
      ]
    },
    {
      "format_name": "Interleaved FASTQ",
      "file_extensions": [".fq", ".fastq", ".fq.gz", ".fastq.gz"],
      "data_type": "Paired-end reads stored in an interleaved FASTQ stream",
      "primary_or_additional": "PRIMARY",
      "use_case": "Paired-end mapping using the -p option",
      "evidence": [
        {
          "source_file": "bwa.1",
          "location": "Lines 141-152",
          "evidence_text": "If -p is used, the command assumes adjacent reads constitute a read pair."
        },
        {
          "source_file": "NEWS.md",
          "location": "Lines 539-541",
          "evidence_text": "BWA-MEM optionally takes one interleaved FASTQ for paired-end mapping."
        }
      ]
    },
    {
      "format_name": "Illumina 1.3+ FASTQ",
      "file_extensions": [".fq", ".fastq"],
      "data_type": "FASTQ reads using legacy Illumina quality encoding",
      "primary_or_additional": "PRIMARY",
      "use_case": "Mapping legacy Illumina reads using the -I option",
      "evidence": [
        {
          "source_file": "bwa.1",
          "location": "Lines 457-458",
          "evidence_text": "-I The input is in the Illumina 1.3+ read format (quality equals ASCII-64)."
        },
        {
          "source_file": "NEWS.md",
          "location": "Line 693",
          "evidence_text": "Feature: Illumina 1.3+ read format support via the '-I' option."
        }
      ]
    },
    {
      "format_name": "MAG",
      "file_extensions": [".mag", ".mag.gz"],
      "data_type": "Sequence/assembly-related data",
      "primary_or_additional": "ADDITIONAL",
      "use_case": "Recognized by the bwakit auxiliary scripts",
      "evidence": [
        {
          "source_file": "bwakit/run-bwamem",
          "location": "Line 87",
          "evidence_text": "Recognizes .mag and .mag.gz extensions."
        }
      ]
    }
  ]
}
```

## Agent Notes

The coding agent additionally reported the following observations:

* BWA index files (`.bwt`, `.pac`, `.sa`, `.ann`, `.amb`) are generated from a reference FASTA using `bwa index` and are required for alignment operations.
* FASTQ input may be gzip-compressed.
* BAM input is supported by `bwa aln -b`.
* Interleaved FASTQ is supported by BWA-MEM using the `-p` option.
* Illumina 1.3+ represents a legacy FASTQ quality encoding.
* SAI is used as an intermediate format in the BWA-backtrack workflow.
* The agent identified SAM and MAG based primarily on auxiliary `bwakit` scripts.

## Preliminary Assessment

This is the raw coding-agent result and has not yet been fully validated.

Some entries represent variants or usage modes of existing formats rather than distinct file formats. In particular:

* Interleaved FASTQ is a usage mode of FASTQ.
* Illumina 1.3+ is a FASTQ encoding variant.
* BWA index files are reference index files rather than biological sequence formats.
* SAM and MAG require additional verification because the evidence comes from auxiliary `bwakit` scripts rather than the core BWA commands.

The verified classification will be documented separately after repository-based verification.
## Prompt 2 - Identify output formats

**Repository analyzed:** https://github.com/lh3/bwa

The coding agent was asked to analyze the BWA repository and identify all file formats produced as output, including primary, intermediate, reference index, and auxiliary outputs, with repository-based evidence.

## Raw AI Result

The coding agent identified the following candidate output formats:

```json
{
  "repository": "lh3/bwa",
  "analysis_date": "2026-08-18",
  "output_formats": [
    {
      "format_name": "SAM (Sequence Alignment/Map)",
      "file_extensions": [".sam"],
      "data_type": "Text-based sequence alignment records",
      "description": "Human-readable text format containing aligned sequence reads with reference positions, quality scores, and optional tags. Default output format for alignment commands.",
      "bwa_commands_that_produce": [
        "bwa mem",
        "bwa aln (via samse/sampe)",
        "bwa samse",
        "bwa sampe",
        "bwa bwasw"
      ],
      "primary_or_additional": "PRIMARY",
      "evidence": [
        {
          "source_file": "fastmap.c",
          "location": "Line 299",
          "evidence_text": "-o FILE       sam file to output results to [stdout]"
        },
        {
          "source_file": "bwa.1",
          "location": "Lines 9-19",
          "evidence_text": "bwa mem ref.fa reads.fq > aln-se.sam; bwa mem ref.fa read1.fq read2.fq > aln-pe.sam; bwa samse ref.fa aln_sa.sai short_read.fq > aln-se.sam; bwa sampe ref.fa aln_sa1.sai aln_sa2.sai read1.fq read2.fq > aln-pe.sam; bwa bwasw ref.fa long_read.fq > aln.sam"
        },
        {
          "source_file": "bwamem.c",
          "location": "Lines 851-976",
          "evidence_text": "mem_aln2sam() generates SAM records containing QNAME, FLAG, RNAME, POS, MAPQ, CIGAR, RNEXT, PNEXT, TLEN, SEQ, QUAL and optional tags."
        },
        {
          "source_file": "README.md",
          "location": "Lines 21-22",
          "evidence_text": "./bwa mem ref.fa read-se.fq.gz | gzip -3 > aln-se.sam.gz"
        }
      ]
    },
    {
      "format_name": "SAI (BWA Alignment Index)",
      "file_extensions": [".sai"],
      "data_type": "Binary alignment intermediate data",
      "description": "Intermediate format produced by the BWA-backtrack aln command and consumed by samse or sampe.",
      "bwa_commands_that_produce": [
        "bwa aln"
      ],
      "primary_or_additional": "INTERMEDIATE",
      "evidence": [
        {
          "source_file": "bwa.1",
          "location": "Lines 13, 380-385",
          "evidence_text": "bwa aln ref.fa short_read.fq > aln_sa.sai; bwa aln [...] <in.db.fasta> <in.query.fq> > <out.sai>"
        },
        {
          "source_file": "README.md",
          "location": "Lines 103-112",
          "evidence_text": "bwa aln ref.fa reads.fq > reads.sai; bwa samse ref.fa reads.sai reads.fq > aln-se.sam"
        }
      ]
    },
    {
      "format_name": "BWA Index Files",
      "file_extensions": [".pac", ".bwt", ".sa", ".ann", ".amb"],
      "data_type": "Binary reference index data",
      "description": "Reference index files generated by bwa index and used by BWA alignment commands.",
      "bwa_commands_that_produce": [
        "bwa index"
      ],
      "primary_or_additional": "REFERENCE_INDEX",
      "evidence": [
        {
          "source_file": "bwtindex.c",
          "location": "Relevant index-generation sections",
          "evidence_text": "The bwa index implementation generates .pac, .bwt and .sa files and the associated reference annotation/index files."
        },
        {
          "source_file": "bwakit/run-bwamem",
          "location": "Lines 51-52",
          "evidence_text": "Checks for .bwt, .pac, .sa, .ann and .amb index files."
        }
      ]
    },
    {
      "format_name": "BAM (Binary Alignment/Map)",
      "file_extensions": [".bam"],
      "data_type": "Binary alignment data",
      "description": "BAM output generated by the auxiliary bwakit pipeline rather than directly by core BWA commands.",
      "bwa_commands_that_produce": [
        "bwakit run-bwamem (using external tools)"
      ],
      "primary_or_additional": "AUXILIARY",
      "evidence": [
        {
          "source_file": "bwakit/README.md",
          "location": "Lines 30-35",
          "evidence_text": "The mapping command generates out.aln.bam."
        },
        {
          "source_file": "README-alt.md",
          "location": "Line 7",
          "evidence_text": "This generates out.aln.bam as the final alignment."
        }
      ]
    },
    {
      "format_name": "HLA Genotype Results",
      "file_extensions": [".hla.top", ".hla.all"],
      "data_type": "Text-based HLA typing results",
      "description": "Auxiliary HLA genotype prediction files produced by bwakit when HLA typing is requested.",
      "bwa_commands_that_produce": [
        "bwakit run-bwamem with -H"
      ],
      "primary_or_additional": "AUXILIARY",
      "evidence": [
        {
          "source_file": "bwakit/README.md",
          "location": "Lines 37-39",
          "evidence_text": "out.hla.top contains the best genotypes and out.hla.all contains other possible genotypes."
        },
        {
          "source_file": "README-alt.md",
          "location": "Line 8",
          "evidence_text": "out.hla.top and out.hla.all are generated by the pipeline."
        }
      ]
    },
    {
      "format_name": "Log Files",
      "file_extensions": [".log.*"],
      "data_type": "Text-based diagnostic and status information",
      "description": "Auxiliary log files produced by bwakit and associated pipeline tools.",
      "bwa_commands_that_produce": [
        "bwakit run-bwamem"
      ],
      "primary_or_additional": "AUXILIARY",
      "evidence": [
        {
          "source_file": "bwakit/README.md",
          "location": "Lines 40-42",
          "evidence_text": "out.log.* contains bwa-mem, samblaster and HLA typing log files."
        }
      ]
    }
  ]
}
```

## Agent Notes

The coding agent additionally reported:

* Core BWA alignment commands produce SAM records, normally written to standard output.
* `bwa aln` produces SAI intermediate output.
* `bwa index` produces the BWA reference index files.
* BAM output is produced by the auxiliary `bwakit` pipeline using external tools rather than directly by the core BWA commands.
* HLA genotype files are generated only by `bwakit` when HLA typing is requested.
* Log files are auxiliary outputs of the `bwakit` pipeline.
* Gzip-compressed SAM is created by piping BWA output through `gzip`; it is not directly generated by BWA.
* Diagnostic messages written to `stderr` are informational output rather than a biological file format.

## Preliminary Assessment

This is the raw coding-agent result and has not yet been fully validated.

Several outputs require careful classification:

* SAM is the main biological output of the core alignment commands.
* SAI is an intermediate BWA-specific output.
* `.pac`, `.bwt`, `.sa`, `.ann`, and `.amb` are reference index files generated by `bwa index`.
* BAM is produced by `bwakit` with external tools and should not be presented as a direct core BWA output.
* HLA genotype files and log files belong to the auxiliary `bwakit` pipeline.
* Gzip-compressed SAM is a compressed form of SAM, not a separate biological format.
* `stderr` diagnostic messages should not normally be treated as a file format.

The final verified classification will be documented separately after repository-based verification.

