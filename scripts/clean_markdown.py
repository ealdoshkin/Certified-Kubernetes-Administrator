#!/usr/bin/env python3
"""
Clean up markdown files converted from PDFs.
"""

import re
import sys
from pathlib import Path

def clean_markdown(content, filename):
    """Clean and improve markdown formatting."""
    lines = content.split('\n')
    cleaned = []
    
    # Skip header lines with "Converted from" and unnecessary metadata
    skip_until_question = True
    
    for i, line in enumerate(lines):
        # Skip conversion notice
        if '*Converted from' in line:
            continue
        
        # Skip generic headers like "Exam Questions CKA"
        if skip_until_question:
            if line.startswith('## Question'):
                skip_until_question = False
                # Add proper header
                title = filename.replace('.md', '').replace('_', ' ').upper()
                cleaned.append(f"# {title}")
                cleaned.append("")
                cleaned.append("---")
                cleaned.append("")
            else:
                continue
        
        # Fix common PDF extraction issues
        # Fix "var 1" -> "var1" (but only in context of environment variables)
        line = re.sub(r'\bvar\s+(\d+)\b', r'var\1', line)
        line = re.sub(r'\bvalue\s+(\d+)\b', r'value\1', line)
        
        # Fix broken column names like "P OD_N AM E" -> "POD_NAME"
        line = re.sub(r'P\s+OD\s*_\s*N\s*AM\s*E', 'POD_NAME', line)
        line = re.sub(r'P\s+OD\s*_\s*S\s*TA\s*TU\s*S', 'POD_STATUS', line)
        
        # Fix "In anew" -> "In a new"
        line = re.sub(r'\bIn anew\b', 'In a new', line)
        line = re.sub(r'\bnamespacenamed\b', 'namespace named', line)
        
        # Fix "contain3replicas" -> "contain 3 replicas"
        line = re.sub(r'contain\s*(\d+)replicas', r'contain \1 replicas', line)
        line = re.sub(r'(\d+)replicas', r'\1 replicas', line)
        
        # Fix "containernginxwithversion" -> "container nginx with version"
        line = re.sub(r'containernginx', 'container nginx', line)
        line = re.sub(r'nginxwith', 'nginx with', line)
        line = re.sub(r'withversion', 'with version', line)
        
        # Fix "byperforming" -> "by performing"
        line = re.sub(r'byperforming', 'by performing', line)
        
        # Fix "totheprevious" -> "to the previous"
        line = re.sub(r'totheprevious', 'to the previous', line)
        
        # Fix "newversion" -> "new version"
        line = re.sub(r'\bnewversion\b', 'new version', line)
        
        # Fix "theprevious" -> "the previous"
        line = re.sub(r'\btheprevious\b', 'the previous', line)
        
        # Fix "ek8s-node-1as" -> "ek8s-node-1 as"
        line = re.sub(r'(\w+-\w+-\d+)([a-z])', r'\1 \2', line)
        
        # Fix "app-data, of capacity2Gi" -> "app-data, of capacity 2Gi"
        line = re.sub(r'capacity(\d+[A-Z])', r'capacity \1', line)
        
        # Fix "access modeReadWriteMany" -> "access mode ReadWriteMany"
        line = re.sub(r'mode([A-Z])', r'mode \1', line)
        
        # Fix "type of volume ishostPath" -> "type of volume is hostPath"
        line = re.sub(r'is([a-z][A-Z])', r'is \1', line)
        
        # Fix "location is/srv/app-data" -> "location is /srv/app-data"
        line = re.sub(r'is(/[^\s]+)', r'is \1', line)
        
        # Fix "Name:mongo" -> "Name: mongo" (but preserve in code blocks)
        if not line.strip().startswith('```') and 'kubectl' not in line:
            line = re.sub(r'([a-zA-Z]):([a-zA-Z][a-z])', r'\1: \2', line)
        
        # Remove empty solution sections
        if line.strip() == '**Solution:**' and i + 1 < len(lines) and not lines[i + 1].strip():
            continue
        
        # Fix duplicate code block markers
        if line.strip() == '```' and cleaned and cleaned[-1].strip() in ['```', '```bash']:
            continue
        
        cleaned.append(line)
    
    # Join and clean up
    content = '\n'.join(cleaned)
    
    # Fix code blocks - ensure proper closing
    # Remove standalone ``` that aren't part of code blocks
    content = re.sub(r'\n```\n(?!bash|yaml|json|shell|sh)', '\n', content)
    
    # Fix code blocks that aren't closed properly
    # Close code blocks before separators
    content = re.sub(r'```bash\n([^`]+?)\n\n---', r'```bash\n\1\n```\n\n---', content, flags=re.MULTILINE | re.DOTALL)
    # Close code blocks at end of explanation sections
    content = re.sub(r'```bash\n([^`]+?)\n\n\*\*', r'```bash\n\1\n```\n\n**', content, flags=re.MULTILINE | re.DOTALL)
    
    # Remove multiple consecutive empty lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Remove trailing whitespace
    lines = content.split('\n')
    cleaned_lines = [line.rstrip() for line in lines]
    content = '\n'.join(cleaned_lines)
    
    # Final pass: fix any remaining code block issues
    # Remove empty code blocks
    content = re.sub(r'```bash\n```\n', '', content)
    content = re.sub(r'```\n```\n', '', content)
    
    return content

def main():
    """Clean all markdown files in exercises/pdfs directory."""
    exercises_dir = Path(__file__).parent.parent / 'exercises' / 'pdfs'
    
    if not exercises_dir.exists():
        print(f"Error: {exercises_dir} not found", file=sys.stderr)
        return 1
    
    md_files = list(exercises_dir.glob('*.md'))
    
    if not md_files:
        print(f"No markdown files found in {exercises_dir}", file=sys.stderr)
        return 1
    
    print(f"Cleaning {len(md_files)} markdown file(s)...\n")
    
    for md_file in sorted(md_files):
        print(f"Cleaning {md_file.name}...")
        try:
            content = md_file.read_text(encoding='utf-8')
            cleaned = clean_markdown(content, md_file.name)
            md_file.write_text(cleaned, encoding='utf-8')
            print(f"✓ Cleaned {md_file.name}")
        except Exception as e:
            print(f"✗ Error cleaning {md_file.name}: {e}", file=sys.stderr)
    
    print(f"\n✓ Successfully cleaned {len(md_files)} file(s)")
    return 0

if __name__ == '__main__':
    sys.exit(main())
