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

## Data Flow

Agents communicate via YAML files in `.agent_workspace/`:
- Curriculum research → `.agent_workspace/curriculum_research/{session_id}.yaml`
- Test drafts → `.agent_workspace/test_drafts/{test_id}_draft_v{n}.md`
- Validation reports → `.agent_workspace/validation_reports/{test_id}_validation.yaml`
- Difficulty analysis → `.agent_workspace/difficulty_analysis/{test_id}_difficulty.yaml`
- Time estimates → `.agent_workspace/time_estimates/{test_id}_timing.yaml`

Final outputs:
- Markdown tests → `tests/{country}/{region}/{school_type}/{subject}/{grade}/{topic}/`
- PDF files → `pdfs/student_versions/` and `pdfs/answer_keys/`

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

**File Operations:** All agents have access to `codebase` and `editFiles` tools
**Terminal Access:** PDF Generator uses `runInTerminal` for Pandoc commands
**Auto-Approval:** Disabled for safety - manual review required for file modifications

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
