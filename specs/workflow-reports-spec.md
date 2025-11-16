# Workflow Report Specification

[← Back to Documentation Index](../README.md)

---

## Overview

The Workflow Report feature provides comprehensive, human-readable documentation of every test creation workflow run. Each report captures all 9 agent steps, decisions, metrics, and outputs, creating a complete audit trail for transparency, debugging, and quality assurance.

**Status:** ✅ Implemented (November 2025)

---

## Purpose & Benefits

### Why Workflow Reports?

**Transparency:**
- Makes AI-driven test generation process visible and understandable
- Shows exactly what each agent did and why
- Documents all quality checks and validations

**Auditability:**
- Provides verifiable curriculum alignment evidence
- Tracks all intermediate decisions and iterations
- Creates permanent record for educational administrators

**Quality Assurance:**
- Enables systematic review of test generation quality
- Identifies patterns in agent performance
- Supports continuous improvement of agents

**Debugging:**
- Helps diagnose issues when tests don't meet expectations
- Shows exactly where quality gates passed or failed
- Reveals which agents needed multiple iterations

**Educator Support:**
- Provides context for test usage (prerequisites, time management, differentiation)
- Documents curriculum sources and standards alignment
- Offers specific recommendations for classroom use

---

## Report Structure

### Complete Report Template

See `.agent_workspace/reports/TEMPLATE.md` for the complete structure with all placeholder fields.

### Key Sections

#### 1. Overview
- Test parameters (country, region, school, subject, grade, topic, duration)
- Unique identifiers (test_id, session_id)
- Timestamps (start, end, total duration)

#### 2. Agent Steps (1-9)
Each agent section includes:
- Agent name and version
- Status (SUCCESS/FAILED/ADJUSTED/SKIPPED)
- Input sources (files, parameters)
- Actions performed
- Output files generated
- Key metrics and decisions
- Notes and warnings

#### 3. Final Summary
- Overall workflow status
- Complete file manifest
- Quality metrics table
- Strengths and considerations
- Reusability assessment
- Educator recommendations
- Agent performance statistics

#### 4. Appendix
- Original user request
- Curriculum source citations
- System information
- Report metadata

---

## File Naming & Storage

### Location
```
.agent_workspace/reports/
```

### Naming Convention
```
{test_id}_run_{timestamp}.md
```

**Examples:**
- `de-ns-gym-eng-6-tenses-001_run_2025-11-15T14-00-00.md`
- `us-ca-hs-bio-10-photosynthesis-001_run_2025-11-20T09-30-15.md`
- `uk-en-sec-math-8-quadratics-002_run_2025-12-01T11-45-22.md`

### File Format
- **Format:** Markdown (.md)
- **Encoding:** UTF-8
- **Line endings:** LF (Unix-style)
- **Max size:** ~100 KB (typical)

---

## Report Generation Process

### When Reports Are Created

**Initialization:**
- Orchestrator creates report file immediately after generating test_id and session_id
- Initial report contains Overview section with all known parameters
- Status set to "IN_PROGRESS"

**During Workflow:**
- Orchestrator updates report after each agent completes
- Each update adds the completed agent's section
- Metrics accumulated incrementally

**At Completion:**
- Orchestrator finalizes report with Final Summary
- Overall status set (COMPLETED/COMPLETED_WITH_WARNINGS/FAILED)
- Timestamp updated

### Orchestrator Responsibilities

The Orchestrator agent is responsible for:

1. **Creating** the report file at workflow start
2. **Updating** the report after each agent completes:
   - Collect agent output data
   - Format into report section
   - Append to report file
3. **Finalizing** the report at workflow end:
   - Calculate aggregate metrics
   - Generate recommendations
   - Add summary tables
   - Set final status

### Data Sources

Reports aggregate data from:
- User input (requirements)
- Curriculum research YAML (`.agent_workspace/curriculum_research/`)
- Test draft files (`.agent_workspace/test_drafts/`)
- Validation reports (`.agent_workspace/validation_reports/`)
- Difficulty analysis (`.agent_workspace/difficulty_analysis/`)
- Time estimates (`.agent_workspace/time_estimates/`)
- Agent execution logs
- Final test files (`tests/...`)
- PDF outputs (`pdfs/...`)

---

## Quality Metrics Table

Every report includes a standardized metrics table:

```markdown
| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| Curriculum Alignment | 100% | 100% | ✓ |
| Factual Accuracy | 100% | 100% | ✓ |
| Difficulty Distribution | Easy: 28% / Med: 52% / Hard: 20% | 30/50/20 ±10% | ✓ |
| Time (Average Student) | 40 min | 45 min | ✓ |
| Age-Appropriateness | 98% | 95% | ✓ |
| Clarity | 95% | 90% | ✓ |
| Bias-Free | 100% | 100% | ✓ |
```

**Status Indicators:**
- ✓ = Meets or exceeds target
- ⚠️ = Within acceptable tolerance but close to threshold
- ✗ = Below target (triggers revision)

---

## Agent Performance Tracking

Reports include a performance table showing:

```markdown
| Agent | Duration | Status | Iterations |
|-------|----------|--------|------------|
| Orchestrator | 15s | SUCCESS | 1 |
| Curriculum Fetcher | 8s | SKIPPED | 1 |
| Curriculum Researcher | 45s | SUCCESS | 1 |
| Test Designer | 180s | SUCCESS | 2 |
| Content Validator | 95s | SUCCESS | 1 |
| Difficulty Analyzer | 62s | SUCCESS | 1 |
| Time Estimator | 38s | SUCCESS | 1 |
| Formatter | 72s | SUCCESS | 1 |
| PDF Generator | 35s | PARTIAL | 1 |
```

**Metrics Captured:**
- **Duration:** Time spent by each agent
- **Status:** SUCCESS/FAILED/PARTIAL/SKIPPED/ADJUSTED
- **Iterations:** Number of times agent was invoked (>1 indicates revisions)

---

## Status Values

### Overall Workflow Status

- **COMPLETED** - All agents succeeded, all quality gates passed, all outputs generated
- **COMPLETED_WITH_WARNINGS** - Workflow completed but with minor issues (e.g., PDF generation failed due to missing dependencies)
- **FAILED** - Critical failure prevented workflow completion
- **IN_PROGRESS** - Workflow currently executing (temporary status)

### Agent Step Status

- **SUCCESS** - Agent completed successfully, output meets quality standards
- **FAILED** - Agent encountered error and could not complete
- **ADJUSTED** - Agent completed but required revisions (multiple iterations)
- **SKIPPED** - Agent intentionally skipped (e.g., Curriculum Fetcher when curriculum exists)
- **PARTIAL** - Agent partially completed (e.g., HTML generated but PDF failed)

---

## Example Reports

### Sample Report

See `.agent_workspace/reports/de-ns-gym-eng-6-tenses-001_run_2025-11-15T14-00-00.md` for a complete real-world example documenting the creation of a Grade 6 English test on Present Simple vs. Past Progressive.

**Highlights from Example:**
- Total workflow duration: 42 minutes 30 seconds
- Test Designer required 2 iterations (timing adjustment)
- PDF generation partial (Pandoc not installed)
- All quality metrics exceeded thresholds
- Final status: COMPLETED_WITH_WARNINGS

---

## Use Cases

### 1. Teacher Review
**Scenario:** Teacher wants to understand how test was created

**Report Sections Used:**
- Overview (test parameters)
- Curriculum Researcher (learning objectives covered)
- Difficulty Analyzer (question difficulty breakdown)
- Time Estimator (time recommendations)
- Final Summary (educator notes)

**Value:** Teacher understands curriculum alignment and can make informed adjustments

### 2. Quality Audit
**Scenario:** School administrator verifies test quality standards

**Report Sections Used:**
- Content Validator (validation checks)
- Quality Metrics Table (all thresholds)
- Curriculum Source (official documentation)
- Bias check results

**Value:** Verifiable evidence of quality and curriculum compliance

### 3. Debugging
**Scenario:** Test doesn't match expectations, need to understand why

**Report Sections Used:**
- All agent steps (identify where decisions were made)
- Agent Performance Table (identify slow or failed agents)
- Iterations count (identify which agents needed revisions)
- Warnings and notes

**Value:** Pinpoint exact cause of unexpected output

### 4. Process Improvement
**Scenario:** Want to optimize agent workflow performance

**Report Sections Used:**
- Agent Performance Table (duration, iterations)
- Overall workflow duration
- Agent status (identify frequent failures)

**Value:** Data-driven insights for agent optimization

### 5. Reproducibility
**Scenario:** Need to recreate similar test with same parameters

**Report Sections Used:**
- Overview (all parameters)
- Original user request
- Curriculum source
- Test structure (sections, points, question types)

**Value:** Complete recipe for recreating test

---

## Integration with Existing Workflow

### Before (Without Reports)

```
User → Orchestrator → [8 agents] → Final test files
```

- No visibility into intermediate steps
- Hard to debug issues
- No audit trail

### After (With Reports)

```
User → Orchestrator (creates report) → 
       [Agent 1] → Orchestrator (updates report) →
       [Agent 2] → Orchestrator (updates report) →
       ...
       [Agent 9] → Orchestrator (finalizes report) →
       Final test files + Complete workflow report
```

- Full transparency
- Easy debugging
- Permanent audit trail
- Educator-friendly documentation

---

## Technical Implementation

### Orchestrator Agent Modifications

**New Responsibilities:**

1. **Initialize Report:**
   ```yaml
   report_file: .agent_workspace/reports/{test_id}_run_{timestamp}.md
   status: IN_PROGRESS
   sections: [Overview]
   ```

2. **Update After Each Agent:**
   ```python
   def update_report(agent_name, agent_data):
       - Read current report
       - Append agent section with data
       - Write updated report
   ```

3. **Finalize Report:**
   ```python
   def finalize_report():
       - Calculate aggregate metrics
       - Generate summary tables
       - Add recommendations
       - Set status to COMPLETED/COMPLETED_WITH_WARNINGS/FAILED
   ```

### Report Template System

- **Template:** `.agent_workspace/reports/TEMPLATE.md`
- **Placeholders:** `{test_id}`, `{timestamp}`, `{country}`, etc.
- **Orchestrator** replaces placeholders with actual values

### Data Schema

Report metadata added to `specs/data-schemas.md`:

```yaml
workflow_report:
  file_path: ".agent_workspace/reports/{test_id}_run_{timestamp}.md"
  format: "markdown"
  sections:
    - overview
    - agent_steps (1-9)
    - final_summary
    - appendix
  generated_by: "orchestrator"
  updated_by: "orchestrator"
```

---

## Future Enhancements

### Phase 2 (Potential)

1. **JSON Export:** Generate machine-readable JSON version alongside Markdown
2. **Report Index:** Central index of all workflow reports
3. **Dashboard:** Web-based visualization of metrics across reports
4. **Comparison:** Side-by-side comparison of multiple test runs
5. **Templates:** Multiple report templates for different audiences (technical, educator-focused, admin-focused)
6. **Notifications:** Alert when workflows fail or exceed quality thresholds

### Community Requests

Open to suggestions! Create an issue on GitHub with:
- Use case description
- Desired report section or metric
- Why it would be valuable

---

## Related Documentation

- [Orchestrator Agent Specification](./agents/orchestrator-agent.md)
- [Data Schemas](./data-schemas.md)
- [Main Specification](./main-spec.md)
- [Agent Collaboration Protocol](./agent-collaboration.md)

---

## Changelog

**Version 1.0 (November 2025)**
- Initial implementation
- Template structure defined
- Orchestrator integration
- Sample report created

---

**Version:** 1.0  
**Status:** ✅ Implemented  
**Last Updated:** November 16, 2025
