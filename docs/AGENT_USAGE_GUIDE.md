# Agent Usage Guide - Best Practices

## ⚠️ Critical Rules for Using Agents

### Rule #1: Use Natural Language Requests

❌ **DON'T DO THIS:**
```
Run test-designer for grade 7
Check this test with content-validator
Analyze difficulty manually
```

✅ **DO THIS:**
```
Create a math test for grade 7 with linear equations
```

**Why?**
- Claude automatically orchestrates all agents in correct order
- Quality gates are enforced
- No steps are accidentally skipped
- Complete workflow tracking and reporting

---

## Rule #2: Trust the Automated Workflow

The system automatically runs all agents in sequence. **Let Claude coordinate the workflow!**

**Automatic Workflow:**
```
You: Create a test for Gymnasium Grade 7 Math (Linear Equations)

↓ (Claude orchestrates requirements gathering)
↓ (Curriculum Fetcher retrieves official curriculum)
↓ (Curriculum Researcher extracts learning objectives)
↓ (Test Designer creates questions)
↓ (Content Validator checks quality)
↓ (Difficulty Analyzer checks distribution)
↓ (Time Estimator calculates time)
↓ (Formatter applies final formatting)
↓ (PDF Generator creates PDFs)
↓ (Workflow report generated)

Orchestrator: ✅ Test complete! Here are your files...
```

**Total time:** ~5-10 minutes (fully automated)

---

## Rule #3: If Workflow Stalls, Check for Missing Handoffs

**Symptoms of Broken Workflow:**
- Agent finishes but nothing happens
- You receive partial output (only Markdown, no PDF)
- Missing quality reports (no difficulty analysis, no time estimates)
- Agent delivers "final" result but it's incomplete

**Recovery Steps:**

1. **Ask Orchestrator to resume:**
   ```
   @orchestrator The workflow stalled at {agent-name}. Please resume from there.
   ```

2. **Provide context:**
   ```
   @orchestrator Resume test creation for session sess_20251115_103045
   Last completed agent: test-designer
   Missing: validation, difficulty analysis, time estimation, formatting, PDF
   ```

3. **Orchestrator will detect the gap and manually invoke the missing agents**

---

## Rule #4: Understand Revision Loops

**Scenario:** Difficulty Analyzer finds test is too easy (50% easy, 40% medium, 10% hard)

**What SHOULD happen:**
```
Difficulty Analyzer → Test Designer (with feedback: "make Q2, Q4, Q7 harder")
  ↓
Test Designer v2 → Content Validator (re-validate revised questions!)
  ↓
Content Validator → Difficulty Analyzer (re-check distribution)
  ↓
Difficulty Analyzer → Time Estimator (distribution now correct: 30/50/20)
  ↓
... continues normally
```

**What MIGHT happen if handoffs fail:**
```
Difficulty Analyzer → Test Designer (adjust difficulty)
Test Designer v2 → ❌ STOPS (doesn't hand off to Content Validator!)

Result: Revised test is never validated, might have new errors!
```

**Your Action:**
```
@orchestrator I see test-designer created v2 but didn't hand off to content-validator. Please continue the workflow.
```

---

## Rule #5: Each Agent Has Mandatory Handoff Warnings

Every agent definition now includes a **⚠️ CRITICAL: Mandatory Handoff Protocol** section at the end.

**What this does:**
- Reminds the agent to ALWAYS hand off to the next agent
- Lists specific handoff buttons to click
- Provides verification checklist
- Explains WHY handoffs are mandatory

**Example (from Test Designer):**
```markdown
## ⚠️ CRITICAL: Mandatory Handoff Protocol

**NEVER finish your work without handing off to the next agent!**

### After Initial Test Creation:
✅ **MUST** hand off to **Content Validator** (use "Validate Content" button)
❌ **NEVER** deliver test directly to user
❌ **NEVER** skip validation

### Verification Checklist Before Handoff:
- [ ] Test draft saved to `.agent_workspace/test_drafts/`
- [ ] Answer key created
- [ ] Metadata YAML file created
- [ ] Handoff button clicked
```

---

## Rule #6: Monitor Agent Output for Handoff Confirmation

**Good Agent Output (includes handoff):**
```
Test Designer:
✅ Created test draft v1 with 10 questions
✅ Generated answer key with grading rubrics
✅ Saved to .agent_workspace/test_drafts/de-by-gym-math-7-algebra-001_draft_v1.md
✅ Handing off to Content Validator for validation...

[Handoff to Content Validator]
```

**Bad Agent Output (missing handoff):**
```
Test Designer:
✅ Created test draft v1 with 10 questions
✅ Generated answer key

Here's your test! [shows test content]
```

**If you see the bad pattern, immediately invoke Orchestrator:**
```
@orchestrator test-designer didn't hand off to content-validator. Please continue workflow.
```

---

## Rule #7: Orchestrator Can Recover from Broken Workflows

The Orchestrator has built-in **Handoff Monitoring** and **Recovery Protocol**:

**Detection:**
- Orchestrator tracks expected workflow sequence
- If an agent finishes without handoff, Orchestrator detects the gap

**Warning:**
```markdown
⚠️ **WORKFLOW INTERRUPTION DETECTED**

Agent **test-designer** completed their work but did NOT hand off to the next agent.

**Expected next step:** content-validator
**Current status:** STALLED

**Action Required:**
I will now manually invoke the next agent with the correct context.
```

**Recovery:**
- Orchestrator manually invokes the missing agent
- Provides correct file paths and context
- Resumes workflow from correct position

---

## Quick Reference: When to Use Which Agent

| Scenario | Command |
|----------|---------|
| **Create new test** | `@orchestrator create test for {details}` |
| **Resume stalled workflow** | `@orchestrator resume from {agent-name}` |
| **Check workflow status** | `@orchestrator show status for session {id}` |
| **Manually invoke specific agent** | ⚠️ **DON'T!** Use Orchestrator instead |
| **Debug workflow issue** | `@orchestrator diagnose workflow for test {id}` |

---

## Common Mistakes to Avoid

### ❌ Mistake #1: Invoking agents directly
```
@test-designer create a math test
```
**Problem:** Skips curriculum research, validation, difficulty analysis, time estimation, formatting, PDF generation

### ❌ Mistake #2: Accepting incomplete output
```
Test Designer: Here's your test! [delivers Markdown only]
You: Thanks! [stops here]
```
**Problem:** Missing validation, difficulty check, time estimation, formatting, PDF

### ❌ Mistake #3: Not checking for handoff completion
**Problem:** Agent might finish but not hand off, workflow stalls

### ❌ Mistake #4: Trying to fix issues yourself
```
Test Designer creates test → You manually edit Markdown → Upload
```
**Problem:** Bypasses validation, difficulty analysis, time estimation

---

## ✅ Best Practice Summary

1. **ALWAYS** start with `@orchestrator`
2. **NEVER** invoke agents directly (unless debugging)
3. **WAIT** for complete workflow (all 9 agents)
4. **VERIFY** each agent hands off to the next
5. **USE** Orchestrator to recover from stalled workflows
6. **TRUST** the revision loops (they re-validate!)
7. **CHECK** final output includes:
   - Markdown test file
   - Markdown answer key
   - PDF student version
   - PDF answer key
   - Workflow report (in `.agent_workspace/reports/`)

---

## Example: Perfect Workflow Execution

```bash
# Start with Orchestrator
You: @orchestrator Create a math test for Gymnasium Grade 7 in Bayern
     Topic: Linear Equations
     Duration: 30 minutes
     Difficulty: Medium

# Orchestrator gathers any missing details
Orchestrator: I have all the details. Starting test creation...

# Curriculum Research
Orchestrator → Curriculum Researcher
Curriculum Researcher: ✅ Extracted 6 learning objectives from Bayern curriculum
                       → Handing off to Test Designer

# Test Design
Test Designer: ✅ Created 10 questions (30% easy, 50% medium, 20% hard)
               ✅ Generated complete answer key
               → Handing off to Content Validator

# Validation
Content Validator: ✅ Factual accuracy: 100%
                   ✅ Age-appropriateness: 100%
                   ✅ Clarity: 95%
                   ✅ No bias detected
                   → Handing off to Difficulty Analyzer

# Difficulty Analysis
Difficulty Analyzer: ✅ Distribution: Easy 30%, Medium 50%, Hard 20%
                     ✅ Meets target (±10% tolerance)
                     → Handing off to Time Estimator

# Time Estimation
Time Estimator: ✅ Average students: 28 minutes
                ✅ Below-average: 32 minutes
                ✅ Fits 30-minute target
                → Handing off to Formatter

# Formatting
Formatter: ✅ Applied Markdown formatting
           ✅ Added visual elements (⭐ difficulty stars, 📊 icons)
           ✅ Saved to tests/germany/bayern/gymnasium/mathematik/klasse_7/
           → Handing off to PDF Generator

# PDF Generation
PDF Generator: ✅ Student PDF created
               ✅ Answer key PDF created
               → Handing off to Orchestrator

# Final Delivery
Orchestrator: ✅ Test creation complete!

📄 **Files Created:**
- Markdown Test: tests/germany/bayern/gymnasium/mathematik/klasse_7/lineare_gleichungen.md
- Markdown Key: tests/germany/bayern/gymnasium/mathematik/klasse_7/lineare_gleichungen_key.md
- PDF Test: tests/germany/bayern/gymnasium/mathematik/klasse_7/lineare_gleichungen.pdf
- PDF Key: tests/germany/bayern/gymnasium/mathematik/klasse_7/lineare_gleichungen_key.pdf

📊 **Quality Metrics:**
- Factual Accuracy: 100%
- Clarity: 95%
- Difficulty: 30% easy, 50% medium, 20% hard
- Time: 28 min (average), 32 min (below-avg)

✅ Ready for classroom use!
```

**Total time:** ~5-8 minutes (fully automated)  
**Agents invoked:** 9 (Orchestrator + 8 specialists)  
**Handoffs completed:** 8 successful handoffs  
**Quality gates passed:** 3 (validation, difficulty, time)  

---

**Remember:** The system is designed to run AUTOMATICALLY once you invoke `@orchestrator`. Just provide the requirements and let the agents do their work!
