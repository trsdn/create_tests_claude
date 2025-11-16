#!/usr/bin/env python3
"""
HTML Generator für Klassenarbeiten
Konvertiert Markdown-Tests zu druckbaren HTML-Dateien
"""

import re
import os
from pathlib import Path

# HTML Template mit CSS
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        @page {{
            size: A4;
            margin: 1.5cm;
        }}
        body {{
            font-family: 'Arial', 'Helvetica', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 210mm;
            margin: 0 auto;
            padding: 15px;
            font-size: 11pt;
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
            font-size: 24pt;
            margin: 10px 0;
        }}
        h2 {{
            color: #2980b9;
            margin-top: 25px;
            border-left: 5px solid #3498db;
            padding-left: 15px;
            font-size: 16pt;
            page-break-after: avoid;
        }}
        h3 {{
            color: #34495e;
            margin-top: 15px;
            font-size: 13pt;
        }}
        .header-info {{
            display: flex;
            justify-content: space-between;
            margin: 15px 0;
            font-weight: bold;
            font-size: 10pt;
        }}
        .info-center {{
            text-align: center;
            margin: 15px 0;
            font-weight: bold;
            font-size: 11pt;
        }}
        .question {{
            margin: 12px 0;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 5px;
            page-break-inside: avoid;
        }}
        .choices {{
            margin-left: 25px;
            margin-top: 5px;
        }}
        .answer-line {{
            border-bottom: 1px solid #666;
            min-width: 400px;
            display: inline-block;
            margin: 3px 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }}
        table th, table td {{
            border: 1px solid #ddd;
            padding: 10px;
            text-align: center;
        }}
        table th {{
            background-color: #3498db;
            color: white;
            font-weight: bold;
        }}
        table tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        .points {{
            float: right;
            font-weight: bold;
            color: #e74c3c;
        }}
        .text-box {{
            background: #f0f8ff;
            padding: 15px;
            border-left: 4px solid #3498db;
            margin: 15px 0;
            border-radius: 5px;
        }}
        hr {{
            border: none;
            border-top: 2px solid #ccc;
            margin: 20px 0;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 15px;
            border-top: 2px solid #ccc;
            font-size: 9pt;
            color: #666;
            text-align: center;
        }}
        .difficulty-star {{
            color: #f39c12;
        }}
        p {{
            margin: 8px 0;
        }}
        strong {{
            color: #2c3e50;
        }}
        @media print {{
            body {{
                padding: 0;
            }}
            .question, h2, h3 {{
                page-break-inside: avoid;
            }}
            .page-break {{
                page-break-after: always;
            }}
        }}
    </style>
</head>
<body>
{content}
</body>
</html>
"""

def parse_frontmatter(content):
    """Extrahiere YAML Frontmatter"""
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        frontmatter_text = match.group(1)
        title_match = re.search(r'title:\s*"([^"]+)"', frontmatter_text)
        test_id_match = re.search(r'test_id:\s*(\S+)', frontmatter_text)
        
        title = title_match.group(1) if title_match else "Klassenarbeit"
        test_id = test_id_match.group(1) if test_id_match else "unknown"
        
        # Remove frontmatter from content
        content = content[match.end():]
        return title, test_id, content
    return "Klassenarbeit", "unknown", content

def convert_markdown_to_html(md_content):
    """Konvertiere Markdown zu HTML"""
    html = md_content
    
    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    
    # Emojis und Sterne
    html = html.replace('⭐', '<span class="difficulty-star">⭐</span>')
    html = html.replace('📋', '📋')
    html = html.replace('✏️', '✏️')
    html = html.replace('🔄', '🔄')
    html = html.replace('📖', '📖')
    html = html.replace('✍️', '✍️')
    html = html.replace('📊', '📊')
    html = html.replace('💡', '💡')
    html = html.replace('🍀', '🍀')
    html = html.replace('🎯', '🎯')
    
    # Checkboxes
    html = html.replace('- [ ]', '☐')
    
    # Answer lines (placeholder)
    html = re.sub(r'_{10,}', '<span class="answer-line"></span>', html)
    html = re.sub(r'__________', '<span class="answer-line"></span>', html)
    
    # Horizontal rules
    html = html.replace('---\n', '<hr>\n')
    
    # Paragraphs
    lines = html.split('\n')
    processed = []
    in_para = False
    
    for line in lines:
        stripped = line.strip()
        
        # Skip empty lines
        if not stripped:
            if in_para:
                processed.append('</p>')
                in_para = False
            processed.append('')
            continue
            
        # HTML tags - don't wrap
        if stripped.startswith('<'):
            if in_para:
                processed.append('</p>')
                in_para = False
            processed.append(line)
        # Regular text
        else:
            if not in_para and not stripped.startswith('#'):
                processed.append('<p>')
                in_para = True
            processed.append(line)
    
    if in_para:
        processed.append('</p>')
    
    html = '\n'.join(processed)
    
    return html

def create_header_section(content):
    """Erstelle Header mit Name, Klasse, Datum"""
    # Find the header info pattern
    pattern = r'\*\*Name:\*\*[^\n]+\*\*Klasse:\*\*[^\n]+\*\*Datum:\*\*[^\n]+'
    match = re.search(pattern, content)
    
    if match:
        header_html = '''
        <div class="header-info">
            <div>Name: _________________________</div>
            <div>Klasse: 6___</div>
            <div>Datum: _______________</div>
        </div>
        '''
        content = content.replace(match.group(0), header_html)
    
    return content

def create_points_info(content):
    """Format points information"""
    content = re.sub(
        r'\*\*Gesamtpunktzahl:\*\* (\d+) Punkte \| \*\*Zeit:\*\* (\d+) Minuten',
        r'<div class="info-center"><strong>Gesamtpunktzahl:</strong> \1 Punkte | <strong>Zeit:</strong> \2 Minuten</div>',
        content
    )
    return content

def process_markdown_file(input_path, output_path):
    """Verarbeite eine Markdown-Datei zu HTML"""
    print(f"Processing: {input_path}")
    
    # Read markdown
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse frontmatter
    title, test_id, content = parse_frontmatter(content)
    
    # Create header section
    content = create_header_section(content)
    content = create_points_info(content)
    
    # Convert to HTML
    html_content = convert_markdown_to_html(content)
    
    # Add footer
    html_content += f'''
    <div class="footer">
        Erstellt mit dem Educational Test Creator System<br>
        Test-ID: {test_id} | Niedersachsen Kerncurriculum 2015
    </div>
    '''
    
    # Wrap in template
    final_html = HTML_TEMPLATE.format(
        title=title,
        content=html_content
    )
    
    # Write HTML
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"Created: {output_path}")

def main():
    """Main function"""
    # Paths
    tests_dir = Path('/Users/torstenmahr/GitHub/create_tests/tests/germany/niedersachsen/gymnasium/englisch/grade_6/present_simple_vs_past_progressive')
    output_dir = Path('/Users/torstenmahr/GitHub/create_tests/pdfs/student_versions')
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all markdown test files
    test_files = [
        'klassenarbeit_v1.md',
        'klassenarbeit_v2.md',
        'klassenarbeit_v3.md',
        'klassenarbeit_v4.md',
        'klassenarbeit_v5.md'
    ]
    
    for test_file in test_files:
        input_path = tests_dir / test_file
        output_file = test_file.replace('.md', '.html')
        output_path = output_dir / output_file
        
        if input_path.exists():
            process_markdown_file(input_path, output_path)
        else:
            print(f"Warning: {input_path} not found!")
    
    print(f"\n✅ Conversion complete!")
    print(f"📁 HTML files saved to: {output_dir}")
    print(f"\n💡 To create PDFs:")
    print(f"   1. Open each HTML file in your browser")
    print(f"   2. Press Cmd+P (Mac) or Ctrl+P (Windows)")
    print(f"   3. Choose 'Save as PDF'")
    print(f"   4. Adjust margins if needed (recommend: minimal)")

if __name__ == '__main__':
    main()
