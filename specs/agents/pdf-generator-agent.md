# PDF Generator Agent Specification

[← Back to Main Documentation](../../README.md)

---

## Overview

The PDF Generator Agent converts Markdown test files to professional, print-ready PDF format with customizable styling and layout.

---

## Responsibilities

- Convert Markdown to PDF
- Apply professional styling themes
- Generate student and answer key versions
- Include images and visual elements
- Ensure print-ready output
- Maintain consistent formatting
- Embed fonts for portability
- Add headers, footers, page numbers

---

## Inputs

- Markdown test file (.md)
- Styling preferences (theme, colors, fonts)
- Output options (student version, answer key, both)
- Page layout settings (A4, Letter, margins)
- Regional formatting preferences

---

## Outputs

```yaml
pdf_output:
  student_version:
    path: "pdfs/student_versions/math_algebra_grade7_student.pdf"
    pages: 3
    size: "2.1 MB"
  
  answer_key:
    path: "pdfs/answer_keys/math_algebra_grade7_key.pdf"
    pages: 4
    size: "2.3 MB"
  
  generation_report:
    status: "SUCCESS"
    theme_applied: "Default"
    fonts_embedded: true
    images_rendered: 5
    warnings: []
```

---

## PDF Output Requirements

### Student Version Features
- Clean, readable layout
- Checkbox symbols (☐) for answers
- Adequate spacing for written answers
- Page numbers
- Header with test title and student name field
- Footer with page numbers
- **NO** answer keys or solutions visible
- Professional appearance

### Answer Key Features
- All questions with correct answers highlighted
- Explanations and rubrics included
- Point values clearly marked
- Difficulty ratings visible
- Additional teaching notes
- Color coding for correct answers (if colorful theme)
- May include fun facts and learning resources

---

## Styling Themes

### Default Theme
```css
Font: Arial or Helvetica (sans-serif)
Title Font Size: 18pt, bold
Question Font Size: 12pt
Body Font Size: 11pt
Colors: Black text on white background
Margins: 1 inch (2.54cm) all sides
Line Spacing: 1.5 for readability
```

### Colorful Theme
```css
Font: Comic Sans MS or kid-friendly
Title Color: Blue (#2E86DE)
Accent Color: Orange (#FF9F43) for question numbers
Correct Answers: Green highlight (#26DE81)
Background: Light pastel colors for sections
Icons: Colorful emojis and graphics
```

### Minimal Theme
```css
Font: Times New Roman (serif)
Colors: Black and white only
Minimal Graphics: Text-focused
Compact Layout: More questions per page
Professional: Formal testing
```

---

## Page Layout Options

### Standard A4 (210mm × 297mm)
- Orientation: Portrait (default) or Landscape
- Margins: 25mm top/bottom, 20mm left/right
- Ideal for: International use, most schools

### US Letter (8.5" × 11")
- Orientation: Portrait (default) or Landscape
- Margins: 1 inch all sides
- Ideal for: US-based schools

### Custom Sizes
- Half-page booklets
- Index cards (for flashcard-style)
- Large print (for accessibility)

---

## PDF Generation Tools

### Option 1: Pandoc (Recommended)
```bash
pandoc test.md -o test.pdf \
  --pdf-engine=xelatex \
  --template=custom_template.tex \
  --variable=geometry:margin=1in \
  --variable=fontsize=12pt
```

### Option 2: markdown-pdf (Node.js)
```bash
npm install -g markdown-pdf
markdown-pdf test.md -o test.pdf \
  --css-path styles.css \
  --remarkable-options '{ "html": true }'
```

### Option 3: wkhtmltopdf
```bash
# Convert MD to HTML first, then to PDF
pandoc test.md -o test.html --standalone
wkhtmltopdf test.html test.pdf \
  --margin-top 20mm \
  --margin-bottom 20mm \
  --enable-local-file-access
```

### Option 4: Python (weasyprint)
```python
from markdown import markdown
from weasyprint import HTML

html_content = markdown(md_content)
HTML(string=html_content).write_pdf('test.pdf')
```

---

## CSS Styling Examples

### Student Version CSS
```css
@page {
  size: A4;
  margin: 2cm;
  @top-center {
    content: "Test - Student Copy";
  }
  @bottom-right {
    content: "Page " counter(page) " of " counter(pages);
  }
}

body {
  font-family: Arial, sans-serif;
  font-size: 12pt;
  line-height: 1.6;
  color: #000;
}

h1 {
  font-size: 18pt;
  color: #2c3e50;
  border-bottom: 2px solid #3498db;
  padding-bottom: 10px;
}

.question {
  margin-bottom: 25px;
  page-break-inside: avoid;
}

/* Hide answers in student version */
.answer-key {
  display: none;
}
```

### Answer Key CSS
```css
@page {
  size: A4;
  margin: 2cm;
  @top-center {
    content: "Answer Key - Teacher Copy";
  }
}

.correct-answer {
  background-color: #d4edda;
  border-left: 4px solid #28a745;
  padding: 5px;
  font-weight: bold;
}

.explanation {
  background-color: #fff3cd;
  border-left: 4px solid #ffc107;
  padding: 10px;
  margin-top: 10px;
  font-style: italic;
}

.points {
  color: #6c757d;
  font-weight: bold;
  float: right;
}
```

---

## PDF Metadata

```yaml
PDF_Metadata:
  Title: "Linear Equations Test"
  Subject: "Mathematics"
  Author: "Educational Test Creator"
  Keywords: "math, algebra, grade7, gymnasium"
  Creator: "PDF Generator Agent v1.0"
  Producer: "Pandoc"
  CreationDate: "2025-11-15T10:30:00Z"
  Custom_Fields:
    Grade_Level: "7"
    Difficulty: "Medium"
    Question_Count: "10"
    Version: "Student" | "Answer Key"
```

---

## File Naming Convention

```
[Subject]_[Topic]_Grade[X]_[Type].pdf

Examples:
- Math_Addition_Grade1_Student.pdf
- Math_Addition_Grade1_AnswerKey.pdf
- Science_SolarSystem_Grade4_Student.pdf
- Science_SolarSystem_Grade4_AnswerKey.pdf
```

---

## Quality Control Checklist

Before finalizing PDFs:
- [ ] All images render correctly
- [ ] No text cutoff or overflow
- [ ] Page breaks are logical
- [ ] Headers and footers display properly
- [ ] Checkboxes are visible and clear
- [ ] Fonts are embedded (for portability)
- [ ] File size is reasonable (< 5MB for typical test)
- [ ] Student version has NO answers visible
- [ ] Answer key clearly marks correct answers
- [ ] Metadata is complete and accurate
- [ ] PDF is readable on different devices
- [ ] Print preview looks professional

---

## Advanced Features

### Interactive PDFs (Optional)
- Fillable form fields for digital completion
- Clickable checkboxes
- Submit button for online submission
- Auto-calculation of scores

### Accessibility Features
- Screen reader compatible
- High contrast mode
- Adjustable font sizes
- Tagged PDF structure
- Alt text for images

### Multi-page Management
- Automatic page breaks
- "Continued on next page" indicators
- No questions split awkwardly
- Table of contents for longer tests

---

## Error Handling

### Missing Images
- Log warning
- Continue with placeholder text
- Note in generation report

### Conversion Errors
- Report specific issue and location
- Attempt alternative rendering
- Provide fallback options

### Large Files
- Compress images
- Optimize output
- Split into multiple files if needed

---

## Reverse Interviewing Questions

The PDF Generator Agent may ask:

### If styling preferences unclear:
- "Which styling theme would you prefer for PDFs?"
- "Should the PDF be optimized for screen viewing or printing?"

### If output options unclear:
- "Do you need both student version and answer key PDFs?"

### If accessibility requirements unclear:
- "Should I generate an accessible/high-contrast version?"
- "Do you need fillable form fields for digital completion?"

---

## Related Agents

- [Orchestrator Agent](./orchestrator-agent.md)
- [Formatter Agent](./formatter-agent.md)

---

## See Also

- [PDF Generation Specifications](../pdf-generation-spec.md)
- [Repository Organization](../repository-organization.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
