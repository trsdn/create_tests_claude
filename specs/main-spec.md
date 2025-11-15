# Educational Test Creator - Main Specifications

[← Back to Documentation Index](../README.md)

---

## 1. Project Overview

**Project Name:** Educational Test Creator for Kids  
**Purpose:** Create engaging, educational tests in Markdown format for children using GitHub Agent Mode  
**Target Audience:** Children (ages 6-19, adjustable by grade level)  
**Output Formats:** Markdown (.md) files and PDF documents

---

## 2. Educational Research Foundation

### 2.1 Assessment Types

Based on OECD Education Research (2025) and contemporary educational theory:

#### Formative Assessment
- **Purpose:** Continuous learning evaluation to improve student understanding
- **Characteristics:** Low-stakes, feedback-focused, iterative
- **Application:** Regular check-ins, progress monitoring

#### Summative Assessment
- **Purpose:** Evaluate learning at the end of a unit/topic
- **Characteristics:** Higher-stakes, comprehensive coverage
- **Application:** End-of-topic tests, knowledge verification

#### Diagnostic Assessment
- **Purpose:** Identify student strengths, weaknesses, and prior knowledge
- **Characteristics:** Pre-assessment, skill-level identification
- **Application:** Placement tests, learning gap identification

### 2.2 Learning Principles

1. **Active Learning:** Engage students through interactive question formats
2. **Immediate Feedback:** Provide instant learning reinforcement
3. **Differentiated Instruction:** Adapt difficulty based on age/skill level
4. **Authentic Assessment:** Use real-world contexts and meaningful scenarios
5. **Student-Centered Design:** Focus on learner experience and motivation
6. **Social-Emotional Skills:** Include questions that develop critical thinking
7. **Spacing Effect:** Distribute learning over time with varied question types
8. **Desirable Difficulty:** Challenge students appropriately without overwhelming

---

## 3. Question Format Types

### 3.1 Multiple Choice Questions (MCQ)

**Research Basis:** Most common objective assessment type; effective for measuring knowledge recall and comprehension

**Specifications:**
- 3-5 answer options (3-4 for younger kids, 4-5 for older)
- One correct answer
- Distractors should be plausible but clearly incorrect
- Avoid "all of the above" or "none of the above" for younger children

**Example:**
```markdown
**Question 1 [5 points - Easy]:** What is the capital of France?
- [ ] A) London
- [ ] B) Berlin
- [x] C) Paris
- [ ] D) Madrid
```

---

### 3.2 True/False Questions

**Research Basis:** Simple binary choice; good for younger learners and quick assessment

**Specifications:**
- Binary choice (True/False or Yes/No)
- Clear, unambiguous statements
- Mix of true and false answers (avoid patterns)

**Example:**
```markdown
**Question 2 [3 points - Easy]:** True or False: The sun rises in the west.
- [ ] True
- [x] False
```

---

### 3.3 Fill-in-the-Blank

**Research Basis:** Tests recall and understanding without providing answer cues

**Specifications:**
- Single word or short phrase answers
- Clear context clues
- Appropriate difficulty for age group

**Example:**
```markdown
**Question 3 [4 points - Medium]:** The process by which plants make food is called __________.

**Answer:** photosynthesis
```

---

### 3.4 Matching Questions

**Research Basis:** Tests association and relationship understanding

**Specifications:**
- 4-8 items to match
- Clear column headers
- Equal or unequal list lengths (unequal prevents elimination guessing)

**Example:**
```markdown
**Question 4 [6 points - 2 points each - Medium]:** Match the animal with its habitat

**Column A:**
1. Fish
2. Bird
3. Bear

**Column B:**
A) Forest
B) Ocean
C) Sky

**Answers:** 1-B, 2-C, 3-A
```

---

### 3.5 Ordering/Sequencing Questions

**Research Basis:** Assesses understanding of processes, chronology, and logical sequences

**Specifications:**
- 3-6 items to order
- Clear instruction (chronological, size, importance, etc.)
- Numbered or lettered items

**Example:**
```markdown
**Question 5 [8 points - Hard]:** Put these events in the correct order (from first to last):

- [ ] C) Butterfly emerges
- [ ] A) Egg is laid
- [ ] D) Adult butterfly
- [ ] B) Caterpillar hatches

**Correct Order:** A → B → C → D
```

---

### 3.6 Short Answer Questions

**Research Basis:** Higher-order thinking; allows for expression and explanation

**Specifications:**
- 1-3 sentence responses
- Clear question prompt
- Specific rubric for evaluation

**Example:**
```markdown
**Question 6 [10 points - Medium]:** Explain why we have different seasons on Earth. (2-3 sentences)

**Sample Answer:** We have seasons because the Earth is tilted on its axis. As Earth orbits the sun, different parts receive more or less direct sunlight, creating seasonal changes.

**Grading Rubric:**
- Mentions Earth's tilt (4 points)
- Explains orbit around sun (3 points)
- Connects to sunlight variation (3 points)
```

---

### 3.7 Multiple Select Questions

**Research Basis:** Tests comprehensive understanding; more complex than MCQ

**Specifications:**
- Select 2-4 correct answers from 5-7 options
- Clearly state how many answers to select
- Partial credit possible

**Example:**
```markdown
**Question 7 [9 points - 3 points each correct answer - Medium]:** Select ALL the mammals from this list (choose 3):

- [x] A) Dog
- [ ] B) Snake
- [x] C) Whale
- [ ] D) Eagle
- [x] E) Bat
- [ ] F) Frog

**Partial credit:** 1 point deducted for each incorrect selection
```

---

### 3.8 Drag-and-Drop/Interactive

**Research Basis:** Kinesthetic learning; high engagement for digital natives

**Example (Markdown representation):**
```markdown
**Question 8 [12 points - 2 points per item - Medium]:** Categorize these foods:

**Fruits:** [Apple], [Banana]
**Vegetables:** [Carrot], [Broccoli]
**Grains:** [Rice], [Bread]

Items to categorize: Apple, Carrot, Rice, Banana, Broccoli, Bread
```

---

### 3.9 Image-Based Questions

**Research Basis:** Visual literacy; accommodates different learning styles

**Specifications:**
- Clear, high-quality images
- Alt text for accessibility
- Direct connection to curriculum

**Example:**
```markdown
**Question 9 [5 points - Easy]:** Look at the image below. Which type of cloud is shown?

![Cloud Image](images/cumulus_cloud.jpg)

- [ ] A) Cirrus
- [x] B) Cumulus
- [ ] C) Stratus
- [ ] D) Nimbus
```

---

### 3.10 Scenario/Story-Based Questions

**Research Basis:** Authentic assessment; real-world application

**Example:**
```markdown
**Scenario:** Maya has 12 cookies and wants to share them equally among her 4 friends.

**Question 10a [5 points - Easy]:** How many cookies will each friend get?
**Answer:** 3 cookies

**Question 10b [3 points - Easy]:** Will there be any cookies left over?
- [ ] Yes
- [x] No

**Total for Question 10: 8 points**
```

---

## 4. Gamification Elements

### 4.1 Point Systems
- Award points for correct answers
- Bonus points for challenging questions
- Difficulty multipliers (harder questions = more points)

### 4.2 Progress Tracking
- Progress bars
- Level indicators
- Completion badges

### 4.3 Engagement Features
- Fun facts after correct answers
- Encouraging messages
- Theme-based tests (space adventure, jungle exploration, etc.)

### 4.4 Visual Elements
- Emoji rewards 🌟 ⭐ 🏆
- Color-coded difficulty levels
- Achievement unlocks

**Example Implementation:**
```markdown
## 🎮 Test Progress

**Current Level:** 2/5  
**Points Earned:** 75/100  
**Streak:** 3 correct in a row! 🔥

---

## Question 1 [⭐ Easy - 5 points]
...

## Question 5 [⭐⭐⭐ Hard - 15 points]
...
```

---

## 5. Age-Appropriate Design

### 5.1 Age Groups

#### Early Elementary (Ages 6-8, Grades 1-3)
- **Question Types:** True/False, Simple MCQ (3 options), Image-based, Matching
- **Language:** Simple vocabulary, short sentences
- **Length:** 5-10 questions per test
- **Visuals:** Heavy use of images and emojis
- **Topics:** Basic math, colors, animals, simple science

#### Upper Elementary (Ages 9-11, Grades 4-5)
- **Question Types:** MCQ (4 options), Fill-in-blank, Short answer, Ordering
- **Language:** Grade-level vocabulary, clear explanations
- **Length:** 10-15 questions per test
- **Visuals:** Supporting images, diagrams
- **Topics:** Complex math, reading comprehension, science concepts, geography

#### Middle School+ (Ages 12+, Grades 6-13)
- **Question Types:** All types including multiple select, scenario-based, essay-style
- **Language:** Advanced vocabulary, complex sentences
- **Length:** 15-25 questions per test
- **Visuals:** Charts, graphs, detailed diagrams
- **Topics:** Algebra, complex science, critical thinking, analysis

### 5.2 Accessibility Considerations

- Clear, readable fonts (Markdown default)
- Alt text for all images
- Simple language option
- Avoid cultural bias
- Color-blind friendly design
- Logical reading order

---

## 6. Test Metadata Standard

Each test file should include standardized metadata:

```yaml
---
# Basic Information
title: "Test Title"
subject: Mathematics
age_range: 12-13

# Regional Context
country: Germany
region: Bayern
bundesland: Bayern
school_type: Gymnasium
klassenstufe: 7
grade_level: 7

# Test Details
difficulty: Medium
question_count: 12
estimated_time: 30

# Educational Alignment
learning_objectives:
  - "Objective 1"
  - "Objective 2"

curriculum_alignment:
  - "Lehrplan PLUS Bayern"

standards:
  - "KMK Bildungsstandards"

# Metadata
tags: [math, algebra, grade7]
language: de
created_by: Test Designer Agent
date_created: 2025-11-15
version: 1.0
---
```

---

## 7. Quality Standards

### 7.1 Content Requirements
- ✅ Factually accurate
- ✅ Age-appropriate language
- ✅ Clear and unambiguous
- ✅ Aligned with learning objectives
- ✅ Curriculum-aligned
- ✅ Bias-free
- ✅ Grammatically correct
- ✅ Uses correct regional terminology

### 7.2 Format Requirements
- ✅ Consistent Markdown syntax
- ✅ Proper numbering
- ✅ Point values clearly indicated
- ✅ Total points at header
- ✅ Difficulty ratings included
- ✅ Complete metadata header
- ✅ Answer key included

### 7.3 Educational Value
- ✅ Tests genuine understanding
- ✅ Encourages critical thinking
- ✅ Provides learning opportunity
- ✅ Appropriate challenge level
- ✅ Real-world connections

---

## Related Documentation

- [Curriculum & Regional Specifications](./curriculum-regional-spec.md)
- [PDF Generation Specifications](./pdf-generation-spec.md)
- [Repository Organization](./repository-organization.md)
- [Agent Collaboration Protocol](./agent-collaboration.md)
- [All Agent Specifications](./agents/)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
