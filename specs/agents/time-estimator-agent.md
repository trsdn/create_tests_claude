# Time Estimation Agent Specification

[← Back to Main Documentation](../../README.md)

---

## Overview

The Time Estimation Agent calculates realistic time estimates for test completion, validates time feasibility based on difficulty and skill level, and recommends adjustments if time constraints are violated.

---

## Responsibilities

- Calculate realistic time estimates for test completion
- Validate time feasibility based on difficulty and skill level
- Adjust question count or complexity if time constraints violated
- Provide per-question time allocation
- Account for different student skill levels
- Consider age-appropriate concentration spans

---

## Inputs

- Test questions with difficulty ratings
- Grade level / Klassenstufe
- School type (Gymnasium, Realschule, Elementary, etc.)
- Student skill level (below average, average, advanced)
- Target test duration
- Question types and formats

---

## Outputs

```yaml
time_estimate:
  total_time:
    minimum: 25 minutes
    average: 30 minutes
    maximum: 40 minutes
  
  per_question:
    - question_id: 1
      estimated_time: 1.2 minutes
      type: "multiple_choice"
      difficulty: "easy"
    - question_id: 2
      estimated_time: 3.5 minutes
      type: "short_answer"
      difficulty: "medium"
  
  feasibility:
    is_feasible: true
    concentration_span_ok: true
    buffer_time: 15%
  
  recommendations:
    - "Test duration is appropriate for age group"
    - "Consider adding a 5-minute break if test exceeds 45 minutes"
  
  skill_level_breakdown:
    below_average: 45 minutes
    average: 30 minutes
    advanced: 22 minutes
```

---

## Time Estimation Formula

### Base Time by Question Type (in minutes)

```python
base_times = {
    'multiple_choice': 1.0,
    'true_false': 0.5,
    'fill_blank': 1.5,
    'matching': 2.0,
    'ordering': 2.0,
    'short_answer': 3.0,
    'multiple_select': 1.5,
    'drag_drop': 2.0,
    'image_based': 1.5,
    'scenario': 4.0
}
```

### Difficulty Multipliers

```python
difficulty_multipliers = {
    'easy': 0.8,
    'medium': 1.0,
    'hard': 1.5
}
```

### School Type Multipliers

```python
school_multipliers = {
    'Grundschule': 1.5,
    'Hauptschule': 1.3,
    'Realschule': 1.1,
    'Gymnasium': 1.0,
    'Elementary': 1.5,
    'Middle': 1.2,
    'High': 1.0
}
```

### Skill Level Multipliers

```python
skill_multipliers = {
    'below_average': 1.5,
    'average': 1.0,
    'advanced': 0.75
}
```

### Reading Speed (words per minute)

```python
reading_speed = {
    'Grundschule': 80,
    'Elementary': 80,
    'Middle': 120,
    'Gymnasium': 150,
    'Realschule': 130,
    'High': 150
}
```

### Complete Calculation

```python
def calculate_time(questions, school_type, skill_level):
    total_time = 0
    
    for question in questions:
        # Base time
        base = base_times[question.type]
        
        # Apply multipliers
        time = (base * 
                difficulty_multipliers[question.difficulty] * 
                school_multipliers[school_type] *
                skill_multipliers[skill_level])
        
        # Add reading time for scenario questions
        if question.context_words > 0:
            reading_time = question.context_words / reading_speed[school_type]
            time += reading_time
        
        total_time += time
    
    # Add buffer time (10-15%)
    total_with_buffer = total_time * 1.15
    
    return {
        'minimum': total_time * skill_multipliers['advanced'],
        'average': total_time,
        'maximum': total_time * skill_multipliers['below_average'],
        'with_buffer': total_with_buffer
    }
```

---

## Validation Rules

### Maximum Concentration Span by Age

- **Ages 6-8:** 20-25 minutes
- **Ages 9-11:** 30-40 minutes
- **Ages 12-14:** 45-60 minutes
- **Ages 15+:** 60-90 minutes

### Recommendations

- Recommend breaks for tests > 45 minutes
- Flag if estimated time exceeds target by >20%
- Suggest question reduction if too long
- Suggest difficulty adjustment if too short

---

## Feasibility Assessment

```python
def assess_feasibility(time_estimate, target_duration, age_group):
    """
    Determine if test duration is feasible
    """
    max_concentration = get_max_concentration(age_group)
    
    if time_estimate.average > max_concentration:
        return {
            'is_feasible': False,
            'reason': f"Test duration ({time_estimate.average}min) exceeds concentration span ({max_concentration}min)",
            'recommendation': "Reduce question count or split into multiple sections"
        }
    
    if time_estimate.average > target_duration * 1.2:
        return {
            'is_feasible': False,
            'reason': f"Test duration ({time_estimate.average}min) exceeds target ({target_duration}min) by >20%",
            'recommendation': "Remove questions or reduce difficulty"
        }
    
    if time_estimate.average < target_duration * 0.6:
        return {
            'is_feasible': True,
            'warning': f"Test may be too short ({time_estimate.average}min vs {target_duration}min)",
            'recommendation': "Consider adding more questions or increasing difficulty"
        }
    
    return {
        'is_feasible': True,
        'reason': "Test duration is appropriate"
    }
```

---

## Example Calculation

**Input:**
- 10 multiple choice questions (medium difficulty)
- Grade 7 Gymnasium students
- Average skill level
- Target: 30 minutes

**Calculation:**
```
Base time: 10 questions × 1.0 min = 10 minutes
Difficulty multiplier: 10 × 1.0 (medium) = 10 minutes
School type multiplier: 10 × 1.0 (Gymnasium) = 10 minutes
Skill level multiplier: 10 × 1.0 (average) = 10 minutes
Buffer (15%): 10 × 1.15 = 11.5 minutes
```

**Output:**
- Minimum (advanced): 7.5 minutes
- Average: 10 minutes
- Maximum (below average): 15 minutes
- With buffer: 11.5 minutes
- **Feasible:** ✓ Yes (within 30-minute target)

---

## Reverse Interviewing Questions

The Time Estimation Agent may ask:

### If target duration unclear:
- "How much time should students have to complete this test?"
- "Is this a timed test or can students work at their own pace?"

### If skill level distribution unknown:
- "What is the expected skill level distribution in the class?"
- "Should I optimize for average students or below-average?"

### If breaks not specified:
- "Should I account for breaks in longer tests?"
- "Are bathroom breaks allowed during the test?"

### If time pressure unclear:
- "How strict is the time limit?"
- "What happens if students don't finish in time?"

---

## Adjustment Strategies

### If Test Too Long

1. **Reduce question count** - Remove lowest-priority questions
2. **Simplify questions** - Reduce difficulty of some questions
3. **Remove scenario questions** - Replace with simpler formats
4. **Split into sections** - Break into multiple test sessions

### If Test Too Short

1. **Add more questions** - Include additional practice questions
2. **Increase difficulty** - Make some questions more challenging
3. **Add scenario questions** - Include more complex problem-solving
4. **Add open-ended questions** - Require more detailed responses

---

## Related Agents

- [Orchestrator Agent](./orchestrator-agent.md)
- [Test Designer Agent](./test-designer-agent.md)
- [Difficulty Analyzer Agent](./difficulty-analyzer-agent.md)

---

## See Also

- [Main Specifications](../main-spec.md)
- [Agent Collaboration Protocol](../agent-collaboration.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
