# Test Designer Agent Specification

[← Back to Main Documentation](../../README.md)

---

## Overview

The Test Designer Agent creates engaging, age-appropriate test questions aligned with curriculum standards and learning objectives.

---

## Responsibilities

- Generate questions using diverse question types
- Align questions with learning objectives
- Create engaging, age-appropriate content
- Include metadata and formatting
- Generate answer keys with explanations
- Incorporate gamification elements
- Ensure appropriate difficulty distribution

---

## Inputs

- Curriculum research output (learning objectives, standards, terminology)
- Number of questions requested
- Difficulty distribution (% easy/medium/hard)
- Question type preferences
- Language (de, en, etc.)
- Age group and grade level
- School type (Gymnasium, Elementary, etc.)
- Gamification preferences

---

## Outputs

Complete test file in Markdown format with:
- Metadata header
- Formatted questions with point values
- Answer key
- Difficulty ratings
- Learning resources
- Gamification elements (badges, points, progress tracking)

---

## Question Type Distribution

Uses diverse formats from the main specification:
- Multiple Choice (MCQ)
- True/False
- Fill in the Blank
- Matching
- Ordering/Sequencing
- Short Answer
- Multiple Select
- Drag & Drop
- Image-Based Questions
- Scenario-Based Questions

---

## Quality Standards

### Content Requirements
- ✅ Factually accurate
- ✅ Age-appropriate language
- ✅ Clear and unambiguous
- ✅ Aligned with learning objectives
- ✅ Curriculum-aligned
- ✅ Bias-free (cultural, gender, socioeconomic)
- ✅ Grammatically correct
- ✅ Uses correct regional terminology

### Format Requirements
- ✅ Consistent Markdown syntax
- ✅ Proper numbering
- ✅ Point values clearly indicated
- ✅ Total points at header
- ✅ Difficulty ratings included
- ✅ Complete metadata header

### Educational Value
- ✅ Tests genuine understanding
- ✅ Encourages critical thinking
- ✅ Provides learning opportunity
- ✅ Appropriate challenge level
- ✅ Real-world connections

---

## Regional Adaptations

### German Tests (de)
- Use formal "Sie" or informal "du" based on grade level
- Employ correct German mathematical terminology
- Follow German punctuation and grammar rules
- Use metric system exclusively
- Include Umlaute (ä, ö, ü) and ß correctly
- Reference Bundesland-specific curricula
- Use German grading scale (1-6)

### US Tests (en-US)
- Use American English spelling
- Follow Common Core Standards
- Reference state-specific curricula when applicable
- Use imperial and metric units
- Letter grades (A-F) or percentages

### UK Tests (en-UK)
- Use British English spelling
- Follow National Curriculum
- Reference Key Stages
- Use metric system
- Letter grades or GCSE numbering

---

## Gamification Elements

### Point Systems
- Clear point values per question
- Bonus points for challenging questions
- Total points displayed
- Grading scales with emojis

### Badges & Achievements
- 🌟 Space Master (90-100%)
- ⭐⭐ Stellar Student (70-89%)
- ⭐ Budding Astronomer (50-69%)
- 🚀 Keep Exploring! (< 50%)

### Visual Elements
- Themed icons (age-appropriate)
- Progress indicators
- Fun facts and learning tips
- Encouraging messages

---

## Example Output Structure

```markdown
---
title: "Linear Equations Practice"
subject: Mathematics
country: Germany
bundesland: Bayern
school_type: Gymnasium
klassenstufe: 7
difficulty: Medium
question_count: 10
estimated_time: 30
learning_objectives: [...]
tags: [mathematik, algebra, klasse7]
language: de
---

# Klassenarbeit: Lineare Gleichungen

**Total Points:** 50

## Question 1 [⭐ Easy - 3 points]
[Question content...]

## Question 2 [⭐⭐ Medium - 5 points]
[Question content...]

---

## 🔑 Answer Key
[Complete solutions...]

---

## 📊 Grading Scale
- **45-50 points:** Sehr gut (1) 🌟🌟🌟
- **40-44 points:** Gut (2) ⭐⭐
[...]
```

---

## Reverse Interviewing Questions

The Test Designer Agent may ask:

### If question count not specified:
- "How many questions would you like in this test?"

### If difficulty distribution unclear:
- "What difficulty distribution would you prefer? (e.g., 30% easy, 50% medium, 20% hard)"

### If question types not specified:
- "Should I use a specific mix of question types, or vary them for engagement?"

### If gamification unclear:
- "Would you like gamification elements (badges, emojis, fun facts)?"
- "What theme would work best for this topic?"

### If formatting preference unclear:
- "Should I include learning tips and fun facts with questions?"
- "Do you want explanations in the answer key?"

---

## Validation

Before finalizing, the Test Designer ensures:
- All learning objectives addressed
- Appropriate difficulty distribution
- Varied question formats
- Correct regional language/terminology
- Complete metadata
- Answer key accuracy
- Point values add up correctly

---

## Related Agents

- [Orchestrator Agent](./orchestrator-agent.md)
- [Curriculum Research Agent](./curriculum-research-agent.md)
- [Content Validator Agent](./content-validator-agent.md)
- [Formatter Agent](./formatter-agent.md)

---

## See Also

- [Main Specifications](../main-spec.md) - Question formats and examples
- [Agent Collaboration Protocol](../agent-collaboration.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
