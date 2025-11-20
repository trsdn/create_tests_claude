Validate an existing test draft for quality, accuracy, age-appropriateness, clarity, and bias.

This command runs comprehensive content validation on a test draft without going through the full creation workflow.

**What it does:**
1. Reads test draft from .agent_workspace/test_drafts/
2. Validates factual accuracy (100% required)
3. Checks age-appropriateness (≥95% required)
4. Assesses clarity (≥90% required)
5. Screens for bias (100% bias-free required)
6. Verifies curriculum alignment (100% required)
7. Generates detailed validation report

**Usage:**
```
/validate-test
```

You'll be prompted for:
- Test ID or file path to validate

**Quality Gates:**
- Factual accuracy: 100%
- Age-appropriateness: ≥95%
- Clarity: ≥90%
- Bias-free: 100%
- Curriculum alignment: 100%

**Output:**
- Validation report: `.agent_workspace/validation_reports/{test_id}_validation.yaml`
- Pass/fail status with detailed feedback
- Recommendations for improvements if needed

**Use when:**
- Testing a manually created test
- Verifying test quality before publishing
- Checking test after manual edits
- Running spot checks on existing tests

**Time:** 3-5 minutes
