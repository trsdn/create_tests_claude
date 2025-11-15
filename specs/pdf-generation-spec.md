# PDF Generation Specifications

[← Back to Documentation Index](../README.md)

---

## Overview

This document provides comprehensive specifications for converting Markdown test files to professional PDF format.

---

## 1. PDF Output Requirements

### 1.1 Student Version PDF

**Purpose:** Printable test for students to complete

**Features:**
- Clean, readable layout
- Checkbox symbols (☐) for answers
- Adequate spacing for written answers
- Page numbers
- Header with test title and student name field
- Footer with page numbers
- **NO** answer keys or solutions visible
- Professional appearance

**Layout Example:**
```
┌─────────────────────────────────────────────┐
│ [Test Title]              Name: ___________ │
│ Grade [X] | Date: _________                 │
├─────────────────────────────────────────────┤
│                                             │
│ Question 1: [Question text]                 │
│   ☐ A) Option 1                            │
│   ☐ B) Option 2                            │
│   ☐ C) Option 3                            │
│                                             │
├─────────────────────────────────────────────┤
│              Page 1 of 3                    │
└─────────────────────────────────────────────┘
```

### 1.2 Answer Key PDF

**Purpose:** Reference document for teachers/parents

**Features:**
- All questions with correct answers highlighted
- Explanations and rubrics included
- Point values clearly marked
- Difficulty ratings visible
- Additional teaching notes (if any)
- May include fun facts and learning resources

**Layout Example:**
```
┌─────────────────────────────────────────────┐
│ [Test Title] - ANSWER KEY                   │
│ Grade [X] | Total Points: 100               │
├─────────────────────────────────────────────┤
│                                             │
│ Question 1 [5 points]:                      │
│   ☐ A) Option 1                            │
│   ☑ B) Option 2 ← CORRECT                  │
│   ☐ C) Option 3                            │
│                                             │
│ Explanation: [Why B is correct]             │
├─────────────────────────────────────────────┤
│              Page 1 of 3                    │
└─────────────────────────────────────────────┘
```

---

## 2. Styling Themes

### 2.1 Default Theme

```css
Font: Arial or Helvetica (sans-serif)
Title Font Size: 18pt, bold
Question Font Size: 12pt
Body Font Size: 11pt
Colors: Black text on white background
Margins: 1 inch (2.54cm) all sides
Line Spacing: 1.5 for readability
```

### 2.2 Colorful Theme

```css
Font: Comic Sans MS or kid-friendly
Title Color: Blue (#2E86DE)
Accent Color: Orange (#FF9F43) for question numbers
Correct Answers: Green highlight (#26DE81)
Background: Light pastel colors for sections
Icons: Colorful emojis and graphics
```

### 2.3 Minimal Theme

```css
Font: Times New Roman (serif)
Colors: Black and white only
Minimal Graphics: Text-focused
Compact Layout: More questions per page
Professional: Suitable for formal testing
```

---

## 3. Page Layout Options

### 3.1 Standard A4 (210mm × 297mm)
- **Orientation:** Portrait (default) or Landscape
- **Margins:** 25mm top/bottom, 20mm left/right
- **Ideal for:** International use, most schools

### 3.2 US Letter (8.5" × 11")
- **Orientation:** Portrait (default) or Landscape
- **Margins:** 1 inch all sides
- **Ideal for:** US-based schools

### 3.3 Custom Sizes
- Half-page booklets
- Index cards (for flashcard-style)
- Large print (for accessibility)

---

## 4. PDF Generation Tools

### 4.1 Option 1: Pandoc (Recommended)

```bash
pandoc test.md -o test.pdf \
  --pdf-engine=xelatex \
  --template=custom_template.tex \
  --variable=geometry:margin=1in \
  --variable=fontsize=12pt
```

**Pros:**
- Highly configurable
- Excellent typography
- Supports LaTeX templates
- Good for complex layouts

**Cons:**
- Requires LaTeX installation
- Steeper learning curve

### 4.2 Option 2: markdown-pdf (Node.js)

```bash
npm install -g markdown-pdf
markdown-pdf test.md -o test.pdf \
  --css-path styles.css \
  --remarkable-options '{ "html": true }'
```

**Pros:**
- Easy to use
- CSS styling
- Node.js ecosystem

**Cons:**
- Limited advanced features
- Requires Node.js

### 4.3 Option 3: wkhtmltopdf

```bash
# Convert MD to HTML first, then to PDF
pandoc test.md -o test.html --standalone
wkhtmltopdf test.html test.pdf \
  --margin-top 20mm \
  --margin-bottom 20mm \
  --enable-local-file-access
```

**Pros:**
- Web technology based
- Good CSS support
- No LaTeX required

**Cons:**
- Two-step process
- Deprecated (but still works)

### 4.4 Option 4: Python (weasyprint)

```python
from markdown import markdown
from weasyprint import HTML

html_content = markdown(md_content)
HTML(string=html_content).write_pdf('test.pdf')
```

**Pros:**
- Pure Python
- Good CSS3 support
- Programmatic control

**Cons:**
- Requires Python
- Additional dependencies

---

## 5. CSS Styling

### 5.1 Student Version CSS

```css
/* student_version.css */
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
  margin-bottom: 20px;
}

h2 {
  font-size: 14pt;
  color: #34495e;
  margin-top: 20px;
  page-break-after: avoid;
}

.question {
  margin-bottom: 25px;
  page-break-inside: avoid;
}

.answer-options {
  margin-left: 20px;
  line-height: 2;
}

/* Hide answers in student version */
.answer-key {
  display: none;
}

/* Checkbox styling */
input[type="checkbox"] {
  width: 15px;
  height: 15px;
  margin-right: 10px;
}
```

### 5.2 Answer Key CSS

```css
/* answer_key.css */
@page {
  size: A4;
  margin: 2cm;
  @top-center {
    content: "Answer Key - Teacher Copy";
  }
}

/* Show correct answers with highlighting */
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

## 6. PDF Metadata

Each generated PDF should include:

```yaml
PDF_Metadata:
  Title: "Linear Equations Test"
  Subject: "Mathematics"
  Author: "Educational Test Creator"
  Keywords: "math, algebra, grade7, gymnasium"
  Creator: "PDF Generator Agent v1.0"
  Producer: "Pandoc" # or other tool used
  CreationDate: "2025-11-15T10:30:00Z"
  Custom_Fields:
    Grade_Level: "7"
    Difficulty: "Medium"
    Question_Count: "10"
    Version: "Student" # or "Answer Key"
```

---

## 7. File Naming Convention

```
[Subject]_[Topic]_Grade[X]_[Type].pdf

Examples:
- Math_Addition_Grade1_Student.pdf
- Math_Addition_Grade1_AnswerKey.pdf
- Science_SolarSystem_Grade4_Student.pdf
- Science_SolarSystem_Grade4_AnswerKey.pdf
```

---

## 8. Advanced Features

### 8.1 Interactive PDFs (Optional)
- Fillable form fields for digital completion
- Clickable checkboxes
- Submit button for online submission
- Auto-calculation of scores

### 8.2 Accessibility Features
- Screen reader compatible
- High contrast mode
- Adjustable font sizes
- Tagged PDF structure
- Alt text for images

### 8.3 Multi-page Management
- Automatic page breaks
- "Continued on next page" indicators
- No questions split awkwardly across pages
- Table of contents for longer tests

---

## 9. Quality Control Checklist

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

## 10. Error Handling

### 10.1 Missing Images
- Log warning
- Continue with placeholder text
- Note in generation report

### 10.2 Conversion Errors
- Report specific issue and location
- Attempt alternative rendering
- Provide fallback options

### 10.3 Large Files
- Compress images
- Optimize output
- Split into multiple files if needed

---

## Related Documentation

- [PDF Generator Agent](./agents/pdf-generator-agent.md)
- [Formatter Agent](./agents/formatter-agent.md)
- [Repository Organization](./repository-organization.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
