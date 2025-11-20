# Migration from GitHub Copilot to Claude Code

This repository has been restructured from GitHub Copilot custom agents to Claude Code agents.

## What Changed

### Directory Structure

**Before (GitHub Copilot):**
```
.github/
├── agents/*.agent.md      # GitHub Copilot agent definitions
└── copilot-instructions.md # Copilot-specific instructions
```

**After (Claude Code):**
```
.claude/
├── instructions.md         # Claude Code instructions
├── agents/*.md            # Agent definitions for Task tool
└── commands/*.md          # Slash commands for manual workflows
```

### Agent System

**GitHub Copilot Approach:**
- Agents defined with YAML frontmatter
- Invoked via `@agent-name` syntax
- Built-in handoff system between agents
- Tools: `edit`, `search`, `runCommands`, `memory`, `todos`

**Claude Code Approach:**
- Agents defined as markdown prompt files
- Launched via Task tool or slash commands
- Orchestrator coordinates agent handoffs
- Tools: `Read`, `Write`, `Edit`, `WebFetch`, `Grep`, `Glob`, `Bash`, `Task`, `AskUserQuestion`, `TodoWrite`

### Key Improvements for Claude Code

1. **Hybrid Interface:**
   - Automated workflows via orchestrator
   - Manual control via slash commands (`/create-test`, `/fetch-curriculum`, etc.)
   - Flexibility to choose approach based on need

2. **Better Tool Integration:**
   - Direct use of WebFetch for curriculum fetching
   - Native file operations (Read/Write/Edit)
   - Powerful search capabilities (Grep/Glob)
   - Interactive questions via AskUserQuestion

3. **Enhanced Orchestration:**
   - Orchestrator uses Task tool to launch specialized agents
   - Better context management
   - More robust error handling
   - Comprehensive workflow reporting

4. **Documentation:**
   - All agent definitions converted to Claude Code format
   - Added detailed usage instructions for Claude Code tools
   - Created slash commands for common workflows

## Usage Changes

### Creating a Test

**GitHub Copilot:**
```
@orchestrator Create a test for Grade 7 Math
```

**Claude Code:**
```
/create-test
```
Or natural language:
```
Create a test for Grade 7 Math
```

### Fetching Curriculum

**GitHub Copilot:**
```
@curriculum-fetcher Fetch curriculum for Bayern Gymnasium
```

**Claude Code:**
```
/fetch-curriculum
```

### Manual Agent Workflows

**GitHub Copilot:**
- Agents automatically hand off to each other
- Limited manual control

**Claude Code:**
- Full control via slash commands
- Can run individual workflows:
  - `/fetch-curriculum` - Just curriculum
  - `/validate-test` - Just validation
  - `/generate-pdf` - Just PDF generation
  - `/analyze-difficulty` - Just difficulty analysis

## Migration Checklist

If you have existing tests or workflows:

- [x] Repository structure updated to `.claude/`
- [x] Agent definitions converted from `.agent.md` to `.md` format
- [x] Instructions updated to reference Claude Code tools
- [x] Slash commands created for all major workflows
- [x] README updated with Claude Code usage
- [ ] Test the `/create-test` command end-to-end
- [ ] Verify curriculum fetching works with WebFetch
- [ ] Validate PDF generation still functions
- [ ] Check all quality gates operate correctly

## Old Files

The old `.github/` structure remains in the repository for reference but is no longer used by Claude Code. It can be removed once you've verified all functionality works:

```bash
# After verification, optionally remove old structure
rm -rf .github/agents/
rm .github/copilot-instructions.md
```

**Note:** Keep `.github/` directory if you use GitHub Actions or other GitHub-specific features.

## Benefits of Claude Code Version

1. **More Powerful:** Claude Sonnet 4.5 provides superior reasoning and context management
2. **Better Tools:** Native file operations, WebFetch for curriculum retrieval
3. **Flexible Control:** Choose between automated workflows or manual agent invocation
4. **Interactive:** AskUserQuestion tool enables better requirements gathering
5. **Transparent:** TodoWrite tool shows workflow progress in real-time
6. **Comprehensive:** Detailed agent definitions with clear instructions
7. **Auditable:** Complete workflow reports for every test generation

## Questions?

For issues or questions about the migration:
1. Check `.claude/instructions.md` for complete Claude Code usage
2. Read agent definitions in `.claude/agents/` for specific capabilities
3. Try slash commands in `.claude/commands/` for common workflows
4. Open a GitHub issue for any problems

## Version

- **Previous:** GitHub Copilot custom agents (October-November 2025)
- **Current:** Claude Code agents (November 2025)
- **Migration Date:** 2025-11-20
