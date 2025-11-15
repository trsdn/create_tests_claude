# Content Validator Agent Specification

[← Back to Main Documentation](../../README.md)

---

## Overview

The Content Validator Agent reviews generated test questions to ensure accuracy, appropriateness, clarity, and alignment with curriculum standards.

---

## Responsibilities

- Verify factual accuracy of all content
- Check age-appropriateness of language and concepts
- Ensure question clarity and unambiguity
- Detect and eliminate bias
- Validate curriculum alignment
- Check Markdown formatting
- Verify answer key correctness
- Validate point values

---

## Inputs

- Test draft (Markdown file)
- Curriculum research data
- Learning objectives
- Target age group and grade level
- School type
- Regional/cultural context

---

## Outputs

```yaml
validation_report:
  overall_status: "PASS" | "NEEDS_REVISION"
  
  accuracy_check:
    status: "PASS"
    issues: []
  
  age_appropriateness:
    status: "PASS"
    issues: []
  
  clarity_check:
    status: "NEEDS_REVISION"
    issues:
      - question_id: 3
        issue: "Ambiguous wording in option B"
        suggestion: "Rephrase to clarify meaning"
  
  bias_check:
    status: "PASS"
    cultural_bias: false
    gender_bias: false
    socioeconomic_bias: false
  
  curriculum_alignment:
    status: "PASS"
    objectives_covered: [1, 2, 3, 4]
    missing_objectives: []
  
  format_check:
    status: "PASS"
    markdown_valid: true
    structure_consistent: true
    metadata_complete: true
  
  answer_key:
    status: "PASS"
    all_correct: true
    explanations_clear: true
  
  recommendations:
    - "Consider adding more visual elements for younger students"
    - "Question 7 could benefit from a real-world example"
```

---

## Validation Checklist

### Accuracy Check
- [ ] All facts are correct
- [ ] Answers are accurate
- [ ] Scientific/mathematical concepts are sound
- [ ] No outdated information
- [ ] Sources reliable (when applicable)

### Age-Appropriateness
- [ ] Language matches grade level
- [ ] Vocabulary appropriate
- [ ] Concepts developmentally suitable
- [ ] Complexity appropriate for school type
- [ ] Sentence structure clear

### Clarity Check
- [ ] Questions are unambiguous
- [ ] Instructions are clear in target language
- [ ] Answer options are distinct
- [ ] No trick questions (unless intended)
- [ ] Regional terminology used correctly
- [ ] Mathematical notation correct

### Bias Check
- [ ] No cultural bias
- [ ] No gender bias
- [ ] No socioeconomic assumptions
- [ ] Inclusive examples
- [ ] Culturally appropriate for region
- [ ] Names reflect local demographics
- [ ] Scenarios accessible to all students

### Curriculum Alignment
- [ ] Matches learning objectives
- [ ] Follows official standards
- [ ] Appropriate for school type
- [ ] Correct competency level
- [ ] Prerequisites reasonable
- [ ] Content scope accurate

### Format Check
- [ ] Markdown syntax correct
- [ ] Consistent structure
- [ ] Complete answer key
- [ ] Point values present
- [ ] Metadata complete
- [ ] Proper numbering
- [ ] Headers formatted correctly

### Answer Key Validation
- [ ] All answers correct
- [ ] Explanations clear
- [ ] No ambiguous solutions
- [ ] Partial credit criteria defined (where applicable)
- [ ] Points add up correctly

---

## Validation Process

```python
def validate_test(test_draft, curriculum_data):
    """
    Comprehensive test validation
    """
    validation_report = {
        'overall_status': 'PASS',
        'issues': [],
        'warnings': []
    }
    
    # 1. Accuracy Check
    accuracy_issues = check_factual_accuracy(test_draft)
    if accuracy_issues:
        validation_report['issues'].extend(accuracy_issues)
        validation_report['overall_status'] = 'NEEDS_REVISION'
    
    # 2. Age-Appropriateness
    age_issues = check_age_appropriateness(
        test_draft,
        target_age=curriculum_data.age_range
    )
    if age_issues:
        validation_report['issues'].extend(age_issues)
    
    # 3. Clarity Check
    clarity_issues = check_clarity(test_draft)
    if clarity_issues:
        validation_report['issues'].extend(clarity_issues)
    
    # 4. Bias Check
    bias_issues = check_bias(test_draft, region=curriculum_data.region)
    if bias_issues:
        validation_report['issues'].extend(bias_issues)
        validation_report['overall_status'] = 'NEEDS_REVISION'
    
    # 5. Curriculum Alignment
    alignment = check_curriculum_alignment(
        test_draft,
        learning_objectives=curriculum_data.learning_objectives
    )
    if not alignment['complete']:
        validation_report['warnings'].append(
            f"Missing objectives: {alignment['missing']}"
        )
    
    # 6. Format Check
    format_issues = check_markdown_format(test_draft)
    if format_issues:
        validation_report['issues'].extend(format_issues)
    
    # 7. Answer Key Validation
    answer_issues = validate_answer_key(test_draft)
    if answer_issues:
        validation_report['issues'].extend(answer_issues)
        validation_report['overall_status'] = 'NEEDS_REVISION'
    
    return validation_report
```

---

## Issue Severity Levels

### Critical (Must Fix)
- Factual errors
- Incorrect answers
- Bias or discrimination
- Curriculum misalignment
- Broken Markdown syntax

### Major (Should Fix)
- Unclear questions
- Age-inappropriate language
- Missing learning objectives
- Incomplete answer explanations

### Minor (Nice to Fix)
- Stylistic improvements
- Additional context suggestions
- Enhanced visual elements
- Better example choices

---

## Reverse Interviewing Questions

The Content Validator Agent may ask:

### If validation fails:
- "Question X has a factual error. Should I suggest a correction or flag for manual review?"
- "The language in Question Y may be too advanced. Should I recommend simplification?"

### If bias detected:
- "I detected potential cultural bias in Question Z. Should I suggest an alternative scenario?"

### If curriculum alignment questionable:
- "This test doesn't cover learning objective [X]. Should I recommend adding a question?"

---

## Related Agents

- [Orchestrator Agent](./orchestrator-agent.md)
- [Test Designer Agent](./test-designer-agent.md)
- [Curriculum Research Agent](./curriculum-research-agent.md)

---

## See Also

- [Main Specifications](../main-spec.md) - Quality standards
- [Success Metrics](../success-metrics.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
