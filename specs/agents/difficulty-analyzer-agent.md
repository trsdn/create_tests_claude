# Difficulty Analyzer Agent Specification

[← Back to Main Documentation](../../README.md)

---

## Overview

The Difficulty Analyzer Agent assesses question difficulty, ensures appropriate balance, and suggests adjustments to maintain suitable challenge levels for the target audience.

---

## Responsibilities

- Assess individual question difficulty
- Balance overall test complexity
- Suggest difficulty adjustments
- Tag questions by difficulty level
- Ensure appropriate distribution
- Consider school type and grade level
- Validate against regional standards

---

## Inputs

- Test questions (draft or final)
- Target grade level / Klassenstufe
- School type (Gymnasium, Realschule, Elementary, etc.)
- Student skill level (below average, average, advanced)
- Desired difficulty distribution (e.g., 30% easy, 50% medium, 20% hard)
- Curriculum complexity indicators

---

## Outputs

```yaml
difficulty_analysis:
  overall_difficulty: "Medium"
  
  distribution:
    easy: 3 questions (30%)
    medium: 5 questions (50%)
    hard: 2 questions (20%)
  
  target_distribution:
    easy: 30%
    medium: 50%
    hard: 20%
  
  needs_adjustment: false
  
  per_question_analysis:
    - question_id: 1
      difficulty: "Easy"
      factors:
        - "Single-step calculation"
        - "Basic vocabulary"
        - "Clear question"
      confidence: 0.95
    
    - question_id: 2
      difficulty: "Medium"
      factors:
        - "Multi-step problem"
        - "Requires application"
        - "Some inference needed"
      confidence: 0.88
  
  recommendations:
    - "Distribution matches target - no changes needed"
    - "Question 5 may be too difficult for below-average students"
    - "Consider adding one more easy question for confidence building"
```

---

## Difficulty Assessment Criteria

### Easy Questions
- Single-step solutions
- Direct recall or recognition
- Clear, straightforward wording
- Basic vocabulary
- Minimal inference required
- Similar to practiced examples

### Medium Questions
- Multi-step solutions
- Application of concepts
- Some analysis or reasoning required
- Grade-appropriate vocabulary
- Minor inference or connection-making
- Variation from practiced examples

### Hard Questions
- Complex multi-step solutions
- Synthesis of multiple concepts
- Critical thinking required
- Advanced vocabulary
- Significant inference or analysis
- Novel problem formats
- Transfer to new contexts

---

## Difficulty Factors

### Cognitive Complexity
- Bloom's Taxonomy level (Remember → Create)
- Number of steps required
- Amount of inference needed
- Abstraction level

### Linguistic Complexity
- Vocabulary difficulty
- Sentence structure complexity
- Reading level
- Ambiguity in wording

### Content Complexity
- Number of concepts involved
- Prior knowledge required
- Novelty of problem format
- Real-world context complexity

### School Type Considerations
- **Gymnasium:** Can handle more abstraction, multi-step problems
- **Realschule:** Focus on application, practical problems
- **Hauptschule:** Emphasize concrete, foundational concepts
- **Grundschule:** Simple language, single concepts

---

## Difficulty Analysis Algorithm

```python
def analyze_difficulty(question, grade_level, school_type):
    """
    Assess question difficulty based on multiple factors
    """
    difficulty_score = 0
    factors = []
    
    # Cognitive complexity (0-3 points)
    blooms_level = assess_blooms_taxonomy(question)
    difficulty_score += blooms_level * 0.3
    factors.append(f"Bloom's level: {blooms_level}")
    
    # Steps required (0-3 points)
    steps = count_solution_steps(question)
    difficulty_score += min(steps / 2, 3) * 0.3
    factors.append(f"{steps} steps required")
    
    # Vocabulary complexity (0-3 points)
    vocab_score = assess_vocabulary_difficulty(question, grade_level)
    difficulty_score += vocab_score * 0.2
    factors.append(f"Vocabulary: {vocab_score}/3")
    
    # Prior knowledge required (0-3 points)
    prereq_score = assess_prerequisites(question)
    difficulty_score += prereq_score * 0.2
    factors.append(f"Prerequisites: {prereq_score}/3")
    
    # Adjust for school type
    school_adjustment = {
        'Grundschule': -0.5,
        'Hauptschule': -0.3,
        'Realschule': 0.0,
        'Gymnasium': +0.3,
        'Elementary': -0.5,
        'Middle': -0.2,
        'High': 0.0
    }
    difficulty_score += school_adjustment.get(school_type, 0)
    
    # Classify difficulty
    if difficulty_score < 2.0:
        difficulty = "Easy"
    elif difficulty_score < 4.0:
        difficulty = "Medium"
    else:
        difficulty = "Hard"
    
    return {
        'difficulty': difficulty,
        'score': difficulty_score,
        'factors': factors,
        'confidence': calculate_confidence(factors)
    }
```

---

## Distribution Balancing

### Recommended Distributions by Purpose

**Practice/Homework:**
- Easy: 40%
- Medium: 40%
- Hard: 20%

**Regular Assessment:**
- Easy: 30%
- Medium: 50%
- Hard: 20%

**Advanced/Challenge Test:**
- Easy: 20%
- Medium: 40%
- Hard: 40%

**Remedial/Support:**
- Easy: 60%
- Medium: 30%
- Hard: 10%

---

## Adjustment Strategies

### If Too Many Easy Questions
1. Increase complexity of some easy questions
2. Add challenging scenarios
3. Require more detailed explanations
4. Introduce multi-step problems

### If Too Many Hard Questions
1. Simplify wording
2. Provide more context/scaffolding
3. Break complex questions into parts
4. Add easier warm-up questions

### If Unbalanced Distribution
1. Replace questions in over-represented categories
2. Modify difficulty of borderline questions
3. Add new questions to under-represented categories

---

## Reverse Interviewing Questions

The Difficulty Analyzer Agent may ask:

### If target difficulty unclear:
- "What difficulty distribution would you prefer for this test?"
- "Is this for practice, regular assessment, or advanced challenge?"

### If skill level unclear:
- "Should this be suitable for below-average, average, or advanced students?"
- "What percentage of students should be able to score 80%+"

### If distribution needs adjustment:
- "I found 60% hard questions. Should I reduce difficulty or is this intentional?"

---

## Validation

Before finalizing difficulty analysis:
- [ ] All questions analyzed
- [ ] Distribution calculated
- [ ] Compared to target distribution
- [ ] School type considered
- [ ] Grade level appropriate
- [ ] Recommendations provided

---

## Related Agents

- [Orchestrator Agent](./orchestrator-agent.md)
- [Test Designer Agent](./test-designer-agent.md)
- [Time Estimation Agent](./time-estimator-agent.md)

---

## See Also

- [Main Specifications](../main-spec.md) - Question formats
- [Success Metrics](../success-metrics.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
