# Formatter Agent Specification

[← Back to Main Documentation](../../README.md)

---

## Overview

The Formatter Agent ensures consistent, professional formatting of test files according to Markdown standards and project conventions.

---

## Responsibilities

- Apply consistent Markdown formatting
- Structure test sections properly
- Format metadata headers
- Ensure proper heading hierarchy
- Add visual elements (emojis, icons)
- Format answer keys
- Apply regional formatting conventions
- Validate syntax

---

## Inputs

- Test content (questions, answers, metadata)
- Formatting preferences
- Regional conventions
- Age group styling preferences
- Gamification requirements

---

## Outputs

Professionally formatted Markdown file with:
- Complete metadata header
- Properly structured sections
- Consistent formatting throughout
- Visual enhancements
- Valid Markdown syntax

---

## Formatting Standards

### Metadata Header

```markdown
---
title: "Test Title"
subject: Mathematics
country: Germany
bundesland: Bayern
school_type: Gymnasium
klassenstufe: 7
age_range: 12-13
difficulty: Medium
question_count: 10
estimated_time: 30
learning_objectives:
  - Objective 1
  - Objective 2
curriculum_alignment:
  - Standard 1
  - Standard 2
tags: [math, algebra, grade7]
language: de
created_by: Test Designer Agent
date_created: 2025-11-15
version: 1.0
---
```

### Main Title

```markdown
# Test Title

**Grade:** 7  
**Subject:** Mathematics  
**Time:** 30 minutes  
**Total Points:** 50

**Name:** ________________  **Date:** ________
```

### Question Formatting

```markdown
## Question 1 [⭐ Easy - 3 points]

**Question text goes here**

- [ ] A) Option 1
- [ ] B) Option 2
- [ ] C) Option 3
- [ ] D) Option 4

**Topic:** Addition  
**Difficulty:** Easy
```

### Answer Key Formatting

```markdown
---

## 🔑 Answer Key

### Question 1 [3 points]

**Correct Answer:** B

**Explanation:** [Why B is correct]

**Partial Credit:**
- 2 points: Correct method, minor calculation error
- 1 point: Shows understanding of concept

---
```

### Grading Scale Formatting

```markdown
## 📊 Grading Scale

- **45-50 points:** Sehr gut (1) 🌟🌟🌟
- **40-44 points:** Gut (2) ⭐⭐
- **35-39 points:** Befriedigend (3) ⭐
- **30-34 points:** Ausreichend (4) ✓
- **Below 30:** Nicht ausreichend (5-6)
```

---

## Regional Formatting Conventions

### German Tests

**Headers:**
```markdown
# Klassenarbeit: [Topic]
```

**Grading:**
```markdown
## 📊 Bewertung

- **45-50 Punkte:** Sehr gut (1)
- **40-44 Punkte:** Gut (2)
- **35-39 Punkte:** Befriedigend (3)
- **30-34 Punkte:** Ausreichend (4)
- **Unter 30 Punkte:** Nicht ausreichend (5-6)
```

**Answer Key:**
```markdown
## 🔑 Lösungen (Lehrerkopie)
```

### US Tests

**Headers:**
```markdown
# [Topic] Test
```

**Grading:**
```markdown
## 📊 Grading Scale

- **90-100%:** A 🌟🌟🌟
- **80-89%:** B ⭐⭐
- **70-79%:** C ⭐
- **60-69%:** D ✓
- **Below 60%:** F
```

**Answer Key:**
```markdown
## 🔑 Answer Key (Teacher Copy)
```

### UK Tests

**Headers:**
```markdown
# [Topic] Assessment
```

**Grading:**
```markdown
## 📊 Mark Scheme

- **45-50 marks:** Grade 9 🌟🌟🌟
- **40-44 marks:** Grade 7-8 ⭐⭐
- **35-39 marks:** Grade 5-6 ⭐
- **30-34 marks:** Grade 4 ✓
- **Below 30 marks:** Grade 1-3
```

---

## Visual Elements by Age Group

### Ages 6-8 (Grundschule / Elementary)
- **Emojis:** Abundant (🌟⭐🚀🎨📚)
- **Icons:** Colorful, friendly
- **Spacing:** Generous line spacing
- **Font Style:** Large, clear headers
- **Graphics:** Simple, cartoon-style

### Ages 9-11 (Middle Elementary)
- **Emojis:** Moderate (⭐📊🔑💡)
- **Icons:** Fun but less childish
- **Spacing:** Standard
- **Font Style:** Clear, readable
- **Graphics:** Appropriate illustrations

### Ages 12+ (Secondary)
- **Emojis:** Minimal, professional (⭐📊🔑)
- **Icons:** Subtle, informative
- **Spacing:** Compact, efficient
- **Font Style:** Professional
- **Graphics:** Diagrams, charts

---

## Markdown Syntax Validation

### Required Elements
- [ ] Valid YAML metadata header
- [ ] Proper heading hierarchy (H1 → H2 → H3)
- [ ] Consistent list formatting
- [ ] Proper checkbox syntax `- [ ]`
- [ ] No broken links
- [ ] Proper code block formatting
- [ ] Escaped special characters

### Common Fixes
```markdown
# Correct checkbox
- [ ] Option A
- [x] Correct answer

# Correct heading hierarchy
# Main Title
## Section
### Subsection

# Correct emphasis
**Bold text**
*Italic text*

# Correct underline (for PDF generation)
\underline{underlined text}

# Correct lists
1. Ordered item
2. Ordered item

- Unordered item
- Unordered item
```

### Text Formatting for PDF Generation

**IMPORTANT:** For underlined text in PDF output:

- ✅ **Use LaTeX syntax:** `\underline{text to underline}`
- ❌ **Do NOT use HTML tags:** `<u>text</u>` (these are stripped during PDF generation)

**Example:**
```markdown
Identify the underlined word: The teacher praises \underline{the diligent student}.
```

**Rationale:**
- Pandoc converts Markdown to PDF via XeLaTeX
- HTML `<u>` tags are ignored/removed in LaTeX conversion
- Native LaTeX `\underline{}` command renders correctly in PDF
- Works consistently across all PDF generation tools

---

## Formatting Process

```python
def format_test(test_content, preferences):
    """
    Apply consistent formatting to test content
    """
    formatted = {
        'metadata': format_metadata(test_content),
        'header': format_main_header(test_content),
        'instructions': format_instructions(test_content),
        'questions': [],
        'answer_key': format_answer_key(test_content),
        'grading_scale': format_grading_scale(test_content, preferences.region)
    }
    
    # Format each question
    for question in test_content.questions:
        formatted['questions'].append(
            format_question(
                question,
                preferences.age_group,
                preferences.gamification
            )
        )
    
    # Assemble complete file
    return assemble_markdown(formatted)

def format_question(question, age_group, gamification):
    """
    Format individual question with appropriate styling
    """
    # Determine difficulty emoji
    difficulty_emoji = {
        'Easy': '⭐',
        'Medium': '⭐⭐',
        'Hard': '⭐⭐⭐'
    }
    
    # Build question block
    formatted = f"## Question {question.number} "
    formatted += f"[{difficulty_emoji[question.difficulty]} "
    formatted += f"{question.difficulty} - {question.points} points]\n\n"
    formatted += f"**{question.text}**\n\n"
    
    # Add options if multiple choice
    if question.type == 'multiple_choice':
        for option in question.options:
            formatted += f"- [ ] {option}\n"
    
    # Add metadata
    formatted += f"\n**Topic:** {question.topic}  \n"
    formatted += f"**Difficulty:** {question.difficulty}\n"
    
    # Add fun fact if gamification enabled
    if gamification and question.fun_fact:
        formatted += f"\n💡 **Fun Fact:** {question.fun_fact}\n"
    
    formatted += "\n---\n\n"
    
    return formatted
```

---

## Quality Checks

Before finalizing:
- [ ] Metadata complete and valid
- [ ] All headings properly formatted
- [ ] Point values present and correct
- [ ] Checkboxes properly formatted
- [ ] Answer key complete
- [ ] Grading scale included
- [ ] Visual elements appropriate for age
- [ ] Regional conventions followed
- [ ] Markdown syntax valid
- [ ] File structure consistent

---

## Reverse Interviewing Questions

The Formatter Agent may ask:

### If styling preferences unclear:
- "Should I use emojis and gamification elements for this age group?"
- "What level of visual enhancement is appropriate?"

### If regional format unclear:
- "Should I use German grading scale (1-6) or international (A-F)?"

### If spacing preferences unclear:
- "Should I use compact or generous spacing between questions?"

---

## Handover to Next Agent

### Handover to PDF Generator Agent

**When to hand over:**
- ✅ Markdown file is fully formatted and validated
- ✅ All visual elements are properly structured  
- ✅ Metadata is complete and accurate
- ✅ File is saved to `tests/` directory
- ✅ Answer key file is also formatted (if separate)

**What to provide:**

```yaml
handover_to_pdf_generator:
  test_file:
    markdown_path: "tests/germany/niedersachsen/gymnasium/englisch/grade_6/present_simple/klassenarbeit.md"
    test_id: "de-ns-gym-eng-6-tenses-001"
    session_id: "sess_20251115_140000"
  
  answer_key_file:
    markdown_path: "tests/germany/niedersachsen/gymnasium/englisch/grade_6/present_simple/loesung.md"
    
  pdf_generation_options:
    generate_student_version: true
    generate_answer_key: true
    theme: "Default"  # Default | Colorful | Minimal
    page_size: "A4"   # A4 | Letter
    orientation: "Portrait"  # Portrait | Landscape
    
  styling_metadata:
    uses_emojis: true
    uses_tables: true
    uses_checkboxes: true
    color_coding: false
    images_count: 0
    
  regional_settings:
    language: "de"
    grading_scale: "german_1_6"
    decimal_separator: ","
    
  age_appropriateness:
    target_age: 12
    reading_level: "Grade 6"
    visual_complexity: "moderate"
```

**Message to PDF Generator Agent:**

> "@pdf-generator The formatted Markdown test is ready at `{markdown_path}`. Please generate professional PDFs for both student version and answer key. Use the **{theme}** theme on **{page_size}** paper in **{orientation}** orientation. The test includes visual elements (emojis: {uses_emojis}, tables: {uses_tables}) suitable for {target_age}-year-old students. Regional settings: {language} language, {grading_scale} grading scale."

**Quality Checklist Before Handover:**

- [ ] All headings use proper Markdown hierarchy
- [ ] Visual elements render correctly in Markdown preview
- [ ] Checkboxes use proper syntax (- [ ])
- [ ] Tables are properly aligned
- [ ] Code blocks/math notation is correctly formatted
- [ ] No broken emoji characters
- [ ] Metadata header is complete
- [ ] File paths are correctly structured
- [ ] Answer key matches question numbering
- [ ] Point values sum correctly

---

## Related Agents

### Handover to PDF Generator Agent

**When to hand over:**
- Markdown file is fully formatted and validated
- All visual elements are properly structured
- Metadata is complete
- File is saved to `tests/` directory

**What to provide:**
```yaml
handover_to_pdf_generator:
  markdown_file_path: "tests/germany/niedersachsen/gymnasium/englisch/grade_6/present_simple/test.md"
  answer_key_path: "tests/germany/niedersachsen/gymnasium/englisch/grade_6/present_simple/answer_key.md"
  pdf_options:
    generate_student_version: true
    generate_answer_key: true
    theme: "Default" | "Colorful" | "Minimal"
    page_size: "A4" | "Letter"
    orientation: "Portrait" | "Landscape"
  styling_notes:
    - "Uses emojis for visual appeal"
    - "German grading scale included"
    - "Age-appropriate language (12 years old)"
```

**Message to PDF Generator:**
> "@pdf-generator The formatted Markdown test is ready at `{file_path}`. Please generate professional PDFs for both student version and answer key using the Default theme on A4 paper. The test includes visual elements (emojis) suitable for Grade 6 students."

---

## Related Agents

- [Orchestrator Agent](./orchestrator-agent.md)
- [Test Designer Agent](./test-designer-agent.md)
- [PDF Generator Agent](./pdf-generator-agent.md)

---

## See Also

- [Main Specifications](../main-spec.md) - Markdown syntax examples
- [PDF Generation Specifications](../pdf-generation-spec.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
