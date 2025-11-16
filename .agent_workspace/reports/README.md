# Workflow Reports

This directory contains detailed execution reports for each test creation workflow run.

## Purpose

Each report documents:
- Input parameters (country, region, school type, subject, grade, topic, duration)
- All 9 agent steps with inputs, outputs, and status
- Key metrics (difficulty distribution, time estimates, curriculum alignment)
- Paths to all generated files (Markdown tests, PDFs, YAML files)

## File Naming Convention

```
{test_id}_run_{timestamp}.md
```

Examples:
- `de-ns-gym-eng-6-tenses-001_run_2025-11-16T10-23-00.md`
- `de-bay-gym-math-8-algebra-002_run_2025-11-17T14-15-30.md`

## Report Structure

Each report follows this structure:

1. **Overview** - Test parameters and metadata
2. **Step 1-9** - One section per agent with input/output/status
3. **Final Summary** - Overall status, file paths, recommendations

## Usage

- Generated automatically by the Orchestrator agent during each test creation run
- Can be shared with educators for transparency
- Useful for debugging and quality assurance
- Serves as audit trail for curriculum alignment
