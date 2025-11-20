Launch the orchestrator agent to create a complete educational test through the full workflow pipeline (curriculum fetch → research → design → validate → format → PDF generation).

This command initiates the main test creation workflow with quality gates, revision loops, and comprehensive audit trails.

**What it does:**
1. Gathers test requirements (country, region, school, subject, grade, topic)
2. Coordinates all 9 specialized agents
3. Enforces quality gates (accuracy, difficulty distribution, time feasibility)
4. Manages revision loops when quality issues detected
5. Generates final Markdown and PDF test files
6. Provides workflow report with complete audit trail

**Usage:**
```
/create-test
```

The orchestrator will ask for any missing requirements through interactive questions.

**Example:**
```
/create-test

# Orchestrator will ask:
# 1. Country/Region?
# 2. School type?
# 3. Subject and grade?
# 4. Specific topic?
# 5. Test preferences (optional)
```

**Output Files:**
- Student test (MD + PDF): `tests/{country}/{region}/{school}/{subject}/{grade}/{topic}/`
- Answer key (MD + PDF): Same location
- Workflow report: `.agent_workspace/reports/{test_id}_run_{timestamp}.md`
- Agent logs: `.agent_workspace/orchestrator_logs/{session_id}.log`

**Quality Standards:**
- Factual accuracy: 100%
- Curriculum alignment: 100%
- Difficulty distribution: 30% easy, 50% medium, 20% hard
- All content age-appropriate and bias-free

**Time:** Typically 5-10 minutes for complete workflow (varies by complexity)
