---
title: GitHub Copilot Customization Specification
description: Comprehensive guide for customizing GitHub Copilot with custom instructions, prompt files, custom agents, and MCP servers
version: 1.0
date: 2025-11-15
related:
  - agent-collaboration.md
  - implementation-guide.md
  - data-schemas.md
tags:
  - github-copilot
  - custom-instructions
  - prompt-files
  - custom-agents
  - ai-customization
---

# GitHub Copilot Customization Specification

## Table of Contents

1. [Overview](#overview)
2. [Directory Structure](#directory-structure)
3. [Custom Instructions](#custom-instructions)
4. [Prompt Files](#prompt-files)
5. [Custom Agents](#custom-agents)
6. [Chat Tools and MCP Servers](#chat-tools-and-mcp-servers)
7. [Integration with Test Creator System](#integration-with-test-creator-system)
8. [Best Practices](#best-practices)

---

## Overview

GitHub Copilot can be customized to match specific project requirements, coding standards, and workflows through three main mechanisms:

1. **Custom Instructions**: Guidelines that automatically influence how AI generates code
2. **Prompt Files**: Reusable prompts for common development tasks
3. **Custom Agents**: Specialized AI personas with specific tools and instructions

### Customization Hierarchy

```
Priority (Highest → Lowest):
1. Prompt File Tools (if specified)
2. Custom Agent Tools (if referenced)
3. Default Agent Tools
4. Custom Instructions (always applied when enabled)
```

### Supported Environments

- **VS Code**: Full support for all customization types
- **JetBrains IDEs**: Support for `.github/copilot-instructions.md` and `.prompt.md` files
- **GitHub.com**: Support for repository-wide custom instructions
- **Visual Studio**: Support for `.github/copilot-instructions.md`
- **Xcode/Eclipse**: Limited support

---

## Directory Structure

### Recommended File Organization

```
project-root/
├── .github/
│   ├── copilot-instructions.md          # Repository-wide instructions
│   ├── instructions/                    # Path-specific instructions
│   │   ├── backend.instructions.md
│   │   ├── frontend.instructions.md
│   │   ├── testing.instructions.md
│   │   └── security.instructions.md
│   ├── prompts/                         # Reusable prompt files
│   │   ├── generate-tests.prompt.md
│   │   ├── code-review.prompt.md
│   │   ├── security-audit.prompt.md
│   │   └── generate-docs.prompt.md
│   └── agents/                          # Custom agent definitions
│       ├── planner.agent.md
│       ├── implementation.agent.md
│       ├── reviewer.agent.md
│       └── security.agent.md
├── AGENTS.md                            # Root agent instructions (optional)
└── docs/
    └── agents/                          # Subfolder agent instructions (experimental)
        └── AGENTS.md
```

### File Extensions and Naming

| File Type | Extension | Location | Purpose |
|-----------|-----------|----------|---------|
| Repository Instructions | `.md` | `.github/copilot-instructions.md` | Apply to all requests |
| Path-Specific Instructions | `.instructions.md` | `.github/instructions/` | Apply to specific files/paths |
| Prompt Files | `.prompt.md` | `.github/prompts/` | Reusable task prompts |
| Custom Agents | `.agent.md` | `.github/agents/` | Specialized AI personas |
| Agent Instructions | `.md` | `AGENTS.md` (root or subfolders) | Multi-agent instructions |

---

## Custom Instructions

### Overview

Custom instructions define common guidelines that automatically influence AI behavior without manual inclusion in every prompt.

### Types of Instructions Files

#### 1. Repository-Wide Instructions (`.github/copilot-instructions.md`)

**Purpose**: Apply to all chat requests in the workspace

**Format**:
```markdown
# Project Coding Standards

- Use TypeScript for all new files
- Follow ESLint configuration in .eslintrc.json
- Write unit tests for all new functions using Jest
- Use functional components with React Hooks
- Follow conventional commits specification for commit messages
- Document all public APIs with JSDoc comments

# Testing Guidelines

- Maintain minimum 80% code coverage
- Write integration tests for all API endpoints
- Use React Testing Library for component tests
- Mock external API calls in unit tests
```

**VS Code Settings**:
```jsonc
{
  // Enable custom instructions
  "github.copilot.chat.codeGeneration.useInstructionFiles": true
}
```

#### 2. Path-Specific Instructions (`.instructions.md`)

**Purpose**: Apply instructions only to files matching specific patterns

**Format**:
```markdown
---
applyTo: "src/**/*.py"
description: Python backend coding standards
name: Python Standards
---

# Python Coding Standards

- Follow PEP 8 style guide
- Use type hints for all function signatures
- Write docstrings in Google style format
- Use pytest for unit tests
- Maintain 90% code coverage
- Use Black for code formatting
- Use mypy for static type checking

# Database Guidelines

- Use SQLAlchemy ORM for database operations
- Always use parameterized queries
- Implement database migrations with Alembic
- Use connection pooling for production
```

**Glob Pattern Examples**:
```yaml
# All TypeScript files
applyTo: "**/*.ts,**/*.tsx"

# Backend Ruby files
applyTo: "app/models/**/*.rb"

# All files (universal)
applyTo: "**"

# Frontend components only
applyTo: "src/components/**/*.jsx"
```

**Agent-Specific Instructions**:
```markdown
---
applyTo: "**"
excludeAgent: "code-review"
---

# Implementation guidelines
(Only used by coding agent, not code review)
```

#### 3. Agent Instructions (`AGENTS.md`)

**Purpose**: Define instructions for multi-agent systems

**Location Options**:
- Root: `AGENTS.md` (applies to all)
- Subfolder: `docs/AGENTS.md` (nearest takes precedence - experimental)
- Alternatives: `CLAUDE.md`, `GEMINI.md` (model-specific)

**Format**:
```markdown
# Educational Test Creator Agent Instructions

## Project Context

This repository contains an AI-powered educational test creator system using GitHub Copilot agent mode. The system generates curriculum-aligned tests for German, USA, and UK education systems.

## Code Generation Guidelines

- All Python code must use type hints
- Follow dataclass pattern for data structures
- Use YAML for configuration files
- Markdown for test content and answer keys
- JSON for test indexes and metadata

## Agent Workflow

1. Curriculum Research Agent researches standards
2. Test Designer Agent creates questions
3. Content Validator Agent checks accuracy
4. Difficulty Analyzer Agent assesses difficulty
5. Time Estimator Agent calculates time requirements
6. Formatter Agent converts to Markdown
7. PDF Generator Agent creates final PDF

## File Organization

- Tests stored in: `tests/{country}/{region}/{school_type}/{subject}/{grade}/{topic}/`
- Intermediate files in: `.agent_workspace/{agent_name}/`
- Final PDFs in: `pdfs/{country}/{region}/{school_type}/{subject}/{grade}/{topic}/`
```

**VS Code Settings**:
```jsonc
{
  // Enable AGENTS.md support
  "chat.useAgentsMdFile": true,
  
  // Enable subfolder AGENTS.md (experimental)
  "chat.useNestedAgentsMdFiles": true
}
```

### Settings-Based Instructions

**Specialized Scenarios**:

```jsonc
{
  // Code review instructions
  "github.copilot.chat.reviewSelection.instructions": [
    { "text": "Check for security vulnerabilities" },
    { "file": "docs/review-checklist.md" }
  ],
  
  // Commit message generation
  "github.copilot.chat.commitMessageGeneration.instructions": [
    { "text": "Follow Conventional Commits format" },
    { "text": "Include ticket reference in format: [PROJ-123]" }
  ],
  
  // PR description generation
  "github.copilot.chat.pullRequestDescriptionGeneration.instructions": [
    { "text": "Include list of key changes" },
    { "text": "Reference related issues" },
    { "file": "docs/pr-template.md" }
  ]
}
```

### Creating Instructions Files

**VS Code Commands**:
- `Chat: New Instructions File` - Create new instructions file
- `Chat: Configure Instructions` - Edit existing instructions
- `Chat: Generate Chat Instructions` - Auto-generate from workspace

**Manual Creation**:

1. Create `.github/instructions/` directory
2. Create file: `{name}.instructions.md`
3. Add YAML frontmatter with `applyTo` pattern
4. Write instructions in Markdown format

### Best Practices

1. **Keep Instructions Concise**: Each instruction should be a single, clear statement
2. **Use Multiple Files**: Separate by topic (language, framework, testing, security)
3. **Apply Selectively**: Use `applyTo` patterns to target specific file types
4. **Store in Repository**: Share instructions with team via version control
5. **Reference, Don't Duplicate**: Link to instructions from prompt files and agents

---

## Prompt Files

### Overview

Prompt files define reusable prompts for common development tasks. They are standalone prompts triggered on-demand.

### Prompt File Structure

**YAML Frontmatter Fields**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | string | No | Short description (placeholder text) |
| `name` | string | No | Prompt name (defaults to filename) |
| `argument-hint` | string | No | Hint text for chat input |
| `agent` | string | No | Agent to use: `ask`, `edit`, `agent`, or custom agent name |
| `model` | string | No | AI model (defaults to selected model) |
| `tools` | array | No | Available tools for this prompt |

**Body Content**:
- Markdown formatted instructions
- Reference files with Markdown links: `[file](../../path/to/file.ts)`
- Reference tools: `#tool:githubRepo`
- Use variables:
  - Workspace: `${workspaceFolder}`, `${workspaceFolderBasename}`
  - Selection: `${selection}`, `${selectedText}`
  - File: `${file}`, `${fileBasename}`, `${fileDirname}`, `${fileBasenameNoExtension}`
  - Input: `${input:variableName}`, `${input:variableName:placeholder}`

### Example Prompt Files

#### Example 1: Generate React Form Component

**File**: `.github/prompts/generate-react-form.prompt.md`

```markdown
---
description: Generate a React form component with validation
name: create-react-form
argument-hint: Specify form name and fields (e.g., formName=UserProfile fields=name,email,age)
agent: agent
tools: ['search', 'codebase', 'editFiles']
model: Claude Sonnet 4
---

# Generate React Form Component

Create a new React form component with the following requirements:

## Component Specifications

- Component Name: ${input:componentName:FormName}
- Fields: ${input:fields:name,email}
- Use React Hook Form for form management
- Include Zod schema validation
- Add TypeScript types
- Include proper error handling
- Follow project's component structure in #codebase

## Implementation Details

1. Create component file in `src/components/forms/`
2. Export component from `src/components/forms/index.ts`
3. Add TypeScript interface for form data
4. Implement validation schema with Zod
5. Include error messages for all fields
6. Add submit handler with proper typing
7. Include accessibility attributes (aria-labels, roles)

## Validation Rules

- Required fields must show "*" indicator
- Email fields must validate format
- Number fields must check range
- Custom validation as specified in prompt

## Styling

- Use Tailwind CSS classes
- Follow design system in `src/styles/design-tokens.ts`
- Include focus states for accessibility
- Add loading state during submission

## Testing

Generate unit tests in `src/components/forms/__tests__/` using:
- React Testing Library
- Test form submission
- Test validation errors
- Test accessibility
```

#### Example 2: Security Code Review

**File**: `.github/prompts/security-review.prompt.md`

```markdown
---
description: Perform comprehensive security review of selected code
name: security-audit
agent: ask
tools: ['codebase', 'usages', 'problems']
---

# Security Code Review

Perform a thorough security audit of the selected code: ${selection}

## Security Checklist

### Input Validation
- Check for SQL injection vulnerabilities
- Verify XSS prevention measures
- Validate all user inputs
- Check for command injection risks

### Authentication & Authorization
- Verify proper authentication checks
- Check authorization before sensitive operations
- Review session management
- Check for insecure direct object references

### Data Protection
- Verify sensitive data encryption
- Check for hardcoded secrets/credentials
- Review logging of sensitive information
- Check for secure data transmission (HTTPS)

### Common Vulnerabilities (OWASP Top 10)
- Broken Access Control
- Cryptographic Failures
- Injection Flaws
- Insecure Design
- Security Misconfiguration
- Vulnerable Components
- Authentication Failures
- Data Integrity Failures
- Security Logging Failures
- Server-Side Request Forgery

## Analysis Tasks

1. Review the selected code for each security concern
2. Identify specific vulnerabilities with line numbers
3. Assess severity (Critical, High, Medium, Low)
4. Provide remediation recommendations
5. Suggest secure code alternatives
6. Check for security best practices compliance

## Output Format

For each finding, provide:
- **Vulnerability**: Description
- **Location**: File and line numbers
- **Severity**: Critical/High/Medium/Low
- **Impact**: Potential security impact
- **Remediation**: Specific fix recommendations
- **Code Example**: Secure implementation

Use #codebase to analyze related code and #usages to find all instances.
```

#### Example 3: Generate Test Suite

**File**: `.github/prompts/generate-tests.prompt.md`

```markdown
---
description: Generate comprehensive test suite for selected function or class
name: generate-tests
agent: agent
tools: ['readFile', 'editFiles', 'codebase', 'search']
---

# Generate Test Suite

Generate comprehensive unit tests for: ${selection}

## Test Framework Configuration

- **Language**: Detect from ${fileBasename}
- **Test Framework**: 
  - JavaScript/TypeScript: Jest + React Testing Library
  - Python: pytest
  - Java: JUnit 5
  - Ruby: RSpec
- **Coverage Target**: 90%+

## Test Categories

### 1. Happy Path Tests
- Test normal execution flow
- Verify expected outputs
- Test typical use cases

### 2. Edge Cases
- Boundary values (min/max)
- Empty inputs
- Null/undefined values
- Zero values

### 3. Error Handling
- Invalid inputs
- Missing required parameters
- Type mismatches
- Exception scenarios

### 4. Integration Points
- Mock external dependencies
- Test API calls
- Test database operations
- Test file I/O

## Test Structure

Each test should include:
- **Arrange**: Setup test data and mocks
- **Act**: Execute the function/method
- **Assert**: Verify expected outcomes

## Naming Convention

Tests should be named: `test_{method_name}_{scenario}_{expected_result}`

Example: `test_calculateTotal_withValidItems_returnsCorrectSum`

## Mock Strategy

- Mock external API calls
- Mock database connections
- Mock file system operations
- Use dependency injection where possible

## Implementation Steps

1. Analyze the selected code using #codebase
2. Identify all code paths
3. Determine required test cases
4. Create test file in appropriate location
5. Generate tests with proper setup/teardown
6. Add descriptive test names and comments
7. Include assertion messages
8. Generate coverage report command

## Output Location

- JavaScript/TypeScript: `${fileDirname}/__tests__/${fileBasenameNoExtension}.test.ts`
- Python: `tests/test_${fileBasenameNoExtension}.py`
- Java: `src/test/java/.../Test${fileBasenameNoExtension}.java`
```

### Using Prompt Files

**Trigger Methods**:

1. **Slash Command in Chat**:
   ```
   /generate-react-form componentName=LoginForm fields=username,password
   ```

2. **Command Palette**:
   - `Chat: Run Prompt` → Select prompt file

3. **Editor Play Button**:
   - Open `.prompt.md` file
   - Click play button in editor title
   - Choose: "Run in current session" or "Open new session"

4. **Attach Context**:
   - Click paperclip icon in Chat view
   - Select "Prompt..." → Choose prompt file

### VS Code Settings

```jsonc
{
  // Enable prompt files
  "chat.promptFiles": true,
  
  // Additional prompt file locations
  "chat.promptFilesLocations": [
    "${workspaceFolder}/.github/prompts",
    "${workspaceFolder}/docs/prompts"
  ],
  
  // Show prompts as recommendations
  "chat.promptFilesRecommendations": true
}
```

### User Profile Prompt Files

**Location**: `{VS Code Profile Directory}/prompts/`

**Benefits**:
- Available across all workspaces
- Personal reusable prompts
- Can sync via Settings Sync

**Sync Configuration**:
1. Enable Settings Sync
2. Run: `Settings Sync: Configure`
3. Select: "Prompts and Instructions"

---

## Custom Agents

### Overview

Custom agents define specialized AI personas with specific tools, instructions, and behaviors for different development roles.

### Custom Agent File Structure

**YAML Frontmatter Fields**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `description` | string | No | Agent description (placeholder text) |
| `name` | string | No | Agent name (defaults to filename) |
| `argument-hint` | string | No | Hint text for interaction |
| `tools` | array | No | Available tools for agent |
| `model` | string | No | AI model to use |
| `target` | string | No | Target environment: `vscode` or `github-copilot` |
| `mcp-servers` | array | No | MCP server configs for GitHub Copilot |
| `handoffs` | array | No | Handoff definitions to other agents |

**Handoff Structure**:

```yaml
handoffs:
  - label: "Start Implementation"      # Button text
    agent: "implementation"            # Target agent
    prompt: "Implement the plan..."    # Pre-filled prompt
    send: false                        # Auto-submit (true/false)
```

**Body Content**:
- Markdown formatted agent instructions
- Reference files with Markdown links
- Reference tools: `#tool:toolName`
- Define agent behavior and workflow

### Example Custom Agents

#### Example 1: Planning Agent

**File**: `.github/agents/planner.agent.md`

```markdown
---
description: Generate implementation plans for features and refactoring
name: Planner
tools: ['fetch', 'githubRepo', 'search', 'usages', 'codebase', 'textSearch']
model: Claude Sonnet 4
handoffs:
  - label: "Implement Plan"
    agent: "implementation"
    prompt: "Implement the plan outlined above using the agent mode."
    send: false
  - label: "Review Plan"
    agent: "reviewer"
    prompt: "Review the implementation plan for completeness and accuracy."
    send: false
---

# Planning Agent Instructions

You are in **planning mode**. Your task is to generate detailed implementation plans without making any code edits.

## Responsibilities

- Analyze requirements and existing codebase
- Generate comprehensive implementation plans
- Identify dependencies and prerequisites
- Estimate complexity and risks
- Suggest testing strategies
- Do NOT make any code changes

## Plan Structure

Generate a Markdown document with these sections:

### 1. Overview
- Brief description of the feature/refactoring
- High-level approach
- Expected outcomes

### 2. Requirements Analysis
- Functional requirements
- Non-functional requirements
- Constraints and assumptions
- Success criteria

### 3. Current State Analysis
Use #codebase and #search to analyze:
- Existing code structure
- Related components
- Potential impact areas
- Technical debt considerations

### 4. Implementation Steps

For each step, include:
- **Step Number**: Sequential step identifier
- **Description**: What needs to be done
- **Files Affected**: List of files to modify/create
- **Dependencies**: Prerequisites for this step
- **Estimated Complexity**: Low/Medium/High
- **Risk Level**: Low/Medium/High

### 5. Architecture Changes
- New components/modules
- Modified interfaces
- Database schema changes
- API changes
- Configuration updates

### 6. Testing Strategy
- Unit tests required
- Integration tests needed
- E2E test scenarios
- Performance testing considerations
- Security testing requirements

### 7. Rollout Plan
- Feature flags needed
- Deployment sequence
- Rollback strategy
- Monitoring requirements

### 8. Dependencies
- External libraries needed
- Internal modules required
- Breaking changes
- Migration needs

### 9. Risk Assessment
- Technical risks
- Mitigation strategies
- Fallback options

### 10. Estimated Timeline
- Total effort estimate
- Breakdown by component
- Critical path items

## Tools Usage

- Use #codebase to understand project structure
- Use #search to find existing implementations
- Use #usages to understand code dependencies
- Use #githubRepo to research patterns in similar projects
- Use #fetch to get external documentation

## Output Guidelines

- Be thorough and detailed
- Include code examples for complex changes
- Reference specific file paths
- Provide clear acceptance criteria
- Highlight potential challenges
- Suggest alternatives when applicable
- Use Mermaid diagrams for complex workflows

## Handoff Process

After generating the plan:
1. Review completeness with user
2. Iterate based on feedback
3. When approved, hand off to Implementation Agent
4. Or hand off to Reviewer Agent for peer review
```

#### Example 2: Implementation Agent

**File**: `.github/agents/implementation.agent.md`

```markdown
---
description: Implement features and changes based on approved plans
name: Implementation
tools: 
  - 'edit'
  - 'readFile'
  - 'editFiles'
  - 'createFile'
  - 'createDirectory'
  - 'runInTerminal'
  - 'getTerminalOutput'
  - 'codebase'
  - 'search'
  - 'usages'
  - 'runTests'
  - 'problems'
model: Claude Sonnet 4
handoffs:
  - label: "Review Changes"
    agent: "reviewer"
    prompt: "Review the implemented changes for quality and correctness."
    send: false
  - label: "Generate Tests"
    agent: "tester"
    prompt: "Generate comprehensive tests for the implemented changes."
    send: false
---

# Implementation Agent Instructions

You are in **implementation mode**. Your task is to execute approved implementation plans by making actual code changes.

## Responsibilities

- Implement features according to plan
- Write clean, maintainable code
- Follow project coding standards
- Create necessary tests
- Update documentation
- Resolve compilation/linting errors

## Implementation Workflow

### 1. Review Plan
- Read implementation plan carefully
- Understand all requirements
- Identify dependencies
- Note risk areas

### 2. Pre-Implementation Checks
- Review existing code using #codebase
- Check for similar implementations using #search
- Understand usage patterns with #usages
- Identify affected areas

### 3. Implementation Steps

For each change:

#### A. Create/Modify Files
- Use #createFile for new files
- Use #editFiles for modifications
- Follow project structure
- Apply coding standards from [custom instructions](../../copilot-instructions.md)

#### B. Write Code
- Follow language-specific best practices
- Add type annotations
- Include error handling
- Write clear comments
- Use descriptive variable names

#### C. Handle Dependencies
- Import required modules
- Update package files if needed
- Resolve version conflicts

#### D. Update Tests
- Create unit tests for new code
- Update existing tests
- Ensure coverage thresholds
- Use #runTests to verify

#### E. Check for Issues
- Run linter: #runInTerminal
- Fix problems shown in #problems
- Resolve type errors
- Fix failing tests

### 4. Documentation
- Update README if needed
- Add JSDoc/docstrings
- Update API documentation
- Add inline comments for complex logic

### 5. Verification
- Run test suite: #runTests
- Check build: #runInTerminal
- Verify no regressions
- Test manually if needed

## Code Quality Standards

### General
- Follow DRY principle
- Keep functions small and focused
- Use meaningful names
- Handle errors gracefully
- Add logging where appropriate

### TypeScript/JavaScript
- Use TypeScript for type safety
- Prefer functional patterns
- Use async/await over promises
- Follow ESLint rules

### Python
- Follow PEP 8
- Use type hints
- Write docstrings
- Use dataclasses for data structures

### Error Handling
- Never swallow exceptions
- Provide meaningful error messages
- Log errors appropriately
- Handle edge cases

## Tools Usage

### File Operations
- #createFile - Create new files
- #createDirectory - Create directories
- #editFiles - Modify existing files
- #readFile - Read file content

### Code Analysis
- #codebase - Search codebase
- #search - Search for patterns
- #usages - Find references
- #problems - View issues

### Execution
- #runInTerminal - Run commands
- #getTerminalOutput - Get command output
- #runTests - Run test suite

## Progressive Implementation

1. Start with core functionality
2. Add error handling
3. Implement edge cases
4. Add tests
5. Refine and optimize

## Handoff Process

After implementation:
1. Verify all tests pass
2. Fix all linting errors
3. Update documentation
4. Hand off to Reviewer Agent for code review
5. Or hand off to Tester Agent for additional testing
```

#### Example 3: Code Review Agent

**File**: `.github/agents/reviewer.agent.md`

```markdown
---
description: Perform thorough code reviews with security and quality focus
name: Reviewer
tools: 
  - 'codebase'
  - 'search'
  - 'usages'
  - 'problems'
  - 'readFile'
  - 'changes'
  - 'textSearch'
model: Claude Sonnet 4
handoffs:
  - label: "Fix Issues"
    agent: "implementation"
    prompt: "Fix the issues identified in the code review."
    send: false
---

# Code Review Agent Instructions

You are in **review mode**. Your task is to perform comprehensive code reviews focusing on quality, security, and best practices.

## Review Categories

### 1. Code Quality
- [ ] Code readability and clarity
- [ ] Proper naming conventions
- [ ] DRY principle adherence
- [ ] Function/method length appropriate
- [ ] Proper code organization
- [ ] Comments where necessary
- [ ] No commented-out code
- [ ] Consistent code style

### 2. Architecture & Design
- [ ] Follows project architecture
- [ ] Proper separation of concerns
- [ ] Appropriate design patterns
- [ ] Scalability considerations
- [ ] Performance implications
- [ ] Code reusability
- [ ] Dependency management

### 3. Security
- [ ] Input validation
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] Authentication checks
- [ ] Authorization verification
- [ ] Secure data handling
- [ ] No hardcoded secrets
- [ ] Secure dependencies

### 4. Testing
- [ ] Adequate test coverage
- [ ] Tests are meaningful
- [ ] Edge cases covered
- [ ] Error cases tested
- [ ] Mocks used appropriately
- [ ] Tests are maintainable

### 5. Error Handling
- [ ] Errors properly caught
- [ ] Meaningful error messages
- [ ] Proper logging
- [ ] Graceful degradation
- [ ] No silent failures

### 6. Documentation
- [ ] README updated
- [ ] API docs current
- [ ] Code comments adequate
- [ ] Complex logic explained
- [ ] Examples provided

### 7. Performance
- [ ] No obvious bottlenecks
- [ ] Efficient algorithms
- [ ] Proper resource cleanup
- [ ] Memory usage reasonable
- [ ] Database queries optimized

## Review Process

### 1. Initial Analysis
Use #changes to get list of modified files:
```
- Identify all changed files
- Understand scope of changes
- Check for related files using #usages
```

### 2. File-by-File Review
For each changed file:
```
- Read full file using #readFile
- Understand context using #codebase
- Check for problems using #problems
- Identify code smells
- Note security concerns
```

### 3. Generate Review Report

Create a structured review report:

```markdown
## Code Review Report

**Date**: [Current Date]
**Reviewer**: Code Review Agent
**Files Reviewed**: [Count]

### Summary
[Brief overview of changes and overall assessment]

### Critical Issues 🔴
[Issues that must be fixed before merge]

1. **[Issue Title]**
   - **File**: `path/to/file.ts:123`
   - **Severity**: Critical
   - **Description**: [What's wrong]
   - **Impact**: [Why it matters]
   - **Recommendation**: [How to fix]
   - **Code Example**: 
     ```typescript
     // Current (problematic)
     [bad code]
     
     // Suggested fix
     [good code]
     ```

### Major Issues 🟡
[Important but not blocking issues]

### Minor Issues 🔵
[Nice-to-have improvements]

### Positive Observations ✅
[Things done well]

### Security Checklist
- [ ] No SQL injection vulnerabilities
- [ ] No XSS vulnerabilities
- [ ] Input validation present
- [ ] Authentication verified
- [ ] Authorization checked
- [ ] Secrets properly managed
- [ ] Secure dependencies

### Performance Notes
[Performance observations and recommendations]

### Testing Coverage
- **Current Coverage**: [if available]
- **Test Quality**: [assessment]
- **Missing Tests**: [what's not tested]

### Overall Assessment
- **Approval Status**: Approved / Changes Requested / Rejected
- **Recommendation**: [final recommendation]
```

## Review Severity Levels

### Critical 🔴
- Security vulnerabilities
- Data loss risks
- Breaking changes
- Performance regressions
- **Action**: Must fix before merge

### Major 🟡
- Design flaws
- Code quality issues
- Missing tests
- Poor error handling
- **Action**: Should fix before merge

### Minor 🔵
- Style inconsistencies
- Missing comments
- Minor optimizations
- Nice-to-have improvements
- **Action**: Consider for future

## Tools Usage

- #changes - Get modified files
- #readFile - Read file contents
- #codebase - Search for patterns
- #usages - Find code usage
- #problems - View linting issues
- #search - Find similar code
- #textSearch - Search for specific text

## Best Practices

1. Be constructive, not critical
2. Explain WHY something is an issue
3. Provide specific examples
4. Suggest concrete solutions
5. Acknowledge good code
6. Focus on important issues
7. Be consistent in feedback

## Handoff Process

After review:
1. Generate complete review report
2. Categorize all findings
3. Provide clear action items
4. If changes needed, hand off to Implementation Agent
5. If approved, note in report
```

### Creating Custom Agents

**VS Code Commands**:
- `Chat: New Custom Agent` - Create new agent
- Configure Custom Agents → "Create new custom agent"

**Creation Steps**:

1. **Choose Location**:
   - **Workspace**: `.github/agents/` (team-shared)
   - **User Profile**: Available across workspaces (personal)

2. **Define Agent**:
   - Add YAML frontmatter
   - Specify tools
   - Write agent instructions
   - Define handoffs

3. **Test Agent**:
   - Select agent from dropdown
   - Test with sample prompts
   - Iterate based on results

### Using Custom Agents

**Activation**:
1. Open Chat view (⌃⌘I / Ctrl+Cmd+I)
2. Click agent dropdown
3. Select custom agent
4. Enter prompt

**Agent Handoffs**:
- Complete task with one agent
- Click handoff button
- Switch to next agent with context
- Pre-filled prompt (optional auto-send)

### Managing Agents

**Show/Hide Agents**:
1. Configure Custom Agents dropdown
2. Hover over agent
3. Click eye icon to toggle visibility

---

## Chat Tools and MCP Servers

### Built-in Tools

**Code Analysis**:
- `#codebase` - Semantic code search
- `#search` - File and code search
- `#usages` - Find references and implementations
- `#problems` - View linting/compilation errors
- `#textSearch` - Find text in files

**File Operations**:
- `#createFile` - Create new files
- `#createDirectory` - Create directories
- `#editFiles` - Modify files
- `#readFile` - Read file contents
- `#listDirectory` - List directory contents
- `#fileSearch` - Search files by glob pattern

**Terminal Operations**:
- `#runInTerminal` - Execute shell commands
- `#getTerminalOutput` - Get command output
- `#terminalLastCommand` - Get last command
- `#terminalSelection` - Get terminal selection

**Testing & Tasks**:
- `#runTests` - Run unit tests
- `#runTask` - Run workspace task
- `#createAndRunTask` - Create and run task
- `#getTaskOutput` - Get task output

**Context & Metadata**:
- `#selection` - Current editor selection
- `#changes` - Source control changes
- `#fetch` - Fetch web content
- `#githubRepo` - Search GitHub repositories
- `#extensions` - Search VS Code extensions

**Specialized**:
- `#new` - Scaffold new workspace
- `#newJupyterNotebook` - Create notebook
- `#getProjectSetupInfo` - Get setup instructions
- `#VSCodeAPI` - VS Code API documentation

### Tool Sets

**Predefined Sets**:
- `#edit` - File editing tools
- `#search` - Search and discovery tools
- `#runCommands` - Terminal command execution
- `#runTasks` - Task execution tools
- `#runNotebooks` - Notebook execution tools

**Custom Tool Sets**:

**File**: `.github/tool-sets.jsonc`

```jsonc
{
  "reader": {
    "tools": ["changes", "codebase", "problems", "usages", "readFile", "search"],
    "description": "Read-only tools for analysis",
    "icon": "book"
  },
  
  "writer": {
    "tools": ["createFile", "editFiles", "createDirectory", "runInTerminal"],
    "description": "Tools for making changes",
    "icon": "edit"
  },
  
  "tester": {
    "tools": ["runTests", "testFailure", "problems", "readFile", "codebase"],
    "description": "Testing and debugging tools",
    "icon": "beaker"
  },
  
  "security": {
    "tools": ["codebase", "usages", "textSearch", "problems", "readFile"],
    "description": "Security analysis tools",
    "icon": "shield"
  }
}
```

**Creating Tool Sets**:
1. Run: `Chat: Configure Tool Sets`
2. Select: "Create new tool sets file"
3. Define tool sets in `.jsonc` format

**Using Tool Sets**:
```
# In chat prompt
Analyze security issues #security

# In prompt file frontmatter
tools: ['security', 'reader']

# In custom agent
tools: ['security', 'tester', 'codebase']
```

### MCP Servers

**Model Context Protocol (MCP)** extends chat capabilities with external tools and data sources.

**Popular MCP Servers**:
- **GitHub**: Repository search, PR management
- **Filesystem**: Advanced file operations
- **PostgreSQL**: Database queries
- **Brave Search**: Web search
- **Slack**: Team communication
- **Memory**: Persistent knowledge base
- **Everything**: System-wide file search

**Configuration**:

**File**: `settings.json` (workspace or user)

```jsonc
{
  "chat.experimental.mcp.servers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"
      }
    },
    
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
    },
    
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres"],
      "env": {
        "POSTGRES_CONNECTION_STRING": "postgresql://user:pass@localhost/db"
      }
    }
  }
}
```

**Using MCP Tools**:

```markdown
# In custom agent tools list
tools: ['github/*', 'filesystem/read_file', 'postgres/query']

# In chat
Use GitHub MCP to find recent PRs #tool:github/list_pulls

# In prompt file
Use #tool:filesystem/read_file to load the configuration
```

### Tool Configuration

**Tool Picker**:
- Click "Configure Tools" button in Chat view
- Select/deselect tools for current request
- Search for specific tools

**Tool Approval**:

**Settings**:
```jsonc
{
  // Auto-approve all tools (⚠️ Security Risk)
  "chat.tools.global.autoApprove": false,
  
  // Auto-approve specific terminal commands
  "chat.tools.terminal.autoApprove": {
    "mkdir": true,
    "/^git (status|show\\b.*)$/": true,
    "rm -rf": false
  },
  
  // Enable terminal auto-approve
  "chat.tools.terminal.enableAutoApprove": true,
  
  // Block detected file writes
  "chat.tools.terminal.blockDetectedFileWrites": true
}
```

**Reset Confirmations**:
- Command: `Chat: Reset Tool Confirmations`

---

## Integration with Test Creator System

### Agent-Specific Custom Instructions

#### Orchestrator Agent Instructions

**File**: `.github/instructions/orchestrator.instructions.md`

```markdown
---
applyTo: ".agent_workspace/orchestrator/**"
description: Instructions for Orchestrator Agent workflow
---

# Orchestrator Agent Instructions

## Role
Coordinate all 7 specialized agents in the test creation workflow.

## Workflow Sequence
1. Parse user request (country, region, subject, grade, topic, etc.)
2. Invoke Curriculum Research Agent
3. Wait for curriculum data (YAML)
4. Invoke Test Designer Agent with curriculum context
5. Wait for test metadata (YAML)
6. Invoke Content Validator Agent
7. Wait for validation report
8. Invoke Difficulty Analyzer Agent
9. Wait for difficulty analysis
10. Invoke Time Estimator Agent
11. Wait for time estimates
12. Invoke Formatter Agent with all data
13. Wait for formatted Markdown test
14. Invoke PDF Generator Agent
15. Deliver final PDF and metadata

## Error Handling
- Retry failed agents (max 3 attempts)
- Log all errors to `.agent_workspace/orchestrator/errors.log`
- Notify user of failures
- Implement fallback strategies

## Quality Gates
- Curriculum must align with standards
- Test must pass validation
- Difficulty must be appropriate
- Time must be feasible
- Format must be correct
```

#### Test Designer Agent Instructions

**File**: `.github/instructions/test-designer.instructions.md`

```markdown
---
applyTo: ".agent_workspace/test_designer/**"
description: Instructions for Test Designer Agent
---

# Test Designer Agent Instructions

## Question Generation Rules

### Multiple Choice Questions (MCQ)
- 4 answer options (A, B, C, D)
- Only 1 correct answer
- Distractors must be plausible
- Avoid "all of the above" or "none of the above"
- Randomize correct answer position

### True/False Questions
- Statement must be unambiguous
- No double negatives
- Clear factual basis

### Fill-in-the-Blank
- One blank per question
- Blank should test key concept
- Provide word bank for younger grades

### Matching Questions
- 5-8 pairs
- One-to-one matching
- Clear column headers
- Randomize order

### Ordering/Sequencing
- 4-6 items to order
- Logical sequence (chronological, process, size, etc.)
- Clear ordering criterion

### Short Answer
- Clear question prompt
- Expected answer length specified
- Rubric for partial credit

### Multiple Select
- 4-6 options
- 2-3 correct answers
- Indicate "Select all that apply"

### Drag-and-Drop
- Visual categories or buckets
- 6-10 items to drag
- Clear instructions

### Image-Based
- High-quality image required
- Question references specific elements
- Alt text for accessibility

### Scenario-Based
- Realistic scenario (2-3 sentences)
- Multiple questions from same scenario
- Application of knowledge

## Metadata Requirements

Every question must include:
- Question ID (unique)
- Question type
- Subject area
- Topic
- Subtopic
- Difficulty level (1-5)
- Estimated time (seconds)
- Learning objective
- Bloom's taxonomy level
- Curriculum standard alignment

## Output Format

Save to: `.agent_workspace/test_designer/test_metadata.yaml`
```

### Custom Prompts for Educational Test Creation

#### Curriculum Research Prompt

**File**: `.github/prompts/research-curriculum.prompt.md`

```markdown
---
description: Research educational curriculum standards
name: research-curriculum
agent: agent
tools: ['fetch', 'githubRepo', 'search', 'codebase']
---

# Curriculum Research Prompt

Research curriculum standards for: ${input:country} - ${input:subject} - Grade ${input:grade}

## Research Tasks

### 1. Identify Standards
- **Germany**: Research Bildungsplan for ${input:bundesland}
- **USA**: Common Core, NGSS, or state standards for ${input:state}
- **UK**: National Curriculum for Key Stage ${input:keystage}

### 2. Extract Learning Objectives
For topic: ${input:topic}

Find:
- Core concepts
- Skills to develop
- Assessment criteria
- Prerequisite knowledge
- Cross-curricular links

### 3. Document Sources
- Official curriculum documents
- Educational authority websites
- Textbook references
- Academic standards

### 4. Generate YAML Output

```yaml
curriculum_research:
  country: ${input:country}
  region: ${input:region}
  subject: ${input:subject}
  grade: ${input:grade}
  topic: ${input:topic}
  standards:
    - id: ""
      description: ""
      source: ""
  learning_objectives:
    - objective: ""
      bloom_level: ""
  prerequisites:
    - ""
  assessment_criteria:
    - ""
  recommended_resources:
    - title: ""
      url: ""
```

Save to: `.agent_workspace/curriculum_research/standards.yaml`

Use #fetch for official documents and #githubRepo for educational repositories.
```

### Custom Agent for Educational Testing

**File**: `.github/agents/edu-test-creator.agent.md`

```markdown
---
description: Educational test creation specialist
name: EduTestCreator
tools:
  - 'fetch'
  - 'githubRepo'
  - 'search'
  - 'codebase'
  - 'createFile'
  - 'editFiles'
  - 'readFile'
  - 'createDirectory'
model: Claude Sonnet 4
handoffs:
  - label: "Research Curriculum"
    agent: "researcher"
    prompt: "Research curriculum standards for the specified educational context."
    send: true
  - label: "Design Test"
    agent: "designer"
    prompt: "Design test questions based on curriculum research."
    send: true
  - label: "Validate Content"
    agent: "validator"
    prompt: "Validate test content for accuracy and appropriateness."
    send: true
---

# Educational Test Creator Agent

Specialized agent for creating curriculum-aligned educational tests.

## Capabilities

1. **Curriculum Research**: Find and analyze educational standards
2. **Test Design**: Create age-appropriate questions
3. **Content Validation**: Ensure accuracy and appropriateness
4. **Difficulty Analysis**: Assess question difficulty
5. **Time Estimation**: Calculate completion time
6. **Formatting**: Generate Markdown and PDF outputs

## Workflow

### Step 1: Parse Request
Extract from user prompt:
- Country (Germany/USA/UK)
- Region (Bundesland/State/Region)
- School type
- Subject
- Grade level
- Topic
- Number of questions
- Time limit (optional)

### Step 2: Research Curriculum
Use #fetch and #githubRepo to:
- Find official curriculum documents
- Extract learning objectives
- Identify assessment standards
- Note prerequisites

### Step 3: Design Questions
Based on curriculum research:
- Generate questions aligned to standards
- Mix question types appropriately
- Ensure age-appropriateness
- Include answer key with explanations

### Step 4: Validate and Refine
- Check factual accuracy
- Verify language level
- Ensure cultural appropriateness
- Review answer key

### Step 5: Format Output
Generate:
- Markdown test file
- Markdown answer key
- YAML metadata
- PDF (via handoff)

## Educational Principles

### Age-Appropriate Design

**Ages 6-10 (Primary)**:
- Simple language
- Visual elements
- Short questions
- Clear instructions
- Encouraging tone
- 15-25 questions
- 20-30 minute tests

**Ages 11-14 (Secondary)**:
- Moderate complexity
- Mix of question types
- Some multi-step problems
- Academic tone
- 25-35 questions
- 40-50 minute tests

**Ages 15-18 (Upper Secondary)**:
- Complex reasoning
- Analytical questions
- Application scenarios
- Professional tone
- 30-40 questions
- 60-75 minute tests

### Question Distribution

Bloom's Taxonomy levels:
- Remember/Understand: 40%
- Apply/Analyze: 40%
- Evaluate/Create: 20%

### Difficulty Distribution

- Easy (1-2): 30%
- Medium (3): 50%
- Hard (4-5): 20%

## Output Structure

```
tests/{country}/{region}/{school_type}/{subject}/{grade}/{topic}/
  ├── test.md (Markdown test)
  ├── answer_key.md (Detailed solutions)
  ├── test_metadata.yaml (Metadata)
  └── test.pdf (Final PDF)

.agent_workspace/
  ├── curriculum_research/standards.yaml
  ├── test_designer/test_metadata.yaml
  ├── content_validator/validation_report.yaml
  ├── difficulty_analyzer/difficulty_report.yaml
  └── time_estimator/time_report.yaml
```

## Example Usage

```
Create a math test for German 6th graders (Gymnasium) in Bavaria 
covering fractions (Brüche). Include 25 questions, mix of MCQ, 
fill-in-blank, and short answer. Time limit: 45 minutes.
```

Agent will:
1. Research Bavarian Gymnasium math curriculum (Grade 6)
2. Extract learning objectives for fractions
3. Generate 25 curriculum-aligned questions
4. Create answer key with explanations
5. Validate content and difficulty
6. Estimate completion time
7. Format as Markdown and PDF
8. Save to appropriate directory
```

### Repository Instructions

**File**: `.github/copilot-instructions.md`

```markdown
# Educational Test Creator Repository Instructions

## Project Overview

This repository contains an AI-powered educational test creation system that generates curriculum-aligned tests for:
- **Germany**: 16 Bundesländer, 5 school types (Grundschule, Hauptschule, Realschule, Gymnasium, Gesamtschule)
- **USA**: 50 states, Common Core, NGSS
- **UK**: 4 regions, National Curriculum, Key Stages

## Architecture

### Agent System (8 Agents)

1. **Orchestrator**: Coordinates workflow
2. **Curriculum Research**: Researches educational standards
3. **Test Designer**: Creates questions
4. **Content Validator**: Validates accuracy
5. **Difficulty Analyzer**: Assesses difficulty
6. **Time Estimator**: Calculates time requirements
7. **Formatter**: Converts to Markdown
8. **PDF Generator**: Creates final PDF

### Data Flow

```
User Request
  → Orchestrator Agent
    → Curriculum Research Agent (YAML)
      → Test Designer Agent (YAML + MD draft)
        → Content Validator Agent (YAML report)
          → Difficulty Analyzer Agent (YAML report)
            → Time Estimator Agent (YAML report)
              → Formatter Agent (Markdown test + answer key)
                → PDF Generator Agent (PDF)
```

## Coding Standards

### Python
- Use type hints for all functions
- Follow PEP 8 style guide
- Use dataclasses for data structures
- Write docstrings in Google style
- Minimum 80% test coverage

### File Formats
- **Tests**: Markdown (.md)
- **Metadata**: YAML (.yaml)
- **Indexes**: JSON (.json)
- **Final Output**: PDF (.pdf)

### Directory Structure

```
tests/{country}/{region}/{school_type}/{subject}/{grade}/{topic}/
.agent_workspace/{agent_name}/
pdfs/{country}/{region}/{school_type}/{subject}/{grade}/{topic}/
```

## Question Types

Supported formats:
1. Multiple Choice (MCQ)
2. True/False
3. Fill-in-the-Blank
4. Matching
5. Ordering/Sequencing
6. Short Answer
7. Multiple Select
8. Drag-and-Drop (description)
9. Image-Based
10. Scenario-Based

## Age-Appropriate Design

### Ages 6-10
- Simple language, visual elements
- 15-25 questions, 20-30 minutes
- Encouraging, positive tone

### Ages 11-14
- Moderate complexity
- 25-35 questions, 40-50 minutes
- Academic but supportive tone

### Ages 15-18
- Complex reasoning
- 30-40 questions, 60-75 minutes
- Professional, objective tone

## Educational Standards

### Bloom's Taxonomy Distribution
- Remember/Understand: 40%
- Apply/Analyze: 40%
- Evaluate/Create: 20%

### Difficulty Distribution
- Easy (1-2): 30%
- Medium (3): 50%
- Hard (4-5): 20%

## Testing

- Unit tests for all agents
- Integration tests for workflows
- Validation tests for outputs
- Use pytest framework

## Documentation

- Update README for new features
- Document all agent specifications
- Maintain data schema documentation
- Include examples in docs/
```

---

## Best Practices

### General Guidelines

1. **Start Simple**: Begin with basic instructions, iterate based on results
2. **Be Specific**: Provide concrete examples and clear requirements
3. **Use Context**: Reference files and tools to provide full context
4. **Test Thoroughly**: Validate customizations with real-world scenarios
5. **Version Control**: Track instructions files in repository
6. **Team Sharing**: Store in workspace for team collaboration
7. **Document Purpose**: Explain why instructions exist

### Custom Instructions

1. **Keep Concise**: Each instruction should be a single, clear statement
2. **Separate Concerns**: Use multiple files for different topics
3. **Apply Selectively**: Use `applyTo` patterns for targeted application
4. **Reference Don't Duplicate**: Link to shared instructions
5. **Update Regularly**: Keep aligned with project evolution

### Prompt Files

1. **Clear Purpose**: Each prompt should have one specific task
2. **Provide Context**: Include relevant variables and file references
3. **Specify Output**: Define expected format and structure
4. **Include Examples**: Show desired output format
5. **Use Variables**: Make prompts reusable with input variables
6. **Reference Tools**: Explicitly call out required tools

### Custom Agents

1. **Define Clear Roles**: Each agent should have specific responsibilities
2. **Limit Tools**: Only include necessary tools for the role
3. **Use Handoffs**: Create workflows between related agents
4. **Write Detailed Instructions**: Provide comprehensive guidance
5. **Test Workflows**: Validate handoffs work smoothly
6. **Document Behavior**: Explain agent's decision-making process

### Security Considerations

1. **Tool Approval**: Never auto-approve all tools in production
2. **Terminal Commands**: Carefully configure auto-approve rules
3. **MCP Servers**: Only use trusted MCP servers
4. **Secret Management**: Never hardcode credentials
5. **Input Validation**: Validate user inputs in agents
6. **Access Control**: Limit file system access appropriately
7. **Review Changes**: Always review code changes before applying

### Performance Optimization

1. **Selective Tools**: Enable only required tools
2. **Tool Sets**: Group related tools for efficiency
3. **Virtual Tools**: Use for large tool counts (128+ tools)
4. **Caching**: Leverage agent memory for repeated tasks
5. **Incremental Changes**: Make small, focused edits
6. **Parallel Operations**: Use handoffs for parallel workflows

---

## Resources and References

### Official Documentation

- [VS Code Copilot Documentation](https://code.visualstudio.com/docs/copilot)
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- [Awesome Copilot Repository](https://github.com/github/awesome-copilot)
- [Model Context Protocol](https://modelcontextprotocol.io)

### Community Resources

- [Awesome Copilot Agents](https://github.com/github/awesome-copilot/tree/main/agents)
- [Custom Instructions Examples](https://docs.github.com/en/copilot/tutorials/customization-library/custom-instructions)
- [Prompt File Examples](https://github.com/github/awesome-copilot/blob/main/docs/README.prompts.md)

### Settings Reference

```jsonc
{
  // Custom Instructions
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "chat.useAgentsMdFile": true,
  "chat.useNestedAgentsMdFiles": false,
  "chat.instructionsFilesLocations": ["${workspaceFolder}/.github/instructions"],
  
  // Prompt Files
  "chat.promptFiles": true,
  "chat.promptFilesLocations": ["${workspaceFolder}/.github/prompts"],
  "chat.promptFilesRecommendations": true,
  
  // Tools
  "chat.tools.global.autoApprove": false,
  "chat.tools.terminal.enableAutoApprove": true,
  "chat.tools.terminal.autoApprove": {
    "mkdir": true,
    "/^git (status|show\\b.*)$/": true
  },
  
  // MCP Servers
  "chat.experimental.mcp.servers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": "${env:GITHUB_TOKEN}"}
    }
  }
}
```

### Keyboard Shortcuts

| Action | macOS | Windows/Linux |
|--------|-------|---------------|
| Open Chat view | ⌃⌘I | Ctrl+Alt+I |
| Voice Chat | ⌘I | Ctrl+I |
| New chat session | ⌘N | Ctrl+N |
| Switch agents | ⇧⌘I | Shift+Ctrl+I |
| Inline chat | ⌘I | Ctrl+I |
| Quick Chat | ⇧⌥⌘L | Shift+Alt+Ctrl+L |

---

## Changelog

### Version 1.0 (2025-11-15)
- Initial specification
- Custom instructions documentation
- Prompt files specification
- Custom agents guide
- MCP servers integration
- Educational test creator integration examples
