Fetch and convert official curriculum data from government education sources to standardized YAML format.

This command checks if curriculum already exists, and if not (or if outdated), fetches from official sources using WebFetch and converts to YAML.

**What it does:**
1. Checks if curriculum exists and is current (< 90 days old)
2. If needed, fetches from official education ministry sources
3. Extracts learning objectives verbatim from official documents
4. Converts to standardized YAML format
5. Validates completeness (target: ≥80%)
6. Saves to data/curriculum/ directory

**Usage:**
```
/fetch-curriculum
```

You'll be prompted for:
- Country (Germany/USA/UK)
- Region (Bayern, Texas, England, etc.)
- School type (Gymnasium, High School, etc.)
- Subject
- Grade level

**Output:**
- YAML file: `data/curriculum/{country}/{region}/{school_type}/{subject}/grade_{grade}.yaml`

**⚠️ CRITICAL:** This command ALWAYS fetches from official government sources. Never creates curriculum from AI knowledge.

**Time:** 2-5 minutes depending on source availability
