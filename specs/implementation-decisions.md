---
title: Implementation Decisions
description: Critical technical decisions for the Educational Test Creator system
version: 1.0
date: 2025-11-15
status: Decided
related:
  - implementation-guide.md
  - data-schemas.md
  - github-copilot-customization.md
---

# Implementation Decisions

## Overview

This document records the critical technical decisions made for implementing the Educational Test Creator system. These decisions resolve ambiguities in the specifications and provide clear direction for development.

**Decision Date:** November 15, 2025  
**Decision Method:** Reverse Interviewing (4-choice format)

---

## Decision Summary

| # | Decision Area | Choice | Rationale |
|---|---------------|--------|-----------|
| 1 | Curriculum Data Source | **A) Static Repository Files** | Fast, reliable, offline capable |
| 2 | PDF Generation Tool | **A) Pandoc + LaTeX** | Professional quality, excellent math rendering |
| 3 | Agent Environment | **A) GitHub Copilot Chat Agents** | Native integration, leverages existing AI |
| 4 | Answer Key Format | **C) Detailed Step-by-Step** | Excellent for learning, clear pedagogy |

---

## Decision 1: Curriculum Data Source Management

### Selected: **A) Static Repository Files**

Pre-downloaded curriculum documents stored in `data/curriculum/` directory, manually updated quarterly.

### Implementation Details

**Directory Structure:**
```
data/
└── curriculum/
    ├── germany/
    │   ├── baden_wuerttemberg/
    │   │   ├── gymnasium/
    │   │   │   ├── mathematik/
    │   │   │   │   └── grade_7.yaml
    │   │   │   └── bildungsplan_2016.pdf
    │   │   └── metadata.yaml
    │   ├── bayern/
    │   │   ├── gymnasium/
    │   │   │   ├── mathematik/
    │   │   │   │   └── klasse_7.yaml
    │   │   │   └── lehrplan_plus.pdf
    │   │   └── metadata.yaml
    │   └── ... (all 16 Bundesländer)
    ├── usa/
    │   ├── common_core/
    │   │   ├── mathematics/
    │   │   │   └── grade_7.yaml
    │   │   └── standards.json
    │   ├── states/
    │   │   ├── california/
    │   │   ├── texas/
    │   │   └── ... (all 50 states)
    │   └── ngss/
    │       └── science/
    └── uk/
        ├── england/
        │   ├── key_stage_3/
        │   │   └── mathematics.yaml
        │   └── national_curriculum.pdf
        ├── scotland/
        ├── wales/
        └── northern_ireland/
```

**YAML Curriculum File Format:**
```yaml
# data/curriculum/germany/bayern/gymnasium/mathematik/klasse_7.yaml
curriculum_metadata:
  region: "Bayern"
  country: "Germany"
  school_type: "Gymnasium"
  subject: "Mathematik"
  grade: 7
  source: "Lehrplan PLUS"
  version: "2024"
  last_updated: "2024-09-01"
  next_review: "2025-03-01"
  official_url: "https://www.lehrplanplus.bayern.de/"

topics:
  - id: "algebra_equations"
    name_de: "Lineare Gleichungen"
    name_en: "Linear Equations"
    
    learning_objectives:
      - id: "LO1"
        text_de: "Lösen einfacher linearer Gleichungen"
        text_en: "Solving simple linear equations"
        bloom_level: "Application"
        curriculum_ref: "LP-PLUS-BY-GYM-M7-2.3"
      
      - id: "LO2"
        text_de: "Anwenden von Äquivalenzumformungen"
        text_en: "Applying equivalent transformations"
        bloom_level: "Application"
        curriculum_ref: "LP-PLUS-BY-GYM-M7-2.3.1"
    
    prerequisites:
      - "Grundrechenarten"
      - "Bruchrechnung"
      - "Variablen und Terme"
    
    recommended_question_types:
      - type: "fill_blank"
        percentage: 30
      - type: "short_answer"
        percentage: 40
      - type: "multiple_choice"
        percentage: 20
      - type: "word_problem"
        percentage: 10
    
    vocabulary:
      required_terms:
        - term_de: "Gleichung"
          term_en: "Equation"
        - term_de: "Variable"
          term_en: "Variable"
        - term_de: "Äquivalenzumformung"
          term_en: "Equivalent transformation"
    
    assessment_criteria:
      - "Korrekte Anwendung von Äquivalenzumformungen"
      - "Systematisches Vorgehen beim Lösen"
      - "Durchführung der Probe"
```

### Update Process

**Quarterly Review Checklist:**
1. Check official education ministry websites for updates
2. Download new curriculum documents
3. Update YAML files with changes
4. Update `last_updated` and `next_review` dates
5. Commit changes to Git with changelog
6. Tag release: `curriculum-update-YYYY-QQ`

**Maintenance Commands:**
```bash
# Update script
python scripts/update_curriculum.py --region bayern --verify

# Validate all curriculum files
python scripts/validate_curriculum.py --all

# Generate report of outdated curriculum data
python scripts/curriculum_status.py --report
```

### Advantages Realized

✅ **Fast Access** - No network latency, instant curriculum lookup  
✅ **Reliable** - No dependency on external website availability  
✅ **Offline Capable** - Works without internet connection  
✅ **Version Controlled** - Git tracks all curriculum changes  
✅ **Predictable** - Consistent behavior across environments

### Mitigation of Disadvantages

❌ **Manual Maintenance** → Mitigated by:
- Quarterly update schedule
- Automated validation scripts
- Clear update procedures
- Git changelog tracking

❌ **Could Become Outdated** → Mitigated by:
- `next_review` dates in metadata
- Status monitoring scripts
- Automated alerts for outdated data
- Version tracking in YAML files

---

## Decision 2: PDF Generation Tool

### Selected: **A) Pandoc + LaTeX**

Industry standard solution providing highest quality typography and excellent math rendering.

### Implementation Details

**Installation Requirements:**

**macOS:**
```bash
# Install Pandoc
brew install pandoc

# Install BasicTeX (smaller than full TeX Live)
brew install basictex

# Install required LaTeX packages
sudo tlmgr update --self
sudo tlmgr install collection-fontsrecommended
sudo tlmgr install collection-latexextra
sudo tlmgr install babel-german
sudo tlmgr install ulem
sudo tlmgr install fancyhdr
```

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install pandoc
sudo apt-get install texlive-latex-recommended
sudo apt-get install texlive-fonts-recommended
sudo apt-get install texlive-latex-extra
sudo apt-get install texlive-lang-german
```

**Windows:**
```powershell
# Install via Chocolatey
choco install pandoc
choco install miktex

# Or download installers:
# Pandoc: https://pandoc.org/installing.html
# MiKTeX: https://miktex.org/download
```

**PDF Generation Command:**
```bash
pandoc test.md \
  -o test.pdf \
  --pdf-engine=xelatex \
  --template=templates/default.tex \
  --variable=lang:de-DE \
  --variable=geometry:a4paper \
  --variable=geometry:margin=2cm \
  --variable=fontsize:11pt \
  --variable=linestretch:1.15 \
  --toc \
  --toc-depth=2 \
  --number-sections
```

**LaTeX Template:** `templates/default.tex`
```latex
\documentclass[$if(fontsize)$$fontsize$,$endif$$if(lang)$$babel-lang$,$endif$$if(papersize)$$papersize$paper,$endif$$for(classoption)$$classoption$$sep$,$endfor$]{article}

% Packages
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage{geometry}
\usepackage[hidelinks]{hyperref}

% Page layout
\geometry{$geometry$}

% Headers and footers
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{$title$}
\fancyhead[R]{$if(subject)$$subject$ - $endif$Klasse $grade$}
\fancyfoot[C]{\thepage}

% Custom colors for themes
$if(theme)$
  $if(theme.colorful)$
    \definecolor{primarycolor}{RGB}{52,152,219}
    \definecolor{secondarycolor}{RGB}{46,204,113}
  $endif$
$endif$

% Document
\begin{document}

$if(title)$
\begin{center}
{\LARGE\bfseries $title$}
\end{center}
$endif$

$if(metadata)$
\begin{tabular}{ll}
Klasse: & $metadata.grade$ \\
Fach: & $metadata.subject$ \\
Zeit: & $metadata.time$ Minuten \\
Punkte: & $metadata.points$ \\
\end{tabular}
$endif$

\vspace{1cm}

$body$

\end{document}
```

**Python Integration:**
```python
# scripts/generate_pdf.py
import subprocess
import os
from pathlib import Path

class PandocPDFGenerator:
    def __init__(self, template_dir="templates"):
        self.template_dir = Path(template_dir)
        self.verify_installation()
    
    def verify_installation(self):
        """Verify Pandoc and LaTeX are installed"""
        try:
            subprocess.run(["pandoc", "--version"], 
                         capture_output=True, check=True)
            subprocess.run(["xelatex", "--version"], 
                         capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            raise RuntimeError(
                "Pandoc or LaTeX not installed. See installation instructions."
            ) from e
    
    def generate_pdf(self, markdown_path, output_path, 
                     theme="default", metadata=None):
        """Generate PDF from Markdown file"""
        cmd = [
            "pandoc",
            str(markdown_path),
            "-o", str(output_path),
            "--pdf-engine=xelatex",
            f"--template={self.template_dir / theme}.tex",
            "--variable=lang:de-DE",
            "--variable=geometry:a4paper",
            "--variable=geometry:margin=2cm",
            "--number-sections"
        ]
        
        if metadata:
            for key, value in metadata.items():
                cmd.append(f"--variable={key}:{value}")
        
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True,
                timeout=30
            )
            return {"success": True, "path": output_path}
        except subprocess.CalledProcessError as e:
            return {
                "success": False,
                "error": e.stderr,
                "command": " ".join(cmd)
            }
        except subprocess.TimeoutExpired:
            return {
                "success": False,
                "error": "PDF generation timed out after 30 seconds"
            }
```

### Three Themes Implementation

**1. Default Theme** (`templates/default.tex`)
- Clean, professional layout
- Black text on white background
- Standard fonts (Latin Modern)
- Minimal decoration

**2. Colorful Theme** (`templates/colorful.tex`)
- Bright, engaging colors
- Icons and emojis preserved
- Colored section headers
- Visual difficulty indicators

**3. Minimal Theme** (`templates/minimal.tex`)
- Maximum white space
- Larger fonts (12pt base)
- Wide margins (3cm)
- Dyslexia-friendly (OpenDyslexic font option)

### Performance Optimization

**Parallel Generation:**
```python
from concurrent.futures import ThreadPoolExecutor

def generate_multiple_pdfs(test_files, max_workers=4):
    """Generate multiple PDFs in parallel"""
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = []
        for md_file in test_files:
            pdf_file = md_file.with_suffix('.pdf')
            future = executor.submit(
                generator.generate_pdf, md_file, pdf_file
            )
            futures.append((md_file, future))
        
        results = []
        for md_file, future in futures:
            result = future.result()
            results.append((md_file, result))
        
        return results
```

### Advantages Realized

✅ **Professional Output** - Publication-quality typography  
✅ **Excellent Math Rendering** - LaTeX math equations render perfectly  
✅ **Full Control** - Complete customization via templates  
✅ **Industry Standard** - Well-documented, widely supported  
✅ **Unicode Support** - Handles German characters (ä, ö, ü, ß)

### Mitigation of Disadvantages

❌ **Large Installation** → Mitigated by:
- Use BasicTeX (450MB) instead of full TeX Live (5GB)
- Docker image with pre-installed dependencies
- Cloud generation option for lightweight clients

❌ **Slower Generation** → Mitigated by:
- Parallel PDF generation (4 concurrent)
- Caching of intermediate files
- Template pre-compilation
- Target: <10 seconds per PDF

❌ **Complex Windows Installation** → Mitigated by:
- Detailed installation guide
- Automated installation script
- Docker alternative
- Pre-built Windows executable bundle

---

## Decision 3: Agent Execution Environment

### Selected: **A) GitHub Copilot Chat Agents**

Use `.github/agents/*.agent.md` files with VS Code Copilot for native integration.

### Implementation Details

**Agent File Structure:**

All 8 agents implemented as custom agents in `.github/agents/`:

```
.github/
└── agents/
    ├── orchestrator.agent.md
    ├── curriculum-researcher.agent.md
    ├── test-designer.agent.md
    ├── content-validator.agent.md
    ├── difficulty-analyzer.agent.md
    ├── time-estimator.agent.md
    ├── formatter.agent.md
    └── pdf-generator.agent.md
```

**Example: Curriculum Research Agent**

`.github/agents/curriculum-researcher.agent.md`:
```markdown
---
description: Research educational curriculum standards and learning objectives
name: CurriculumResearcher
tools:
  - 'readFile'
  - 'search'
  - 'textSearch'
  - 'codebase'
  - 'listDirectory'
model: Claude Sonnet 4
handoffs:
  - label: "Design Test"
    agent: "test-designer"
    prompt: "Design a test based on the curriculum research results."
    send: false
---

# Curriculum Research Agent

You are a specialized curriculum research agent for educational test creation.

## Role
Research and analyze curriculum standards from official education documents stored in `data/curriculum/`.

## Workflow

### Step 1: Parse Request
Extract educational context:
- Country (Germany/USA/UK)
- Region (Bundesland/State)
- School type
- Subject
- Grade level
- Topic

### Step 2: Locate Curriculum Data
Use #textSearch and #readFile to find curriculum files:

```
Pattern: data/curriculum/{country}/{region}/{school_type}/{subject}/grade_{N}.yaml
```

Example:
```
#textSearch data/curriculum/germany/bayern/gymnasium/mathematik/klasse_7.yaml
```

### Step 3: Extract Learning Objectives
Read curriculum file using #readFile and extract:
- Learning objectives for the specified topic
- Bloom's taxonomy levels
- Prerequisites
- Recommended question types
- Vocabulary requirements
- Assessment criteria

### Step 4: Generate YAML Output
Create structured output in `.agent_workspace/curriculum_research/`:

```yaml
research_session:
  session_id: "curr_{country}_{region}_{timestamp}"
  timestamp: "{ISO-8601}"
  
request:
  country: "{country}"
  region: "{region}"
  school_type: "{school_type}"
  subject: "{subject}"
  grade: {grade}
  topic: "{topic}"

curriculum_data:
  # ... extracted data from curriculum file
  
learning_objectives:
  # ... learning objectives for topic
```

Save to: `.agent_workspace/curriculum_research/{session_id}.yaml`

### Step 5: Hand Off to Test Designer
Use handoff button to pass curriculum data to Test Designer Agent.

## Tools Usage

- #listDirectory - Browse curriculum directory structure
- #textSearch - Find curriculum files by region/subject
- #readFile - Read curriculum YAML files
- #search - Find specific topics within curriculum
- #codebase - Search for curriculum patterns

## Example Interaction

User: "Create a math test for 7th grade Gymnasium in Bayern about linear equations"

Agent:
1. Extract: country=Germany, region=Bayern, school_type=Gymnasium, subject=Mathematik, grade=7, topic=Lineare Gleichungen
2. Search: `data/curriculum/germany/bayern/gymnasium/mathematik/klasse_7.yaml`
3. Read file and extract topic "algebra_equations"
4. Generate YAML with learning objectives
5. Save to `.agent_workspace/curriculum_research/`
6. Notify: "Curriculum research complete. Found 3 learning objectives. Ready to hand off to Test Designer."
```

**Workflow Orchestration:**

Users interact with the system through sequential agent handoffs:

```
User Request
  ↓
[Orchestrator Agent]
  ↓ (gather requirements)
[Curriculum Researcher Agent]
  ↓ (research standards)
[Test Designer Agent]
  ↓ (create questions)
[Content Validator Agent]
  ↓ (validate quality)
[Difficulty Analyzer Agent]
  ↓ (assess difficulty)
[Time Estimator Agent]
  ↓ (calculate time)
[Formatter Agent]
  ↓ (format markdown)
[PDF Generator Agent]
  ↓ (create PDF)
Final Output
```

**Agent Communication:**

Agents communicate via YAML files in `.agent_workspace/`:

```python
# Each agent reads predecessor's output
curriculum_data = read_yaml('.agent_workspace/curriculum_research/session_123.yaml')

# Each agent writes its output
write_yaml('.agent_workspace/test_designer/session_123.yaml', test_data)
```

**VS Code Settings:**

`.vscode/settings.json`:
```json
{
  "chat.promptFiles": true,
  "chat.useAgentsMdFile": true,
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "chat.tools.global.autoApprove": false,
  "chat.tools.terminal.enableAutoApprove": true,
  "chat.tools.terminal.autoApprove": {
    "mkdir": true,
    "cp": true,
    "pandoc": true
  }
}
```

### User Interaction Flow

1. **Start in Chat View** (⌃⌘I)
2. **Select Orchestrator Agent** from dropdown
3. **Enter Request**: "Create a math test for 7th grade Gymnasium in Bayern about linear equations, 30 minutes, 4 questions"
4. **Orchestrator Prompts** for missing info if needed
5. **Sequential Handoffs**: Click handoff buttons to move through pipeline
6. **Review Outputs**: Each agent shows its results before handoff
7. **Final Delivery**: PDF saved to `pdfs/` directory

### Advantages Realized

✅ **Native Integration** - Works seamlessly with VS Code  
✅ **No Infrastructure** - No servers or APIs to manage  
✅ **Existing AI Models** - Uses GitHub Copilot's models  
✅ **Iterative Development** - Easy to test and refine agents  
✅ **Human-in-Loop** - User reviews each step

### Mitigation of Disadvantages

❌ **Manual Interaction** → Mitigated by:
- Clear handoff buttons between agents
- Pre-filled prompts for next step
- Progress tracking in agent outputs
- Can automate later with Python wrapper if needed

❌ **Not Fully Automated** → Mitigated by:
- Orchestrator agent manages workflow
- Minimal user input required
- Future: Python script can invoke agents programmatically
- For now: Semi-automated workflow is acceptable for MVP

---

## Decision 4: Answer Key Format

### Selected: **C) Detailed: Full Step-by-Step Solutions**

Provide complete worked solutions with all steps, explanations, and verification.

### Implementation Details

**Answer Key Template:**

```markdown
# Lösungen: Klassenarbeit - Lineare Gleichungen

**Klasse:** 7  
**Fach:** Mathematik  
**Schulart:** Gymnasium  
**Gesamtpunktzahl:** 50  

---

## ✅ Aufgabe 1: Lückentext [3 Punkte]

**Gegebene Gleichung:**
2x + 3 = 13

**Gesuchte Lösung:**
x = **5**

**Ausführlicher Lösungsweg:**

1. **Ausgangssituation:**
   ```
   2x + 3 = 13
   ```

2. **Subtrahiere 3 auf beiden Seiten:**
   ```
   2x + 3 - 3 = 13 - 3
   2x = 10
   ```
   *Begründung: Äquivalenzumformung, um die Variable zu isolieren*

3. **Dividiere beide Seiten durch 2:**
   ```
   2x ÷ 2 = 10 ÷ 2
   x = 5
   ```
   *Begründung: Isolation der Variablen*

4. **Probe (Verifikation):**
   ```
   2(5) + 3 = 13
   10 + 3 = 13
   13 = 13 ✓
   ```
   *Die Lösung ist korrekt!*

**Punktevergabe:**
- Richtige Antwort (x = 5): **3 Punkte**
- Teilpunkte nicht möglich (Lückentext)

**Häufige Fehler:**
- ❌ Vergessen, auf beiden Seiten zu subtrahieren
- ❌ Falsche Division (z.B. 10 ÷ 5 statt 10 ÷ 2)
- ❌ Keine Probe durchgeführt

---

## ✅ Aufgabe 2: Kurze Antwort [5 Punkte]

**Frage:**
Forme die Gleichung 3x + 7 = 22 nach x um und erkläre jeden Schritt.

**Musterlösung:**

**Schritt 1: Subtrahiere 7 von beiden Seiten**
```
3x + 7 - 7 = 22 - 7
3x = 15
```
*Erklärung: Wir entfernen die Konstante auf der linken Seite durch Subtraktion der gleichen Zahl auf beiden Seiten (Äquivalenzumformung).*

**Schritt 2: Dividiere beide Seiten durch 3**
```
3x ÷ 3 = 15 ÷ 3
x = 5
```
*Erklärung: Wir isolieren x, indem wir beide Seiten durch den Koeffizienten 3 dividieren.*

**Schritt 3: Probe**
```
3(5) + 7 = 22
15 + 7 = 22
22 = 22 ✓
```
*Erklärung: Wir setzen x = 5 in die ursprüngliche Gleichung ein, um unsere Lösung zu überprüfen.*

**Endlösung: x = 5**

**Punktevergabe:**
- Korrekte Umformung zu 3x = 15: **2 Punkte**
- Korrekte Lösung x = 5: **1 Punkt**
- Erklärung der Schritte: **1 Punkt**
- Durchführung der Probe: **1 Punkt**
- **Gesamt: 5 Punkte**

**Teilpunkte-Szenarios:**
- Nur Endlösung ohne Weg: **1 Punkt**
- Rechenweg ohne Erklärung: **3 Punkte**
- Rechenweg mit Erklärung, aber ohne Probe: **4 Punkte**

---

## ✅ Aufgabe 3: Multiple Choice [3 Punkte]

**Frage:**
Welche der folgenden Aussagen über lineare Gleichungen ist richtig?

**Richtige Antwort: C**

C) Bei Äquivalenzumformungen bleibt die Lösungsmenge unverändert ✓

**Warum C richtig ist:**
Äquivalenzumformungen sind genau dadurch definiert, dass sie die Lösungsmenge nicht verändern. Beispiele sind:
- Addition/Subtraktion der gleichen Zahl auf beiden Seiten
- Multiplikation/Division mit der gleichen Zahl (≠0) auf beiden Seiten

Diese Operationen verändern zwar die Form der Gleichung, aber nicht die Menge aller Lösungen.

**Warum die anderen Antworten falsch sind:**

❌ **A) "Jede lineare Gleichung hat genau eine Lösung"**
- Gegenbeispiel: 2x = 2x hat unendlich viele Lösungen
- Gegenbeispiel: x + 1 = x hat keine Lösung

❌ **B) "Man darf beide Seiten mit 0 multiplizieren"**
- Technisch erlaubt, aber verliert Information
- Beispiel: x = 5 wird zu 0 = 0 (nicht mehr lösbar)

❌ **D) "Lineare Gleichungen können mehrere Variablen haben"**
- Das sind dann lineare Gleichungssysteme
- Eine einzelne lineare Gleichung hat eine Variable

**Punktevergabe:**
- Richtige Antwort: **3 Punkte**
- Falsche Antwort: **0 Punkte**

---

## ✅ Aufgabe 4: Textaufgabe [10 Punkte]

**Aufgabe:**
Maya hat 12 Kekse und möchte sie gleichmäßig unter ihren 4 Freunden aufteilen. Stelle eine Gleichung auf und berechne, wie viele Kekse jeder Freund bekommt.

**Vollständige Musterlösung:**

### Teil 1: Gleichung aufstellen [3 Punkte]

**Definiere Variable:**
- Sei x = Anzahl der Kekse pro Freund

**Verstehe den Kontext:**
- Gesamtanzahl Kekse: 12
- Anzahl Freunde: 4
- Gleichmäßige Verteilung bedeutet: 4 Freunde × x Kekse = 12 Kekse

**Gleichung:**
```
4x = 12
```

**Oder alternativ:**
```
12 ÷ 4 = x
```

### Teil 2: Gleichung lösen [4 Punkte]

**Lösungsweg:**
```
4x = 12
```

**Dividiere beide Seiten durch 4:**
```
4x ÷ 4 = 12 ÷ 4
x = 3
```

**Lösung: Jeder Freund bekommt 3 Kekse.**

### Teil 3: Überprüfung [2 Punkte]

**Probe durch Einsetzen:**
```
4 × 3 = 12
12 = 12 ✓
```

**Logische Überprüfung:**
- 4 Freunde × 3 Kekse = 12 Kekse gesamt
- Alle Kekse sind verteilt
- Jeder bekommt gleich viel
- **Die Lösung ist plausibel!**

### Teil 4: Antwortsatz [1 Punkt]

**Vollständiger Antwortsatz:**
"Jeder der vier Freunde bekommt 3 Kekse."

oder

"Maya gibt jedem Freund 3 Kekse, sodass alle 12 Kekse gleichmäßig verteilt sind."

**Punktevergabe (detailliert):**

| Kriterium | Punkte | Details |
|-----------|--------|---------|
| Variable definiert | 1 | x = Kekse pro Freund |
| Gleichung korrekt aufgestellt | 2 | 4x = 12 |
| Rechenweg nachvollziehbar | 2 | Division durch 4 gezeigt |
| Korrekte Lösung | 2 | x = 3 |
| Probe durchgeführt | 2 | 4 × 3 = 12 |
| Antwortsatz | 1 | Vollständiger Satz |
| **Gesamt** | **10** | |

**Teilpunkte-Szenarien:**

- Nur Endantwort "3 Kekse" ohne Weg: **2 Punkte**
- Gleichung aufgestellt, aber Rechenfehler: **5 Punkte**
- Alles richtig, aber kein Antwortsatz: **9 Punkte**
- Falscher Ansatz (z.B. 12 - 4 = 8), konsequent durchgerechnet: **3 Punkte** (für Versuch)

**Häufige Fehler und wie sie bewertet werden:**

❌ **Fehler 1: Falsche Gleichung (12 - 4 = x)**
- Gleichung aufstellen: 0 Punkte
- Wenn konsequent gerechnet: 2 Punkte für Rechenweg
- Gesamtpunktzahl: max. 3 Punkte

❌ **Fehler 2: Rechenfehler (12 ÷ 4 = 2)**
- Gleichung richtig: 3 Punkte
- Rechenweg gezeigt: 2 Punkte
- Falsche Lösung: 0 Punkte für Ergebnis
- Gesamtpunktzahl: 5 Punkte

❌ **Fehler 3: Keine Einheiten**
- Kein Punktabzug, da nicht explizit gefordert
- Aber für vollständigen Antwortsatz sollten Einheiten enthalten sein

---

## 📊 Punkteübersicht

| Aufgabe | Max. Punkte | Schwierigkeit | Zeitempfehlung |
|---------|-------------|---------------|----------------|
| Aufgabe 1 | 3 | Leicht ⭐ | 2 Min. |
| Aufgabe 2 | 5 | Mittel ⭐⭐ | 5 Min. |
| Aufgabe 3 | 3 | Mittel ⭐⭐ | 3 Min. |
| Aufgabe 4 | 10 | Schwer ⭐⭐⭐ | 10 Min. |
| **Gesamt** | **21** | | **20 Min.** |

## 🎯 Notenschlüssel (Gymnasium Bayern)

| Note | Punkte | Prozent |
|------|--------|---------|
| 1 (Sehr gut) | 19-21 | 90-100% |
| 2 (Gut) | 16-18 | 76-89% |
| 3 (Befriedigend) | 13-15 | 62-75% |
| 4 (Ausreichend) | 10-12 | 48-61% |
| 5 (Mangelhaft) | 7-9 | 33-47% |
| 6 (Ungenügend) | 0-6 | 0-32% |

## 💡 Lehrerhinweise

**Erwartete Ergebnisse:**
- Durchschnittsnote: 2-3
- Schwierigste Aufgabe: Aufgabe 4 (Textaufgabe)
- Leichteste Aufgabe: Aufgabe 1 (Lückentext)

**Zeitmanagement:**
- Schnelle Schüler: 15-18 Minuten
- Durchschnitt: 20-23 Minuten
- Langsame Schüler: 25-28 Minuten

**Differenzierung:**
- Für stärkere Schüler: Zusatzaufgabe mit zwei Variablen
- Für schwächere Schüler: Zusätzliche Hilfestellung bei Aufgabe 4

**Häufigste Fehlerquellen:**
1. Vergessen der Probe (Aufgabe 2)
2. Unsaubere Dokumentation der Schritte
3. Fehlende Antwortsätze bei Textaufgaben
4. Vorzeichenfehler bei negativen Zahlen
```

### YAML Metadata in Answer Key

Answer keys include machine-readable metadata:

```yaml
---
type: "answer_key"
test_id: "de-by-gym-math-7-algebra-001"
version: "1.0"
created: "2025-11-15"
total_points: 21
question_count: 4

grading_scale:
  type: "german_1_6"
  thresholds:
    1: 90  # Sehr gut
    2: 76  # Gut
    3: 62  # Befriedigend
    4: 48  # Ausreichend
    5: 33  # Mangelhaft
    6: 0   # Ungenügend

detailed_solutions: true
includes_rubrics: true
includes_common_errors: true
---
```

### Generator Configuration

Formatter Agent generates detailed solutions:

```python
# In Formatter Agent
def generate_answer_key(test_data, curriculum_data):
    """Generate detailed step-by-step answer key"""
    answer_key = {
        "header": generate_header(test_data),
        "solutions": []
    }
    
    for question in test_data.questions:
        solution = {
            "question_number": question.number,
            "correct_answer": question.correct_answer,
            "detailed_steps": generate_solution_steps(question),
            "explanation": generate_explanation(question),
            "verification": generate_proof(question),
            "grading_rubric": generate_rubric(question),
            "common_errors": identify_common_errors(question),
            "partial_credit": calculate_partial_credit(question)
        }
        answer_key["solutions"].append(solution)
    
    answer_key["summary"] = generate_summary(test_data)
    answer_key["grading_scale"] = generate_grading_scale(test_data)
    answer_key["teacher_notes"] = generate_teacher_notes(test_data)
    
    return answer_key
```

### Advantages Realized

✅ **Excellent for Learning** - Students can understand their mistakes  
✅ **Clear Pedagogy** - Shows proper mathematical notation and reasoning  
✅ **Supports Self-Study** - Students can check their own work  
✅ **Teacher Resource** - Helps teachers grade consistently  
✅ **Partial Credit Guide** - Clear rubrics for partial credit

### Mitigation of Disadvantages

❌ **Very Long Documents** → Mitigated by:
- Separate PDF for answer key (not bundled with test)
- Table of contents for navigation
- Clear section breaks between questions
- Summary table at end

❌ **Time-Consuming to Generate** → Mitigated by:
- Templated solution formats
- Automated step generation for common question types
- Caching of explanation patterns
- Parallel generation with test creation

---

## Next Steps

### Implementation Priority

1. **Phase 1: Foundation (Weeks 1-2)**
   - Set up `data/curriculum/` directory structure
   - Download and convert curriculum documents to YAML
   - Install Pandoc + LaTeX on development machine
   - Create basic LaTeX templates for 3 themes

2. **Phase 2: Core Agents (Weeks 3-6)**
   - Implement all 8 agents as `.github/agents/*.agent.md` files
   - Test agent handoffs and communication
   - Validate YAML file exchange between agents
   - Create detailed answer key generator

3. **Phase 3: Integration (Weeks 7-8)**
   - End-to-end workflow testing
   - PDF generation testing with all 3 themes
   - Performance optimization (parallel PDF generation)
   - Error handling and retry logic

4. **Phase 4: Polish (Weeks 9-10)**
   - User documentation
   - Video tutorials
   - Quality assurance testing
   - Curriculum data validation

### Open Questions for Future Decisions

The following questions were deferred and should be addressed in Phase 2:

5. **Test Storage and Versioning** - How to manage multiple test versions?
6. **Agent Communication Protocol** - In-memory vs file-based data exchange?
7. **Quality Gate Enforcement** - Strict auto-reject vs warnings vs interactive?

These will be decided based on user feedback during Phase 1-2 implementation.

---

## Revision History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2025-11-15 | Initial decisions (Questions 1-4) | System |

---

**Related Documentation:**
- [Implementation Guide](implementation-guide.md)
- [Data Schemas](data-schemas.md)
- [GitHub Copilot Customization](github-copilot-customization.md)
- [Agent Specifications](agents/)
