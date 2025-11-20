Convert Markdown test files to professional PDF format using Pandoc and LaTeX.

This command generates both student versions and answer key PDFs with proper formatting.

**What it does:**
1. Reads Markdown test file from tests/ directory
2. Applies LaTeX template (test_default.tex or answer_key.tex)
3. Generates professional PDF with:
   - Proper page breaks
   - Consistent formatting
   - Answer boxes/lines for student version
   - Highlighted solutions for answer key
4. Saves to same directory as Markdown file

**Usage:**
```
/generate-pdf
```

You'll be prompted for:
- Test file path (Markdown file in tests/ directory)
- PDF type: student version, answer key, or both

**Requirements:**
- Pandoc installed (`brew install pandoc` on macOS)
- LaTeX distribution (included with Pandoc typically)

**Output:**
- Student PDF: `tests/{path}/{filename}.pdf`
- Answer Key PDF: `tests/{path}/{filename}_key.pdf`

**Formatting features:**
- A4 or Letter paper size (region-specific)
- Professional fonts and spacing
- Page numbers and headers
- Answer boxes/lines properly sized
- Color-coding for difficulty levels (optional)

**Time:** < 1 minute per PDF

**Note:** If Pandoc not installed, will provide installation instructions.
