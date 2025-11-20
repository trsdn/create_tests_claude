# Claude Code Instructions - Educational Test Creator

This repository implements an AI-powered educational test creation system optimized for Claude Code's capabilities, using specialized agents and slash commands for maximum flexibility.

## Project Context

**Purpose:** Generate curriculum-aligned educational tests for children ages 6-19 across multiple education systems (Germany, USA, UK)

**Output Formats:**
- Markdown test files with YAML frontmatter
- Professional PDF versions (student + answer key)

**Target Users:** Teachers and educators creating assessments

## Directory Structure

```
create_tests_claude/
├── .claude/
│   ├── instructions.md        # This file - repository-wide Claude Code instructions
│   ├── agents/                # Agent definitions for Task tool
│   └── commands/              # Slash commands for manual workflows
├── data/curriculum/           # Curriculum YAML files by country/region/school/subject/grade
├── tests/                     # Generated Markdown test files
├── pdfs/                      # Generated PDF files (student + answer key versions)
├── .agent_workspace/          # Agent intermediate outputs (YAML files)
├── templates/                 # LaTeX templates for PDF generation
└── specs/                     # Complete specification documentation
```

## Agent Workflow

The system uses 9 specialized agents working in sequence:

1. **Orchestrator** - Coordinates workflow, gathers requirements, enforces quality gates
2. **Curriculum Fetcher** - Fetches curriculum from official sources, converts to YAML
3. **Curriculum Researcher** - Reads curriculum YAML files, extracts learning objectives
4. **Test Designer** - Generates test questions (10+ types) aligned with curriculum
5. **Content Validator** - Validates accuracy, age-appropriateness, clarity, bias
6. **Difficulty Analyzer** - Assesses difficulty (0-10 scale), ensures balanced distribution
7. **Time Estimator** - Calculates completion time for different skill levels
8. **Formatter** - Applies consistent Markdown formatting with visual elements
9. **PDF Generator** - Converts Markdown to PDF using Pandoc + LaTeX

### ⚠️ CRITICAL: Curriculum Fetcher Requirements

**MANDATORY for ALL curriculum creation/updates:**

The **Curriculum Fetcher** agent **MUST ALWAYS** fetch curriculum content from official government sources using the `WebFetch` tool. **NEVER** create curriculum content from knowledge or assumptions.

**Required Workflow:**
1. ✅ **ALWAYS** use `WebFetch` to retrieve official curriculum documents
2. ✅ **ALWAYS** verify source URLs (e.g., `schulportal.sachsen.de`, `kmk.org`, `corestandards.org`)
3. ✅ **ALWAYS** extract verbatim learning objectives from official sources
4. ✅ **ALWAYS** document source URLs in YAML `source_url` field
5. ✅ **ALWAYS** note actual fetch date in curriculum metadata

**NEVER:**
- ❌ Create curriculum content without fetching official sources first
- ❌ Rely on AI knowledge or assumptions about curriculum content
- ❌ Fabricate learning objectives or topics
- ❌ Skip source verification

**Why This Matters:**
- Legal compliance: Curriculum must match official government standards
- Accuracy: Only official sources are authoritative
- Traceability: Teachers need verifiable curriculum alignment
- Liability: Incorrect curriculum alignment can invalidate assessments

**This is PRODUCTION CODE** - all curriculum content must be factually accurate and source-verified.

## Data Flow

Agents communicate via YAML files in `.agent_workspace/`:
- Curriculum research → `.agent_workspace/curriculum_research/{session_id}.yaml`
- Test drafts → `.agent_workspace/test_drafts/{test_id}_draft_v{n}.md`
- Validation reports → `.agent_workspace/validation_reports/{test_id}_validation.yaml`
- Difficulty analysis → `.agent_workspace/difficulty_analysis/{test_id}_difficulty.yaml`
- Time estimates → `.agent_workspace/time_estimates/{test_id}_timing.yaml`

Final outputs:
- Markdown tests → `tests/{country}/{region}/{school_type}/{subject}/{grade}/{topic}/`
- PDF files → Same location as Markdown files (co-located)

### ⚠️ CRITICAL: Mandatory Agent Handoffs

**EVERY agent MUST hand off to the next agent in the pipeline!**

**Required Workflow Chain:**
```
Orchestrator → Curriculum Fetcher → Curriculum Researcher → Test Designer
           → Content Validator → Difficulty Analyzer → Time Estimator
           → Formatter → PDF Generator → Orchestrator (final delivery)
```

**Revision Loops (when quality gates fail):**
```
Content Validator → Test Designer → Content Validator (re-validate!)
Difficulty Analyzer → Test Designer → Content Validator → Difficulty Analyzer (re-check!)
Time Estimator → Test Designer → Content Validator → Difficulty Analyzer → Time Estimator (re-check!)
```

**‼️ NEVER skip agents or deliver incomplete tests to users!**

Each agent has a **mandatory handoff protocol**:
- ✅ What they MUST do after completing their work
- ❌ What they must NEVER do (skip steps, deliver directly to user)
- Verification checklist before handoff

**Best Practice:** Use the orchestrator (via `/create-test` command or Task tool) to ensure complete workflow execution.

## Key Standards

**Difficulty Distribution:**
- Easy: 30% (±10%)
- Medium: 50% (±10%)
- Hard: 20% (±10%)

**Quality Thresholds:**
- Factual accuracy: 100%
- Age-appropriateness: 95%
- Clarity: 90%
- Bias-free: 100%

**Question Types:** Multiple choice, True/False, Fill-blank, Matching, Ordering, Short answer, Multiple select, Drag-drop, Image-based, Scenario-based

**Bloom's Taxonomy Distribution:**
- Remember/Understand: 40%
- Apply/Analyze: 40%
- Evaluate/Create: 20%

## File Naming Conventions

**Tests:** `{topic_name}_{variant}.md` (lowercase, underscores)
**Answer Keys:** `{topic_name}_key.md`
**PDFs:** `{Subject}_{Topic}_Grade{X}_{Type}.pdf`

## Regional Specifications

**Germany:**
- Language: German (formal "Sie" for Gymnasium, informal "du" for Grundschule)
- Grading: 1-6 scale (1=Sehr gut, 6=Ungenügend)
- Notation: Decimal comma (3,14), thousands dot (1.000), multiplication (·)

**USA:**
- Language: English
- Grading: A-F or percentage-based
- Standards: Common Core, NGSS, state-specific

**UK:**
- Language: British English
- Grading: Key Stages, GCSE grades
- Standards: National Curriculum for England/Scotland/Wales/NI

## Claude Code Tool Usage Guidelines

**PREFERRED Tools:**
- ✅ Use `Read` tool for reading file contents
- ✅ Use `Edit` tool for modifying existing files
- ✅ Use `Write` tool for creating new files
- ✅ Use `Glob` tool for finding files by pattern
- ✅ Use `Grep` tool for searching content in files
- ✅ Use `WebFetch` tool for fetching curriculum from official sources
- ✅ Use `Task` tool to launch specialized agents for complex workflows
- ✅ Use `Bash` tool ONLY for git, pandoc, installing dependencies, and shell operations

**AVOID:**
- ❌ Using `Bash` for file operations (use Read/Edit/Write instead)
- ❌ Using `Bash` for searching (use Grep/Glob instead)
- ❌ Creating files with echo/cat/heredoc (use Write tool)

**Rationale:**
- Claude Code's specialized tools provide better context awareness
- Direct file operations are more reliable and traceable
- Better error handling and validation
- Improved user experience

## How to Use This System

### Option 1: Main Workflow (Slash Command)

Start a complete test creation workflow:

```
/create-test
```

This launches the orchestrator which will gather requirements and coordinate all agents.

### Option 2: Individual Workflows (Slash Commands)

Run specific parts of the workflow:

```
/fetch-curriculum     # Just fetch and convert curriculum to YAML
/design-test          # Design a test from existing curriculum
/validate-test        # Validate an existing test draft
/generate-pdf         # Convert markdown test to PDF
/analyze-difficulty   # Analyze difficulty distribution
```

### Option 3: Direct Agent Invocation (Advanced)

For advanced users who want full control, you can invoke agents directly via the Task tool. See `.claude/agents/` for agent definitions.

## Workflow Reports

Every test creation run generates a comprehensive workflow report documenting all steps, decisions, and outputs:

**Report Location:** `.agent_workspace/reports/{test_id}_run_{timestamp}.md`

**Report Contents:**
- All 9 agent steps with inputs/outputs
- Quality metrics (difficulty, time, curriculum alignment)
- Revision loops and adjustments
- Complete audit trail
- Performance metrics

## Quality Gates & Revision Loops

The system enforces strict quality gates:

**Content Validation Gate:**
- Factual accuracy: 100%
- Age-appropriateness: ≥95%
- Clarity: ≥90%
- Bias-free: 100%
- Curriculum alignment: 100%

**Difficulty Distribution Gate:**
- Easy: 30% ±10%
- Medium: 50% ±10%
- Hard: 20% ±10%

**Time Feasibility Gate:**
- Fits target duration for average students
- Feasible for below-average students
- Age-appropriate concentration span

**Revision Loop Limits:**
- Maximum 3 content validation attempts
- Maximum 3 difficulty adjustments
- Maximum 3 time adjustments
- Maximum 5 total revisions
- Escalate to human if limits exceeded

## Error Handling

**If Agent Fails:**
1. Log error details in workflow report
2. Retry up to 2 times
3. If still failing, present options to user
4. Allow manual intervention

**If Quality Gate Fails:**
1. Send test back to Test Designer with specific feedback
2. Increment revision counter
3. Re-run full validation pipeline
4. Maximum 3 iterations, then escalate

## Documentation

Complete specifications available in `specs/`:
- `specs/main-spec.md` - Project overview and educational research
- `specs/data-schemas.md` - File formats and templates
- `specs/agent-collaboration.md` - Inter-agent communication
- `specs/agents/*.md` - Individual agent specifications
- `specs/implementation-guide.md` - Implementation checklist

## Getting Started

1. Run `/create-test` to start the workflow
2. Provide test requirements when prompted (country, region, school type, subject, grade, topic)
3. Orchestrator will coordinate all agents automatically
4. Review final Markdown and PDF outputs in `tests/` directory
5. Check workflow report in `.agent_workspace/reports/` for complete audit trail

---

**IMPORTANT:** This system is designed for educational use. All content must be:
- Factually accurate
- Age-appropriate
- Bias-free
- Aligned with official curriculum standards
- Source-verified from official government documents

Always prioritize quality and curriculum alignment over speed of generation.
