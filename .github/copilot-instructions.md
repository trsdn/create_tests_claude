# GitHub Copilot Instructions - Educational Test Creator

This repository implements an AI-powered educational test creation system using 9 specialized GitHub Copilot custom agents.

## Project Context

**Purpose:** Generate curriculum-aligned educational tests for children ages 6-19 across multiple education systems (Germany, USA, UK)

**Output Formats:** 
- Markdown test files with YAML frontmatter
- Professional PDF versions (student + answer key)

**Target Users:** Teachers and educators creating assessments

## Directory Structure

```
create_tests/
├── .github/agents/          # 9 custom agent definitions
├── data/curriculum/         # Curriculum YAML files by country/region/school/subject/grade
├── tests/                   # Generated Markdown test files
├── pdfs/                    # Generated PDF files (student + answer key versions)
├── .agent_workspace/        # Agent intermediate outputs (YAML files)
├── templates/               # LaTeX templates for PDF generation
└── specs/                   # Complete specification documentation
```

## Agent Workflow

The system uses 9 specialized agents working in sequence:

1. **Orchestrator** - Coordinates workflow, gathers requirements, enforces quality gates
2. **Curriculum Fetcher** - Automatically fetches curriculum from official sources, converts to YAML
3. **Curriculum Researcher** - Reads curriculum YAML files, extracts learning objectives
4. **Test Designer** - Generates test questions (10+ types) aligned with curriculum
5. **Content Validator** - Validates accuracy, age-appropriateness, clarity, bias
6. **Difficulty Analyzer** - Assesses difficulty (0-10 scale), ensures balanced distribution
7. **Time Estimator** - Calculates completion time for different skill levels
8. **Formatter** - Applies consistent Markdown formatting with visual elements
9. **PDF Generator** - Converts Markdown to PDF using Pandoc + LaTeX

### ⚠️ CRITICAL: Curriculum Fetcher Requirements

**MANDATORY for ALL curriculum creation/updates:**

The **Curriculum Fetcher** agent **MUST ALWAYS** fetch curriculum content from official government sources using the `fetch_webpage` tool. **NEVER** create curriculum content from knowledge or assumptions.

**Required Workflow:**
1. ✅ **ALWAYS** use `fetch_webpage` to retrieve official curriculum documents
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

Each agent has a **mandatory handoff protocol** section at the end of their definition with:
- ✅ What they MUST do after completing their work
- ❌ What they must NEVER do (skip steps, deliver directly to user)
- Verification checklist before handoff

**If you invoke an agent directly (not through Orchestrator):**
- ⚠️ The agent may skip handoffs and deliver incomplete work
- ⚠️ Quality gates may be bypassed
- ⚠️ Tests may fail validation or have incorrect difficulty distribution

**Best Practice:** ALWAYS start with `@orchestrator` to ensure complete workflow execution.

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

## Tool Usage Guidelines

**⚠️ CRITICAL: Minimize Terminal Usage**

**PREFERRED File Operations:**
- ✅ Use `create_file` tool for creating new files (YAML, Markdown, etc.)
- ✅ Use `replace_string_in_file` or `multi_replace_string_in_file` for editing files
- ✅ Use `read_file` tool for reading file contents
- ✅ Use `list_dir` or `file_search` for exploring directory structure
- ✅ Use `semantic_search` or `grep_search` for finding content in workspace

**AVOID Terminal For:**
- ❌ Creating files (`cat >`, `echo >`, heredoc) → Use `create_file` instead
- ❌ Reading files (`cat`, `head`, `tail`) → Use `read_file` instead
- ❌ Directory listings (`ls`, `tree`) → Use `list_dir` instead
- ❌ File operations (`cp`, `mv`, `rm`) → Use file editing tools instead

**ONLY Use Terminal For:**
- ✅ Git operations (when not using `@github` MCP)
- ✅ Installing dependencies (`brew install pandoc`)
- ✅ Running Pandoc for PDF generation
- ✅ Executing validation scripts or test runners
- ✅ Operations genuinely requiring shell execution

**Rationale:**
- File editing tools maintain better workspace context
- Direct file operations are more reliable and predictable
- Less terminal noise improves user experience
- Proper tools enable better error handling and validation

**Auto-Approval:** Disabled for safety - manual review required for file modifications

## GitHub Integration

**⚠️ MANDATORY: GitHub MCP Server Usage**

This repository **REQUIRES** the use of the GitHub Model Context Protocol (MCP) server for ALL GitHub operations.

**REQUIRED for:**
- ✅ Creating issues for test creation tasks
- ✅ Managing pull requests for curriculum updates
- ✅ Tracking agent workflow progress via GitHub issues
- ✅ Version control operations (commits, branches)
- ✅ Repository metadata queries
- ✅ Collaboration and code review

**Usage:**
- **ALWAYS** use `@github` for GitHub-related operations
- **DO NOT** use git commands directly in terminal for GitHub operations
- **MUST** create GitHub issues for each test creation session
- **MUST** use PRs for curriculum additions or template changes

**Workflow Integration:**
1. **Start Session**: Create GitHub issue via `@github` (e.g., "Create Grade 6 English test")
2. **Track Progress**: Update issue with agent handoff status
3. **Complete**: Close issue when test is generated and validated
4. **Curriculum Updates**: Always use PRs via `@github` for new curriculum YAML files

## Documentation

Complete specifications available in `specs/`:
- Main specification: `specs/main-spec.md`
- Data schemas: `specs/data-schemas.md`
- Agent specs: `specs/agents/*.md`
- GitHub Copilot customization: `specs/github-copilot-customization.md`
- Implementation decisions: `specs/implementation-decisions.md`

## Getting Started

1. Invoke `@orchestrator` in GitHub Copilot Chat
2. Provide test requirements (country, region, school type, subject, grade, topic)
3. Orchestrator guides you through reverse interviewing if needed
4. Agent workflow executes automatically with handoffs
5. Review final Markdown and PDF outputs
