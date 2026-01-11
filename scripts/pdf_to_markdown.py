#!/usr/bin/env python3
"""
Convert PDF exercise files to Markdown format.
"""

import subprocess
import re
import sys
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using pdftotext."""
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', str(pdf_path), '-'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error extracting text from {pdf_path}: {e}", file=sys.stderr)
        return None
    except FileNotFoundError:
        print("Error: pdftotext not found. Please install poppler-utils.", file=sys.stderr)
        return None

def format_as_markdown(text, pdf_name):
    """Convert extracted text to formatted markdown."""
    lines = text.split('\n')
    md_lines = []
    
    # Add header
    md_lines.append(f"# {pdf_name.replace('.pdf', '').replace('_', ' ').title()}")
    md_lines.append("")
    md_lines.append(f"*Converted from {pdf_name}*")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    
    i = 0
    current_question = None
    in_explanation = False
    in_code = False
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Skip empty lines at the start
        if not line and not md_lines:
            i += 1
            continue
        
        # Skip header/footer lines
        if any(skip in line.lower() for skip in ['welcome to download', '2passeasy', 'passing certification', 'visit -']):
            i += 1
            continue
        
        # Detect question headers
        question_match = re.match(r'^(NEW\s+)?QUESTION\s+(\d+)', line, re.IGNORECASE)
        if question_match:
            if current_question:
                md_lines.append("")
                md_lines.append("---")
                md_lines.append("")
            question_num = question_match.group(2)
            md_lines.append(f"## Question {question_num}")
            md_lines.append("")
            current_question = question_num
            in_explanation = False
            i += 1
            continue
        
        # Detect answer line
        if re.match(r'^Answer:\s*[A-Z]', line, re.IGNORECASE):
            if in_code:
                md_lines.append("```")
                md_lines.append("")
                in_code = False
            md_lines.append(f"**Answer:** {line.split(':', 1)[1].strip()}")
            md_lines.append("")
            i += 1
            continue
        
        # Detect explanation header
        if re.match(r'^Explanation:', line, re.IGNORECASE):
            md_lines.append("**Explanation:**")
            md_lines.append("")
            in_explanation = True
            i += 1
            continue
        
        # Detect solution header
        if re.match(r'^solution', line, re.IGNORECASE):
            md_lines.append("**Solution:**")
            md_lines.append("")
            in_explanation = True
            i += 1
            continue
        
        # Skip file paths (like F:\Work\...)
        if re.match(r'^[A-Z]:\\', line):
            i += 1
            continue
        
        # Skip markdown code block markers that might appear in text
        if line.strip() == '```':
            i += 1
            continue
        
        # Detect kubectl commands and format as code
        if line and ('kubectl' in line.lower() or line.startswith('#') or 
                     any(cmd in line for cmd in ['kubectl', 'kubeadm', 'etcdctl', 'curl', 'wget'])):
            if not in_code:
                md_lines.append("```bash")
                in_code = True
            md_lines.append(line)
            i += 1
            continue
        
        # If we were in code block and hit non-code line, close code block
        if in_code and line and not any(indicator in line.lower() for indicator in 
                                         ['kubectl', '#', 'curl', 'wget', 'kubeadm', 'etcdctl', '```']):
            # Don't close if it's just whitespace or continuation
            if not line.startswith((' ', '\t')) and len(line) > 3:
                md_lines.append("```")
                md_lines.append("")
                in_code = False
        
        # Format regular content
        if line:
            # Check if it's a question (starts with capital, not a command)
            if current_question and not in_explanation and not line.startswith(('A.', 'B.', 'C.', 'D.')):
                md_lines.append(line)
            # Format answer options
            elif re.match(r'^[A-Z]\.\s+', line):
                md_lines.append(f"- {line}")
            # Regular text
            else:
                md_lines.append(line)
        
        i += 1
    
    # Close any open code block
    if in_code:
        md_lines.append("```")
        md_lines.append("")
    
    # Clean up markdown: remove stray code block markers and fix formatting
    md_content = '\n'.join(md_lines)
    
    # Remove standalone ``` markers (not part of code blocks)
    md_content = re.sub(r'\n```\n(?!bash|yaml|json|shell|sh)', '\n', md_content)
    
    # Fix double newlines
    md_content = re.sub(r'\n{3,}', '\n\n', md_content)
    
    # Remove empty code blocks
    md_content = re.sub(r'```bash\n```\n', '', md_content)
    md_content = re.sub(r'```\n```\n', '', md_content)
    
    return md_content

def convert_pdf_to_markdown(pdf_path, output_dir=None):
    """Convert a PDF file to Markdown."""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"Error: {pdf_path} not found", file=sys.stderr)
        return False
    
    print(f"Converting {pdf_path.name}...")
    
    # Extract text
    text = extract_text_from_pdf(pdf_path)
    if not text:
        return False
    
    # Format as markdown
    md_content = format_as_markdown(text, pdf_path.name)
    
    # Determine output path
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = pdf_path.parent
    
    output_path = output_dir / f"{pdf_path.stem}.md"
    
    # Write markdown file
    try:
        output_path.write_text(md_content, encoding='utf-8')
        print(f"✓ Created {output_path}")
        return True
    except Exception as e:
        print(f"Error writing {output_path}: {e}", file=sys.stderr)
        return False

def main():
    """Main function to convert all PDFs in exercises/pdfs directory."""
    exercises_dir = Path(__file__).parent.parent / 'exercises' / 'pdfs'
    
    if not exercises_dir.exists():
        print(f"Error: {exercises_dir} not found", file=sys.stderr)
        return 1
    
    pdf_files = list(exercises_dir.glob('*.pdf'))
    
    if not pdf_files:
        print(f"No PDF files found in {exercises_dir}", file=sys.stderr)
        return 1
    
    print(f"Found {len(pdf_files)} PDF file(s) to convert\n")
    
    success_count = 0
    for pdf_file in sorted(pdf_files):
        if convert_pdf_to_markdown(pdf_file):
            success_count += 1
    
    print(f"\n✓ Successfully converted {success_count}/{len(pdf_files)} PDF file(s)")
    return 0 if success_count == len(pdf_files) else 1

if __name__ == '__main__':
    sys.exit(main())
