# Test Run Report – {test_id}

## Overview

- **Country:** {country}
- **State/Region:** {region}
- **School Type:** {school_type}
- **Subject:** {subject}
- **Grade:** {grade}
- **Topic:** {topic}
- **Target Duration:** {duration} minutes
- **Test ID:** {test_id}
- **Session ID:** {session_id}
- **Run Started:** {timestamp_start}
- **Run Completed:** {timestamp_end}
- **Total Duration:** {total_duration}

---

## Step 1 – Orchestrator

- **Agent:** `orchestrator`
- **Status:** {SUCCESS|FAILED|ADJUSTED}
- **Input:**
  - High-level request from user
  - Raw parameters: `{user_request}`
- **Actions:**
  - Parsed parameters (country, state, school type, subject, grade, topic, duration)
  - Validated curriculum file existence
  - Chose curriculum file: `{curriculum_file_path}`
  - Generated test ID: `{test_id}`
  - Created session ID: `{session_id}`
  - Initialized workflow report
- **Output:**
  - Structured test requirements
  - Report file: `{report_file_path}`
- **Notes:** {optional_notes}

---

## Step 2 – Curriculum Fetcher

- **Agent:** `curriculum-fetcher`
- **Status:** {SUCCESS|FAILED|SKIPPED}
- **Input:**
  - Target: {country}, {region}, {school_type}, {subject}, Grade {grade}
  - Required curriculum file: `{curriculum_file_path}`
- **Actions:**
  - Checked if curriculum file exists
  - {If missing: Fetched from official source: `{source_url}`}
  - {If missing: Generated YAML file}
  - Verified curriculum alignment with topic
- **Output:**
  - Curriculum YAML path: `{curriculum_file_path}`
  - Source URL: `{source_url}`
  - Last updated: `{curriculum_last_updated}`
- **Curriculum Metadata:**
  - Learning objectives count: {count}
  - Relevant topics: {topic_list}
- **Notes:** {optional_notes}

---

## Step 3 – Curriculum Researcher

- **Agent:** `curriculum-researcher`
- **Status:** {SUCCESS|FAILED}
- **Input:**
  - Curriculum YAML file: `{curriculum_file_path}`
  - Topic filter: `{topic}`
- **Actions:**
  - Loaded curriculum YAML
  - Extracted learning objectives relevant to topic `{topic}`
  - Identified competency levels (Bloom's taxonomy)
  - Generated curriculum research document
- **Output:**
  - Research file: `.agent_workspace/curriculum_research/{session_id}.yaml`
  - Learning objectives extracted: {count}
  - Competency distribution:
    - Remember/Understand: {percentage}%
    - Apply/Analyze: {percentage}%
    - Evaluate/Create: {percentage}%
- **Curriculum Alignment:** {percentage}%
- **Notes:** {optional_notes}

---

## Step 4 – Test Designer

- **Agent:** `test-designer`
- **Status:** {SUCCESS|FAILED|ADJUSTED}
- **Input:**
  - Curriculum research file: `.agent_workspace/curriculum_research/{session_id}.yaml`
  - Target duration: {duration} minutes
  - Grade level: {grade}
  - Language/region: {region} ({language})
- **Actions:**
  - Generated initial test draft (Markdown)
  - Created {task_count} tasks across {task_type_count} question types
  - Applied regional standards (grading scale, notation, language formality)
- **Output:**
  - Test draft: `.agent_workspace/test_drafts/{test_id}_draft_v1.md`
- **Test Summary:**
  - Total tasks: {task_count}
  - Total points: {total_points}
  - Task types: {task_type_list}
  - Intended difficulty distribution:
    - Easy (⭐): {percentage}% ({count} tasks)
    - Medium (⭐⭐): {percentage}% ({count} tasks)
    - Hard (⭐⭐⭐): {percentage}% ({count} tasks)
  - Bloom's taxonomy coverage: {coverage_summary}
- **Notes:** {optional_notes}

---

## Step 5 – Content Validator

- **Agent:** `content-validator`
- **Status:** {SUCCESS|FAILED|ADJUSTED}
- **Input:**
  - Test draft: `.agent_workspace/test_drafts/{test_id}_draft_v{version}.md`
- **Validation Checks:**
  - **Factual Accuracy:** {score}% (Threshold: 100%)
  - **Clarity:** {score}% (Threshold: 90%)
  - **Bias-Free:** {score}% (Threshold: 100%)
  - **Age-Appropriateness:** {score}% (Threshold: 95%)
  - **Curriculum Alignment:** {score}% (Threshold: 100%)
- **Actions:**
  - Validated all questions against curriculum
  - Checked for factual errors
  - Assessed language clarity for grade level
  - Screened for bias (gender, cultural, socioeconomic)
  - {If issues found: Generated corrected version}
- **Output:**
  - Validation report: `.agent_workspace/validation_reports/{test_id}_validation.yaml`
  - {If adjusted: Updated test draft v{version}}
- **Issues Found:** {count}
  - {List of issues and corrections}
- **Notes:** {optional_notes}

---

## Step 6 – Difficulty Analyzer

- **Agent:** `difficulty-analyzer`
- **Status:** {SUCCESS|FAILED|ADJUSTED}
- **Input:**
  - Test draft: `.agent_workspace/test_drafts/{test_id}_draft_v{version}.md`
- **Actions:**
  - Scored each question on 0-10 difficulty scale
  - Analyzed cognitive complexity
  - Computed overall distribution
  - {If imbalanced: Suggested adjustments}
- **Output:**
  - Difficulty analysis: `.agent_workspace/difficulty_analysis/{test_id}_difficulty.yaml`
- **Difficulty Distribution:**
  - Easy (0-3): {percentage}% ({count} questions) - Target: 30% ±10%
  - Medium (4-6): {percentage}% ({count} questions) - Target: 50% ±10%
  - Hard (7-10): {percentage}% ({count} questions) - Target: 20% ±10%
- **Assessment:** {Within targets | Needs adjustment}
- **Adjustments Made:** {if any}
- **Notes:** {optional_notes}

---

## Step 7 – Time Estimator

- **Agent:** `time-estimator`
- **Status:** {SUCCESS|FAILED|ADJUSTED}
- **Input:**
  - Test draft: `.agent_workspace/test_drafts/{test_id}_draft_v{version}.md`
  - Difficulty analysis: `.agent_workspace/difficulty_analysis/{test_id}_difficulty.yaml`
  - Target duration: {duration} minutes
- **Actions:**
  - Calculated reading time per question
  - Estimated thinking time based on difficulty
  - Estimated writing time for open-ended questions
  - Aggregated for three skill levels
- **Output:**
  - Time estimates: `.agent_workspace/time_estimates/{test_id}_timing.yaml`
- **Time Estimates by Skill Level:**
  - **Below-average students:** {minutes} min ({percentage}% of target)
  - **Average students:** {minutes} min ({percentage}% of target)
  - **Advanced students:** {minutes} min ({percentage}% of target)
- **Assessment:** {Appropriate | Tight but acceptable | Needs adjustment}
- **Recommendation:** {recommendation_text}
- **Notes:** {optional_notes}

---

## Step 8 – Formatter

- **Agent:** `formatter`
- **Status:** {SUCCESS|FAILED}
- **Input:**
  - Final accepted test draft: `.agent_workspace/test_drafts/{test_id}_draft_v{final_version}.md`
  - All validation and analysis metadata
- **Actions:**
  - Applied consistent Markdown formatting
  - Added visual elements (emojis, tables, boxes)
  - Inserted YAML frontmatter with all metadata
  - Applied regional formatting (German notation, grading scale)
  - Added grammar help boxes
  - Ensured proper section structure
- **Output:**
  - Final test Markdown: `tests/{path}/{topic}/klassenarbeit.md`
- **Formatting Applied:**
  - YAML frontmatter: ✓
  - Section headers with emojis: ✓
  - Difficulty indicators (⭐): ✓
  - Grading scale table: ✓
  - Grammar reference boxes: ✓
  - Regional standards (notation, language): ✓
- **Notes:** {optional_notes}

---

## Step 9 – PDF Generator

- **Agent:** `pdf-generator`
- **Status:** {SUCCESS|FAILED|PARTIAL}
- **Input:**
  - Final test Markdown: `tests/{path}/{topic}/klassenarbeit.md`
  - LaTeX template: `templates/{template_name}.tex`
- **Actions:**
  - Converted Markdown to LaTeX
  - Applied regional formatting (German quotes, decimal comma)
  - Generated student version (without answers)
  - Generated answer key version (with solutions)
  - Used Pandoc + LaTeX engine
- **Output:**
  - **Student PDF:** `pdfs/student_versions/{subject}_{topic}_Grade{grade}_Student.pdf`
  - **Answer Key PDF:** `pdfs/answer_keys/{subject}_{topic}_Grade{grade}_Key.pdf`
- **PDF Metadata:**
  - Pages (student version): {page_count}
  - Pages (answer key): {page_count}
  - File size (student): {file_size} KB
  - File size (answer key): {file_size} KB
- **Notes:** {optional_notes}

---

## Final Summary

### Overall Status
**COMPLETED** | COMPLETED_WITH_WARNINGS | FAILED

### Generated Files

**Test Files:**
- Markdown test: `{markdown_test_path}`
- Student PDF: `{student_pdf_path}`
- Answer key PDF: `{answer_key_path}`

**Intermediate Files:**
- Curriculum research: `{curriculum_research_path}`
- Test drafts: `{test_draft_paths}`
- Validation report: `{validation_report_path}`
- Difficulty analysis: `{difficulty_analysis_path}`
- Time estimates: `{time_estimates_path}`

### Key Metrics

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Curriculum Alignment | {percentage}% | 100% | {✓|✗} |
| Factual Accuracy | {percentage}% | 100% | {✓|✗} |
| Difficulty Distribution | Easy: {p}% / Med: {p}% / Hard: {p}% | 30/50/20 ±10% | {✓|✗} |
| Time (Average Student) | {minutes} min | {target} min | {✓|⚠|✗} |
| Age-Appropriateness | {percentage}% | 95% | {✓|✗} |
| Clarity | {percentage}% | 90% | {✓|✗} |
| Bias-Free | {percentage}% | 100% | {✓|✗} |

### Quality Assessment

**Strengths:**
- {strength_1}
- {strength_2}
- {strength_3}

**Areas for Consideration:**
- {consideration_1}
- {consideration_2}

### Recommendations

**Reusability:** {HIGH|MEDIUM|LOW}

**Suggested Variations:**
- {variation_1}
- {variation_2}

**Notes for Educators:**
- {note_1}
- {note_2}

### Agent Performance

| Agent | Duration | Status | Iterations |
|-------|----------|--------|------------|
| Orchestrator | {seconds}s | SUCCESS | 1 |
| Curriculum Fetcher | {seconds}s | {status} | {count} |
| Curriculum Researcher | {seconds}s | {status} | {count} |
| Test Designer | {seconds}s | {status} | {count} |
| Content Validator | {seconds}s | {status} | {count} |
| Difficulty Analyzer | {seconds}s | {status} | {count} |
| Time Estimator | {seconds}s | {status} | {count} |
| Formatter | {seconds}s | {status} | {count} |
| PDF Generator | {seconds}s | {status} | {count} |

**Total Workflow Duration:** {total_duration}

---

## Appendix

### User Request (Original)
```
{original_user_request}
```

### Curriculum Source
- **Official Source:** `{source_url}`
- **Document Title:** {document_title}
- **Last Updated:** {curriculum_last_updated}
- **Fetch Date:** {fetch_date}

### System Information
- **Report Generated:** {report_timestamp}
- **System Version:** {system_version}
- **Orchestrator Version:** {orchestrator_version}

---

*This report was automatically generated by the Educational Test Creator System*  
*Report ID: {report_id} | Session ID: {session_id}*
