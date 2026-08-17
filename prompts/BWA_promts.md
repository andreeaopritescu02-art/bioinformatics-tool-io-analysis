# BWA - Coding Agent Prompts

These prompts are designed to evaluate whether coding agents can identify input and output formats of a bioinformatics tool, provide repository-based evidence, verify EDAM ontology mappings, and return the results in a structured format.

The prompts should be used, as far as possible, with different AI coding agents and AI models to allow comparison of their results.

---

## Prompt 1 - Identify input formats

Analyze the BWA GitHub repository:

https://github.com/lh3/bwa

Identify all file formats that BWA accepts as input.

For each input format, provide:

* format name
* file extensions, if applicable
* data type/content
* whether it is a primary or additional input
* the specific repository file(s), source code, documentation, or command-line parsing logic that provides evidence for this format

Do not rely only on general knowledge about BWA. Use evidence from the repository.

Return the results as structured JSON.

---

## Prompt 2 - Identify output formats

Analyze the BWA GitHub repository:

https://github.com/lh3/bwa

Identify all file formats that BWA produces as output.

For each output format, provide:

* format name
* file extensions, if applicable
* data type/content
* the BWA command or functionality that produces it
* the specific repository file(s), source code, documentation, or output-writing logic that provides evidence for this format

Distinguish between the main output formats and auxiliary/log/statistical outputs.

Do not infer a format only because it is commonly associated with BWA. Provide repository-based evidence.

Return the results as structured JSON.

---

## Prompt 3 - Map formats to EDAM ontology

Using the input and output formats identified from the BWA repository, map each format to the corresponding EDAM ontology format term.

For each format, provide:

* format name
* EDAM term name
* EDAM identifier
* whether the mapping is exact, close, or uncertain
* a short explanation of why the EDAM term matches the format

Verify the EDAM identifiers against the official EDAM ontology rather than relying solely on the coding agent's prior knowledge.

If no suitable EDAM term exists, explicitly state this instead of inventing an identifier.

Return the results as structured JSON.

---

## Prompt 4 - Produce a final verified BWA I/O report

Using the previous analysis, produce a final verified report of BWA's input and output formats.

For every format:

* classify it as input or output
* give the format name
* give extensions, if applicable
* describe the data represented
* identify the BWA command/functionality involved
* provide repository-based evidence, including file paths and relevant code/documentation references
* provide the EDAM term and identifier
* indicate whether the EDAM mapping is exact, close, or uncertain

Separate:

1. Primary input formats
2. Additional/optional input formats
3. Primary output formats
4. Auxiliary outputs

Do not include formats that are only speculative or unsupported by repository evidence.

Where the repository evidence and EDAM ontology disagree with an earlier AI-generated result, prioritize the verified repository and official EDAM evidence.

Return the final result as structured JSON.
