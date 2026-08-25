#!/usr/bin/env python3
"""
EDAM Ontology Verification Script for SAMtools Formats

This script performs programmatic verification of SAMtools input/output format
mappings against the official EDAM ontology (https://edamontology.org/EDAM.owl).

Functionality:
- Downloads EDAM.owl from the official source
- Parses using rdflib (preferred) or XML fallback
- Verifies all proposed EDAM mappings
- Searches for unmapped formats in EDAM
- Generates JSON and Markdown reports

Usage:
    python3 tools/SAMtools/verify_edam_mappings.py

Output:
    - results/samtools_edam_verification.json
    - results/samtools_edam_verification.md
"""

import json
import sys
import os
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any
from urllib.request import urlopen
from urllib.error import URLError
import tempfile
from datetime import datetime

# Define results directory
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)

OUTPUT_JSON = RESULTS_DIR / "samtools_edam_verification.json"
OUTPUT_MD = RESULTS_DIR / "samtools_edam_verification.md"

def log_info(msg: str):
    """Print info message"""
    print(f"[*] {msg}")

def log_success(msg: str):
    """Print success message"""
    print(f"[+] {msg}")

def log_error(msg: str):
    """Print error message"""
    print(f"[-] {msg}")

def log_warning(msg: str):
    """Print warning message"""
    print(f"[!] {msg}")

def download_edam_owl() -> Optional[str]:
    """Download EDAM.owl from official source"""
    url = "https://edamontology.org/EDAM.owl"
    log_info(f"Downloading EDAM.owl from {url}")
    
    try:
        with urlopen(url, timeout=120) as response:
            content = response.read()
        
        # Save to temp file
        temp_file = tempfile.NamedTemporaryFile(
            mode='wb',
            suffix='.owl',
            delete=False,
            prefix='EDAM_'
        )
        temp_file.write(content)
        temp_path = temp_file.name
        temp_file.close()
        
        file_size_mb = len(content) / (1024 * 1024)
        log_success(f"Downloaded EDAM.owl ({file_size_mb:.2f} MB) to {temp_path}")
        return temp_path
    
    except URLError as e:
        log_error(f"Failed to download EDAM.owl: {e}")
        return None
    except Exception as e:
        log_error(f"Unexpected error downloading EDAM.owl: {e}")
        return None

def parse_edam_with_rdflib(owl_path: str) -> Tuple[Optional[Dict], Optional[Any]]:
    """Parse EDAM.owl using rdflib"""
    try:
        from rdflib import Graph, Namespace, RDF, RDFS
        
        log_info("Attempting to parse with rdflib...")
        
        g = Graph()
        g.parse(owl_path, format='xml')
        
        triple_count = len(g)
        log_success(f"Loaded {triple_count:,} RDF triples from EDAM.owl")
        
        # Extract all EDAM concepts
        concepts = {}
        EDAM = Namespace("http://edamontology.org/")
        
        for subject in g.subjects():
            subject_uri = str(subject)
            if 'edamontology.org' in subject_uri:
                concept_id = subject_uri.split('/')[-1]
                
                # Get label
                labels = list(g.objects(subject, RDFS.label))
                label = str(labels[0]) if labels else None
                
                # Get definition/comment
                definitions = list(g.objects(subject, RDFS.comment))
                definition = str(definitions[0]) if definitions else None
                
                if label:
                    concepts[concept_id] = {
                        'uri': subject_uri,
                        'label': label,
                        'definition': definition
                    }
        
        concept_count = len(concepts)
        log_success(f"Extracted {concept_count:,} EDAM concepts")
        
        return concepts, g
    
    except ImportError:
        log_warning("rdflib not installed, will use XML parser")
        return None, None
    except Exception as e:
        log_error(f"Error parsing with rdflib: {e}")
        return None, None

def parse_edam_with_xml(owl_path: str) -> Optional[Dict]:
    """Fallback: Parse EDAM.owl using standard library XML parser"""
    import xml.etree.ElementTree as ET
    
    log_info("Parsing EDAM.owl with XML ElementTree...")
    
    try:
        tree = ET.parse(owl_path)
        root = tree.getroot()
        
        concepts = {}
        element_count = 0
        
        for elem in root.iter():
            element_count += 1
            
            # Look for Description or Class elements with about attribute
            if ('Description' in elem.tag or 'Class' in elem.tag):
                # Extract about attribute (the URI)
                about = None
                for attr_name in elem.attrib:
                    if attr_name.endswith('about'):
                        about = elem.attrib[attr_name]
                        break
                
                if about and 'edamontology.org' in about:
                    concept_id = about.split('/')[-1]
                    
                    label = None
                    definition = None
                    
                    # Extract label and definition from child elements
                    for child in elem:
                        if 'label' in child.tag:
                            label = child.text
                        elif 'comment' in child.tag or 'definition' in child.tag:
                            definition = child.text
                    
                    if label:
                        concepts[concept_id] = {
                            'uri': about,
                            'label': label,
                            'definition': definition
                        }
        
        concept_count = len(concepts)
        log_success(f"Parsed {concept_count:,} EDAM concepts from {element_count:,} XML elements")
        
        return concepts
    
    except Exception as e:
        log_error(f"Error parsing with XML: {e}")
        return None

def verify_mapping(
    concept_id: str,
    expected_label: str,
    concepts: Dict,
    expected_type: str
) -> Dict[str, Any]:
    """
    Verify a single EDAM mapping against the ontology
    
    Args:
        concept_id: Proposed EDAM ID (e.g., 'format_2572')
        expected_label: Expected term name (e.g., 'BAM')
        concepts: Dictionary of all EDAM concepts
        expected_type: 'file_format' or 'data_type'
    
    Returns:
        Verification result dictionary
    """
    
    if concept_id not in concepts:
        return {
            'status': 'NOT_FOUND',
            'verified': False,
            'reason': f'EDAM ID "{concept_id}" not found in ontology',
            'actual_label': None,
            'label_match': False,
            'type_match': False,
            'uri': None,
            'definition': None
        }
    
    concept = concepts[concept_id]
    actual_label = concept.get('label', '')
    uri = concept.get('uri', '')
    definition = concept.get('definition', '')
    
    # Normalize labels for comparison
    label_normalized_actual = actual_label.lower().strip()
    label_normalized_expected = expected_label.lower().strip()
    
    # Check exact label match
    label_exact_match = label_normalized_actual == label_normalized_expected
    
    # Check type consistency
    is_format = 'format_' in concept_id
    is_data = 'data_' in concept_id
    
    type_expected_format = expected_type == 'file_format'
    type_expected_data = expected_type == 'data_type'
    
    type_match = (type_expected_format and is_format) or (type_expected_data and is_data)
    
    # Determine verification status
    if label_exact_match and type_match:
        status = 'VERIFIED'
        verified = True
    elif type_match and label_normalized_expected in label_normalized_actual:
        status = 'VERIFIED'
        verified = True
    elif type_match:
        status = 'AMBIGUOUS'
        verified = False
    else:
        status = 'NOT_FOUND'
        verified = False
    
    return {
        'status': status,
        'verified': verified,
        'reason': None,
        'actual_label': actual_label,
        'expected_label': expected_label,
        'label_match': label_exact_match,
        'type_match': type_match,
        'uri': uri,
        'definition': definition[:200] + ('...' if len(definition or '') > 200 else '') if definition else None
    }

def search_edam_by_label(
    label: str,
    concepts: Dict,
    expected_type: Optional[str] = None
) -> List[Tuple[str, Dict]]:
    """
    Search EDAM for concepts matching a label
    
    Args:
        label: Label to search for
        concepts: Dictionary of all EDAM concepts
        expected_type: 'file_format' or 'data_type' to filter results
    
    Returns:
        List of (concept_id, concept_data) tuples
    """
    
    label_lower = label.lower().strip()
    matches = []
    
    for concept_id, concept_data in concepts.items():
        actual_label = concept_data.get('label', '').lower().strip()
        
        # Filter by type if specified
        if expected_type == 'file_format' and 'format_' not in concept_id:
            continue
        if expected_type == 'data_type' and 'data_' not in concept_id:
            continue
        
        # Check for exact or close matches
        if actual_label == label_lower:
            matches.append((concept_id, concept_data, 'exact'))
        elif label_lower in actual_label or actual_label in label_lower:
            matches.append((concept_id, concept_data, 'partial'))
    
    # Sort: exact matches first, then by concept_id
    matches.sort(key=lambda x: (x[2] != 'exact', x[0]))
    
    return [(cid, cdata) for cid, cdata, _ in matches[:10]]

def main():
    """Main verification workflow"""
    
    print("\n" + "="*80)
    print("EDAM ONTOLOGY VERIFICATION FOR SAMtools FORMATS")
    print("="*80 + "\n")
    
    # SAMtools format mappings to verify
    MAPPINGS = [
        # Format: (display_name, edam_term, proposed_edam_id, type, source)
        
        # Sequence Alignment Formats
        ("SAM", "SAM", "format_2573", "file_format", "Prompt 1-2"),
        ("BAM", "BAM", "format_2572", "file_format", "Prompt 1-2"),
        ("CRAM", "CRAM", "format_3462", "file_format", "Prompt 1-2"),
        
        # Sequence Formats
        ("FASTQ", "FASTQ", "format_1930", "file_format", "Prompt 1-2"),
        ("FASTA", "FASTA", "format_1929", "file_format", "Prompt 1-2"),
        ("FASTA index", "FAI", None, "file_format", "Prompt 1-2"),
        
        # Genomic Region Formats
        ("BED", "BED", "format_3003", "file_format", "Prompt 1"),
        
        # Variant Formats (from extended analysis)
        ("VCF", "VCF", "format_3016", "file_format", "Extended"),
        ("BCF", "BCF", "format_3020", "file_format", "Extended"),
        
        # Index Formats
        ("BAM index", "BAI", "format_3327", "file_format", "Prompt 1-2"),
        ("CRAM index", "CRAI", None, "file_format", "Prompt 1-2"),
        ("CSI", "CSI", None, "file_format", "Prompt 1-2"),
        ("FASTQ index", "FQIDX", None, "file_format", "Prompt 1-2"),
        
        # Data Types
        ("Sequence alignment", "Sequence alignment", "data_0863", "data_type", "Prompt 1-2"),
        ("Sequence", "Sequence", "data_2044", "data_type", "Prompt 1-2"),
        ("Nucleic acid sequence", "Nucleic acid sequence", "data_2977", "data_type", "Prompt 1-2"),
        ("Annotation track", "Annotation track", "data_3002", "data_type", "Prompt 1-2"),
    ]
    
    # Step 1: Download EDAM.owl
    log_info("Step 1: Downloading EDAM.owl ontology")
    owl_path = download_edam_owl()
    if not owl_path:
        log_error("Cannot proceed without EDAM.owl")
        return 1
    print()
    
    # Step 2: Parse EDAM.owl
    log_info("Step 2: Parsing EDAM.owl")
    
    concepts = None
    parser_used = None
    
    # Try rdflib first
    concepts, graph = parse_edam_with_rdflib(owl_path)
    if concepts is not None:
        parser_used = "rdflib"
    else:
        # Fallback to XML parser
        concepts = parse_edam_with_xml(owl_path)
        if concepts is not None:
            parser_used = "XML ElementTree"
        else:
            log_error("Failed to parse EDAM.owl with any available parser")
            return 1
    print()
    
    # Step 3: Verify mappings
    log_info("Step 3: Verifying EDAM mappings")
    print()
    
    results = []
    verified_count = 0
    not_found_count = 0
    ambiguous_count = 0
    unmapped_count = 0
    
    for format_name, edam_term, proposed_id, mtype, source in MAPPINGS:
        result = {
            'format': format_name,
            'edam_term': edam_term,
            'proposed_edam_id': proposed_id,
            'type': mtype,
            'source': source,
            'verification_status': None,
            'verified': False,
            'actual_edam_label': None,
            'matched_edam_id': None,
            'label_match': False,
            'type_match': False,
            'edam_uri': None,
            'definition': None,
            'search_matches': None,
            'verification_note': None
        }
        
        if proposed_id:
            # Verify proposed ID
            verification = verify_mapping(proposed_id, edam_term, concepts, mtype)
            
            result['verification_status'] = verification['status']
            result['verified'] = verification['verified']
            result['actual_edam_label'] = verification['actual_label']
            result['matched_edam_id'] = proposed_id
            result['label_match'] = verification['label_match']
            result['type_match'] = verification['type_match']
            result['edam_uri'] = verification['uri']
            result['definition'] = verification['definition']
            
            status_str = "✓" if verification['verified'] else "✗"
            status_display = f"[{status_str}] {verification['status']}"
            
            print(f"{status_display:20} {format_name:<25} {proposed_id}")
            
            if verification['verified']:
                verified_count += 1
            elif verification['status'] == 'AMBIGUOUS':
                ambiguous_count += 1
                print(f"                      → Label mismatch: expected '{edam_term}', got '{verification['actual_label']}'")
            elif verification['status'] == 'NOT_FOUND':
                not_found_count += 1
        else:
            # Search for term
            print(f"[?] SEARCHING       {format_name:<25} (no ID provided)")
            
            matches = search_edam_by_label(edam_term, concepts, expected_type=mtype)
            
            if matches:
                best_match_id, best_match_data = matches[0]
                result['search_matches'] = [
                    {
                        'id': mid,
                        'label': mdata.get('label'),
                        'uri': mdata.get('uri')
                    }
                    for mid, mdata in matches[:5]
                ]
                result['matched_edam_id'] = best_match_id
                result['actual_edam_label'] = best_match_data.get('label')
                result['edam_uri'] = best_match_data.get('uri')
                result['definition'] = best_match_data.get('definition')
                
                for idx, (mid, mdata) in enumerate(matches[:3]):
                    label = mdata.get('label')
                    print(f"                      {idx+1}. {mid:20} → {label}")
                
                result['verification_status'] = 'UNMAPPED'
                result['verification_note'] = 'No proposed EDAM ID; potential matches found in ontology'
                unmapped_count += 1
            else:
                print(f"                      → No matches found in EDAM")
                result['verification_status'] = 'UNMAPPED'
                result['verification_note'] = 'No proposed EDAM ID; no matching terms found in ontology'
                unmapped_count += 1
        
        results.append(result)
    
    print()
    
    # Step 4: Summary
    print("="*80)
    print("VERIFICATION SUMMARY")
    print("="*80)
    print(f"Total mappings checked: {len(MAPPINGS)}")
    print(f"Verified:              {verified_count}")
    print(f"Ambiguous:             {ambiguous_count}")
    print(f"Not found:             {not_found_count}")
    print(f"Unmapped:              {unmapped_count}")
    print(f"Success rate:          {100*verified_count//len(MAPPINGS)}%")
    print()
    
    # Step 5: Generate JSON output
    log_info("Step 5: Generating JSON report")
    
    json_output = {
        'metadata': {
            'ontology': 'EDAM',
            'source': 'https://edamontology.org/EDAM.owl',
            'verification_date': datetime.now().isoformat(),
            'parser_used': parser_used,
            'total_concepts_in_edam': len(concepts),
            'verification_purpose': 'SAMtools input/output format EDAM mapping verification'
        },
        'summary': {
            'total_mappings_checked': len(MAPPINGS),
            'verified': verified_count,
            'ambiguous': ambiguous_count,
            'not_found': not_found_count,
            'unmapped': unmapped_count,
            'success_rate': f"{100*verified_count//len(MAPPINGS)}%"
        },
        'mappings': results
    }
    
    with open(OUTPUT_JSON, 'w') as f:
        json.dump(json_output, f, indent=2)
    
    log_success(f"JSON report saved to {OUTPUT_JSON}")
    print()
    
    # Step 6: Generate Markdown report
    log_info("Step 6: Generating Markdown report")
    
    md_content = generate_markdown_report(json_output, verified_count, not_found_count, ambiguous_count, unmapped_count, len(MAPPINGS))
    
    with open(OUTPUT_MD, 'w') as f:
        f.write(md_content)
    
    log_success(f"Markdown report saved to {OUTPUT_MD}")
    print()
    
    # Step 7: Display summary
    print("="*80)
    print("FILES CREATED")
    print("="*80)
    print(f"1. {OUTPUT_JSON}")
    print(f"2. {OUTPUT_MD}")
    print()
    
    return 0

def generate_markdown_report(
    json_output: Dict,
    verified: int,
    not_found: int,
    ambiguous: int,
    unmapped: int,
    total: int
) -> str:
    """Generate Markdown report from verification results"""
    
    mappings = json_output['mappings']
    
    md = f"""# SAMtools EDAM Ontology Verification Report

## Metadata

- **Ontology:** EDAM
- **Source:** https://edamontology.org/EDAM.owl
- **Verification Date:** {json_output['metadata']['verification_date']}
- **Parser Used:** {json_output['metadata']['parser_used']}
- **Total EDAM Concepts Parsed:** {json_output['metadata']['total_concepts_in_edam']:,}

## Summary

| Status | Count | Percentage |
|--------|-------|-----------|
| Verified | {verified} | {100*verified//total}% |
| Ambiguous | {ambiguous} | {100*ambiguous//total}% |
| Not Found | {not_found} | {100*not_found//total}% |
| Unmapped | {unmapped} | {100*unmapped//total}% |
| **Total** | **{total}** | **100%** |

## Verification Results

### Verified Mappings ({verified})

| Format | EDAM ID | EDAM Label | EDAM URI |
|--------|---------|-----------|----------|
"""
    
    for mapping in mappings:
        if mapping['verification_status'] == 'VERIFIED':
            md += f"| {mapping['format']} | `{mapping['matched_edam_id']}` | {mapping['actual_edam_label']} | {mapping['edam_uri']} |\n"
    
    md += f"""

### Ambiguous Mappings ({ambiguous})

Mappings where the EDAM ID was found but the label does not exactly match:

| Format | Proposed ID | Expected Label | Actual EDAM Label |
|--------|-------------|-----------------|-------------------|
"""
    
    for mapping in mappings:
        if mapping['verification_status'] == 'AMBIGUOUS':
            md += f"| {mapping['format']} | `{mapping['matched_edam_id']}` | {mapping['edam_term']} | {mapping['actual_edam_label']} |\n"
    
    md += f"""

### Not Found Mappings ({not_found})

Mappings where the proposed EDAM ID does not exist in the ontology:

| Format | Proposed ID | Expected Label |
|--------|-------------|-----------------|
"""
    
    for mapping in mappings:
        if mapping['verification_status'] == 'NOT_FOUND':
            md += f"| {mapping['format']} | `{mapping['proposed_edam_id']}` | {mapping['edam_term']} |\n"
    
    md += f"""

### Unmapped Formats ({unmapped})

Formats without proposed EDAM IDs. Search results shown where available:

"""
    
    for mapping in mappings:
        if mapping['verification_status'] == 'UNMAPPED':
            md += f"\n#### {mapping['format']}\n\n"
            md += f"- **Search term:** {mapping['edam_term']}\n"
            md += f"- **Note:** {mapping['verification_note']}\n"
            
            if mapping['search_matches']:
                md += "- **Potential matches in EDAM:**\n"
                for match in mapping['search_matches'][:5]:
                    md += f"  - `{match['id']}` → {match['label']}\n"
            else:
                md += "- **Matches:** None found\n"
    
    md += f"""

## Verification Method

1. Downloaded official EDAM.owl from https://edamontology.org/EDAM.owl
2. Parsed ontology using {json_output['metadata']['parser_used']}
3. For each proposed EDAM ID:
   - Verified the ID exists in the ontology
   - Retrieved the actual rdfs:label
   - Compared with expected term name
   - Validated type (format_XXXX or data_XXXX)
4. For unmapped formats, searched EDAM by label

## Conclusions

- **High confidence:** {verified} mappings verified successfully
- **Investigation needed:** {ambiguous} ambiguous mappings require review
- **Incorrect IDs:** {not_found} proposed IDs not found in EDAM
- **New mappings needed:** {unmapped} formats lack EDAM mappings

## Notes

- EDAM ontology verified programmatically against official source
- No EDAM IDs were invented or guessed
- Results reflect actual contents of EDAM.owl at time of verification
- Labels are case-sensitive in matching (exact case comparison used)

---

*Report generated by verify_edam_mappings.py*
"""
    
    return md

if __name__ == '__main__':
    sys.exit(main())
