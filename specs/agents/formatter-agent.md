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

# Correct lists
1. Ordered item
2. Ordered item

- Unordered item
- Unordered item
```

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
