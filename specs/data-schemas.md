# Data Schemas & File Formats

[← Back to Documentation Index](../README.md)

---

## Overview

This document defines exact data structures, file formats, and storage locations for all agent outputs.

---

## 1. Agent Output Locations

### 1.1 Directory Structure for Agent Outputs

```
create_tests/
├── tests/                           # Generated test files (MD + PDF)
│   ├── germany/
│   ├── usa/
│   └── uk/
├── pdfs/                            # DEPRECATED - PDFs now stored with tests/
│
├── .agent_workspace/                # Agent working directory (hidden)
│   ├── curriculum_research/
│   │   └── [country]_[region]_[school]_[subject]_[grade].yaml
│   ├── test_drafts/
│   │   └── [test_id]_draft_v[n].md
│   ├── validation_reports/
│   │   └── [test_id]_validation.yaml
│   ├── difficulty_analysis/
│   │   └── [test_id]_difficulty.yaml
│   ├── time_estimates/
│   │   └── [test_id]_timing.yaml
│   ├── reports/                     # Workflow execution reports
│   │   └── [test_id]_run_[timestamp].md
│   └── orchestrator_logs/
│       └── [session_id].log
│
└── index/                           # Metadata and indexes
    ├── test_index.json
    ├── by_subject.json
    ├── by_grade.json
    └── by_topic.json
```

---

## 2. Markdown Format Standards

### 2.1 Complete Test File Template

Every test file MUST follow this exact structure:

```markdown
---
# === METADATA HEADER (YAML) ===
# Required Fields
title: "Linear Equations Practice Test"
title_en: "Linear Equations Practice Test"  # English translation if different language

# Educational Context
subject: "Mathematik"
subject_en: "Mathematics"
country: "Germany"
region: "Bayern"
bundesland: "Bayern"
school_type: "Gymnasium"
klassenstufe: 7
grade_level: 7
age_range: "12-13"

# Test Properties
difficulty: "Medium"
question_count: 10
total_points: 50
estimated_time: 30  # minutes
language: "de"

# Curriculum Alignment
learning_objectives:
  - "Lösen einfacher linearer Gleichungen"
  - "Anwenden von Äquivalenzumformungen"
  - "Übersetzen von Sachaufgaben in Gleichungen"

curriculum_alignment:
  - "Lehrplan PLUS Bayern Gymnasium Klasse 7"
  - "KMK Bildungsstandards Mathematik"

standards:
  - "Kompetenzbereich: Mit symbolischen und formalen Elementen umgehen"

# Test Structure
difficulty_distribution:
  easy: 30    # percentage
  medium: 50
  hard: 20

question_types:
  - "multiple_choice"
  - "fill_blank"
  - "short_answer"

# Metadata
tags: ["mathematik", "algebra", "gleichungen", "klasse7", "gymnasium"]
created_by: "Test Designer Agent v1.0"
curriculum_researched_by: "Curriculum Research Agent v1.0"
validated_by: "Content Validator Agent v1.0"
date_created: "2025-11-15"
version: "1.0"
test_id: "de-by-gym-math-7-algebra-001"

# Optional Fields
variant: "practice"  # practice, exam, homework, quiz
time_of_year: "Q2"   # When typically administered
prerequisite_tests: []
related_tests: []
---

# Klassenarbeit: Lineare Gleichungen

**Klasse:** 7  
**Fach:** Mathematik  
**Schulart:** Gymnasium  
**Zeit:** 30 Minuten  
**Gesamtpunktzahl:** 50

**Name:** ________________  
**Datum:** ________________  
**Klasse:** ________________

---

## 📋 Anweisungen

- Lies jede Aufgabe sorgfältig durch
- Zeige deinen Lösungsweg
- Achte auf die Punkteverteilung
- Viel Erfolg! 🍀

---

## Aufgabe 1 [⭐ Leicht - 3 Punkte]

**Löse die Gleichung:**

x + 7 = 15

**Lösungsweg:**

_______________________________________

_______________________________________

**Lösung:** x = ________

**Thema:** Grundlagen linearer Gleichungen  
**Schwierigkeit:** Leicht  
**Geschätzte Zeit:** 2 Minuten

---

## Aufgabe 2 [⭐⭐ Mittel - 5 Punkte]

**Löse die Gleichung und mache die Probe:**

3x - 8 = 13

**Lösungsweg:**

_______________________________________

_______________________________________

_______________________________________

**Lösung:** x = ________

**Probe:**

_______________________________________

_______________________________________

**Thema:** Äquivalenzumformungen  
**Schwierigkeit:** Mittel  
**Geschätzte Zeit:** 4 Minuten

---

## Aufgabe 3 [⭐⭐ Mittel - 8 Punkte]

**Wähle die richtige Antwort:**

Welche der folgenden Gleichungen hat die Lösung x = 4?

- [ ] A) 2x + 3 = 9
- [ ] B) 5x - 10 = 10
- [ ] C) 3x + 1 = 12
- [ ] D) x/2 + 1 = 3

**Thema:** Gleichungen lösen  
**Schwierigkeit:** Mittel  
**Geschätzte Zeit:** 3 Minuten

---

## Aufgabe 4 [⭐⭐⭐ Schwer - 10 Punkte]

**Sachaufgabe:**

Lisa ist dreimal so alt wie ihr Bruder Tom. In 5 Jahren wird Lisa doppelt so alt sein wie Tom.

a) Stelle zwei Gleichungen auf. [4 Punkte]

**Gleichungen:**

1) _______________________________________

2) _______________________________________

b) Berechne das aktuelle Alter von Lisa und Tom. [6 Punkte]

**Lösungsweg:**

_______________________________________

_______________________________________

_______________________________________

_______________________________________

**Antwort:** Lisa ist _____ Jahre alt, Tom ist _____ Jahre alt.

**Thema:** Anwendungsaufgaben  
**Schwierigkeit:** Schwer  
**Geschätzte Zeit:** 8 Minuten

---

## 📊 Bewertungsschlüssel

| Punkte | Note | Bewertung |
|--------|------|-----------|
| 45-50 | 1 | Sehr gut 🌟🌟🌟 |
| 40-44 | 2 | Gut ⭐⭐ |
| 35-39 | 3 | Befriedigend ⭐ |
| 30-34 | 4 | Ausreichend ✓ |
| 25-29 | 5 | Mangelhaft |
| 0-24 | 6 | Ungenügend |

**Bestanden:** ab 30 Punkte (Note 4)

---

## 💡 Tipps zum Lernen

- Übe regelmäßig verschiedene Gleichungstypen
- Mache immer eine Probe deiner Lösung
- Achte auf die Vorzeichen bei Umformungen
- Zeichne bei Sachaufgaben eine Skizze

**Weiterführende Übungen:** Arbeitsblatt "Lineare Gleichungen - Fortgeschritten"

---

**Dokumentversion:** 1.0  
**Erstellt am:** 15.11.2025  
**Letzte Aktualisierung:** 15.11.2025
```

### 2.2 Answer Key File Template

```markdown
---
# === METADATA (same as main test) ===
title: "Linear Equations Practice Test - ANSWER KEY"
is_answer_key: true
parent_test_id: "de-by-gym-math-7-algebra-001"
# ... (all other metadata same as main test)
---

# Klassenarbeit: Lineare Gleichungen - LÖSUNGEN

**⚠️ LEHRERKOPIE - NUR FÜR LEHRKRÄFTE**

---

## 🔑 Aufgabe 1 [3 Punkte]

**Aufgabe:** Löse die Gleichung: x + 7 = 15

**✓ Musterlösung:**

```
x + 7 = 15    | -7
x = 8
```

**Antwort:** x = 8

**Bewertung:**
- Richtige Lösung: 3 Punkte
- Richtiger Ansatz, Rechenfehler: 2 Punkte
- Ansatz erkennbar, aber falsch: 1 Punkt

**Häufige Fehler:**
- Vergessen, auf beiden Seiten zu subtrahieren
- Vorzeichenfehler

**Schwierigkeit:** Leicht  
**Erwartete Erfolgsquote:** 90%

---

## 🔑 Aufgabe 2 [5 Punkte]

**Aufgabe:** Löse die Gleichung und mache die Probe: 3x - 8 = 13

**✓ Musterlösung:**

Lösungsweg:
```
3x - 8 = 13    | +8
3x = 21        | :3
x = 7
```

Probe:
```
3(7) - 8 = 13
21 - 8 = 13
13 = 13 ✓
```

**Antwort:** x = 7

**Bewertung:**
- Richtige Lösung mit Probe: 5 Punkte
- Richtige Lösung, Probe fehlt oder falsch: 3 Punkte
- Richtiger Ansatz, Rechenfehler: 2 Punkte
- Ansatz erkennbar: 1 Punkt

**Schwierigkeit:** Mittel  
**Erwartete Erfolgsquote:** 75%

---

## 🔑 Aufgabe 3 [8 Punkte]

**Aufgabe:** Welche Gleichung hat die Lösung x = 4?

**✓ Richtige Antwort:** B) 5x - 10 = 10

**Erklärung:**
- A) 2(4) + 3 = 11 ≠ 9
- B) 5(4) - 10 = 10 ✓ RICHTIG
- C) 3(4) + 1 = 13 ≠ 12
- D) 4/2 + 1 = 3 ✓ AUCH RICHTIG! (beide akzeptieren)

**⚠️ Hinweis:** Aufgabe hat zwei richtige Antworten (B und D). Beide voll bewerten!

**Bewertung:**
- Antwort B oder D: 8 Punkte
- Beide Antworten erkannt: 8 Punkte + Bonuspunkt
- Falsche Antwort mit korrekter Begründung: 4 Punkte

**Schwierigkeit:** Mittel  
**Erwartete Erfolgsquote:** 60%

---

## 🔑 Aufgabe 4 [10 Punkte]

**Sachaufgabe:** Lisa und Tom Altersaufgabe

**✓ Musterlösung:**

a) Gleichungen aufstellen: [4 Punkte]
```
Sei x = Toms aktuelles Alter
Dann ist 3x = Lisas aktuelles Alter

Gleichung 1: L = 3T
Gleichung 2: L + 5 = 2(T + 5)
```

b) Berechnung: [6 Punkte]
```
3T + 5 = 2(T + 5)
3T + 5 = 2T + 10
T = 5

L = 3T = 15
```

**Antwort:** Tom ist 5 Jahre alt, Lisa ist 15 Jahre alt.

**Bewertung:**
- Teil a) Gleichungen korrekt: 4 Punkte
- Teil a) eine Gleichung korrekt: 2 Punkte
- Teil b) richtige Lösung: 6 Punkte
- Teil b) richtiger Ansatz: 3 Punkte
- Teil b) nur Endresultat ohne Weg: 2 Punkte

**Probe (zur Kontrolle):**
- Jetzt: Lisa (15) = 3 × Tom (5) ✓
- In 5 Jahren: Lisa (20) = 2 × Tom (10) ✓

**Häufige Fehler:**
- Gleichungen vertauscht
- Falsche Variablendefinition
- Rechenfehler bei Auflösung

**Schwierigkeit:** Schwer  
**Erwartete Erfolgsquote:** 40%

---

## 📊 Statistik & Auswertung

**Erwartete Durchschnittspunktzahl:** 38 Punkte (76%)  
**Erwartete Durchschnittsnote:** 2,5

**Lernziele-Abdeckung:**
- ✓ Lösen einfacher Gleichungen: Aufgabe 1, 2
- ✓ Äquivalenzumformungen: Aufgabe 2, 3
- ✓ Sachaufgaben: Aufgabe 4
- ✓ Probe durchführen: Aufgabe 2

**Differenzierung:**
- Leichte Aufgaben (1): Basis für alle Schüler
- Mittlere Aufgaben (2, 3): Kern der Kompetenzen
- Schwere Aufgabe (4): Herausforderung für starke Schüler

---

## 👨‍🏫 Lehrerhinweise

**Zeitmanagement:**
- Aufgabe 1: ~2 Min
- Aufgabe 2: ~4 Min
- Aufgabe 3: ~3 Min
- Aufgabe 4: ~8 Min
- Puffer: ~13 Min
- **Gesamt:** 30 Minuten

**Vorbereitung:**
- Thema sollte in 4-5 Unterrichtsstunden behandelt worden sein
- Voraussetzung: Grundrechenarten sicher beherrscht
- Empfehlung: 1 Übungsstunde vor der Arbeit

**Nach der Korrektur:**
- Häufige Fehler in der Klasse besprechen
- Bei Bedarf Förderunterricht anbieten
- Schwere Aufgaben gemeinsam nachbesprechen

---

**Dokumentversion:** 1.0  
**Erstellt am:** 15.11.2025
```

---

## 3. Agent Data Exchange Schemas

### 3.0 Workflow Report Schema

**File:** `.agent_workspace/reports/[test_id]_run_[timestamp].md`

**Purpose:** Comprehensive execution report documenting all agent steps, decisions, metrics, and outputs for a complete test creation workflow.

**Template:** See `.agent_workspace/reports/TEMPLATE.md` for the complete structure.

**Key Sections:**
- **Overview:** Test parameters, IDs, timestamps
- **Step 1-9:** One section per agent (Orchestrator, Curriculum Fetcher, Curriculum Researcher, Test Designer, Content Validator, Difficulty Analyzer, Time Estimator, Formatter, PDF Generator)
- **Final Summary:** Overall status, file paths, quality metrics, recommendations

**Generated By:** Orchestrator Agent (initialized at workflow start, updated after each agent step, finalized at workflow completion)

**Used For:**
- Transparency and auditability
- Debugging and quality assurance
- Educator documentation
- Reproducibility
- Performance tracking

**Example Filename:** `de-ns-gym-eng-6-tenses-001_run_2025-11-16T10-23-00.md`

---

### 3.1 Curriculum Research Agent Output

**File:** `.agent_workspace/curriculum_research/[country]_[region]_[school]_[subject]_[grade].yaml`

```yaml
# Curriculum Research Output Schema
research_session:
  session_id: "curr_de_by_gym_math_7_20251115_103045"
  timestamp: "2025-11-15T10:30:45Z"
  agent_version: "1.0"
  
request:
  country: "Germany"
  region: "Bayern"
  bundesland: "Bayern"
  school_type: "Gymnasium"
  klassenstufe: 7
  subject: "Mathematik"
  topic: "Lineare Gleichungen"

curriculum_data:
  official_sources:
    - name: "Lehrplan PLUS Bayern"
      url: "https://www.lehrplanplus.bayern.de/..."
      document_version: "2024"
      access_date: "2025-11-15"
    
    - name: "KMK Bildungsstandards"
      url: "https://www.kmk.org/..."
      document_version: "2022"
      access_date: "2025-11-15"

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
    
    - id: "LO3"
      text_de: "Übersetzen von Sachaufgaben in Gleichungen"
      text_en: "Translating word problems into equations"
      bloom_level: "Analysis"
      curriculum_ref: "LP-PLUS-BY-GYM-M7-2.3.2"

  competency_areas:
    - name_de: "Mit symbolischen und formalen Elementen umgehen"
      name_en: "Working with symbolic and formal elements"
      weight: "high"
      curriculum_ref: "LP-PLUS-BY-GYM-M-K5"
    
    - name_de: "Mathematisch argumentieren"
      name_en: "Mathematical reasoning"
      weight: "medium"
      curriculum_ref: "LP-PLUS-BY-GYM-M-K1"

  content_scope:
    include:
      - "Einfache lineare Gleichungen (ax + b = c)"
      - "Gleichungen mit Variablen auf beiden Seiten"
      - "Sachaufgaben mit linearen Gleichungen"
      - "Proben durchführen"
    
    exclude:
      - "Quadratische Gleichungen (erst Klasse 9)"
      - "Gleichungssysteme (erst Klasse 8)"
      - "Bruchgleichungen (erst Klasse 8)"
    
    prerequisites:
      - "Grundrechenarten sicher beherrschen"
      - "Umgang mit Variablen (Terme)"
      - "Rechengesetze (Kommutativ-, Assoziativ-, Distributivgesetz)"

  difficulty_recommendations:
    distribution:
      easy: 30
      medium: 50
      hard: 20
    
    explanation: "Gymnasium Klasse 7 - Mittelstufe, akademisches Niveau"
    
    easy_characteristics:
      - "Einschrittige Gleichungen"
      - "Ganzzahlige Lösungen"
      - "Klare Formulierung"
    
    medium_characteristics:
      - "Zweischrittige Gleichungen"
      - "Variable auf beiden Seiten"
      - "Sachaufgaben mit klarem Kontext"
    
    hard_characteristics:
      - "Mehrschrittige Gleichungen"
      - "Komplexe Sachaufgaben"
      - "Transfer zu neuen Situationen"

  terminology:
    mathematical_terms:
      - german: "Gleichung"
        english: "Equation"
        symbol: "="
        usage: "x + 3 = 7"
      
      - german: "Variable"
        english: "Variable"
        symbol: "x, y, z"
        usage: "Die unbekannte Größe"
      
      - german: "Äquivalenzumformung"
        english: "Equivalent transformation"
        symbol: "⇔"
        usage: "Umformung ohne Änderung der Lösungsmenge"
      
      - german: "Probe"
        english: "Check/Verification"
        usage: "Einsetzen der Lösung zur Überprüfung"

  regional_specifics:
    language: "de"
    formality_level: "Sie" # or "du" for younger grades
    notation_conventions:
      decimal_separator: ","  # 3,14 not 3.14
      thousands_separator: "."  # 1.000 not 1,000
      multiplication: "·"  # 3·x not 3*x or 3×x
    
    grading_scale:
      type: "1-6"
      best: 1
      passing: 4
      failing: [5, 6]
      description:
        1: "Sehr gut"
        2: "Gut"
        3: "Befriedigend"
        4: "Ausreichend"
        5: "Mangelhaft"
        6: "Ungenügend"
    
    cultural_context:
      currency: "EUR"
      measurement_system: "metric"
      date_format: "DD.MM.YYYY"
      appropriate_names:
        - "Lisa"
        - "Tom"
        - "Anna"
        - "Max"
        - "Sophie"
        - "Leon"
      appropriate_scenarios:
        - "Fußball (soccer)"
        - "Schule"
        - "Familie"
        - "Einkaufen"

  assessment_criteria:
    question_types_recommended:
      - type: "fill_blank"
        percentage: 30
        reason: "Tests direct recall and application"
      
      - type: "short_answer"
        percentage: 40
        reason: "Shows understanding of process"
      
      - type: "multiple_choice"
        percentage: 20
        reason: "Quick concept checking"
      
      - type: "word_problem"
        percentage: 10
        reason: "Application to real-world context"
    
    cognitive_levels:
      reproduction: 30  # Remember, Understand
      connection: 50    # Apply, Analyze
      reflection: 20    # Evaluate, Create

  vocabulary_guidelines:
    reading_level: "Grade 7"
    max_sentence_length: 20  # words
    avoid_terms:
      - "Kongruenz (zu fortgeschritten)"
      - "Isomorphismus (zu fortgeschritten)"
    
    required_terms:
      - "Gleichung"
      - "Variable"
      - "Lösung"
      - "Äquivalenzumformung"

research_quality:
  confidence_score: 0.95
  sources_verified: true
  curriculum_current: true
  warnings: []
  
  validation_checks:
    official_source: true
    grade_appropriate: true
    school_type_match: true
    regional_specific: true

metadata:
  research_duration: 45  # seconds
  sources_accessed: 3
  last_curriculum_update: "2024-09-01"
  next_review_date: "2026-09-01"
```

### 3.2 Test Designer Agent Output

**File:** `.agent_workspace/test_drafts/[test_id]_draft_v[n].md`

This is a Markdown file following the complete template shown in section 2.1 above.

**Companion Metadata File:** `.agent_workspace/test_drafts/[test_id]_draft_v[n]_meta.yaml`

```yaml
# Test Draft Metadata
draft_info:
  test_id: "de-by-gym-math-7-algebra-001"
  draft_version: 1
  status: "pending_validation"  # draft, pending_validation, validated, rejected, final
  created_at: "2025-11-15T10:35:22Z"
  agent_version: "Test Designer Agent v1.0"

generation_details:
  curriculum_research_id: "curr_de_by_gym_math_7_20251115_103045"
  generation_strategy: "balanced_distribution"
  randomization_seed: 42
  
  question_generation:
    - question_number: 1
      type: "fill_blank"
      difficulty: "easy"
      learning_objective: "LO1"
      generation_method: "template_based"
      alternatives_generated: 3
      selected_reason: "Clearest wording"
    
    - question_number: 2
      type: "short_answer"
      difficulty: "medium"
      learning_objective: "LO2"
      generation_method: "curriculum_aligned"
      alternatives_generated: 2
      selected_reason: "Best demonstrates competency"
    
    - question_number: 3
      type: "multiple_choice"
      difficulty: "medium"
      learning_objective: "LO1"
      generation_method: "distractor_analysis"
      alternatives_generated: 4
      selected_reason: "Balanced distractors"
    
    - question_number: 4
      type: "word_problem"
      difficulty: "hard"
      learning_objective: "LO3"
      generation_method: "real_world_scenario"
      alternatives_generated: 2
      selected_reason: "Age-appropriate context"

quality_checks:
  total_points: 50
  question_count: 4
  difficulty_distribution:
    easy: 25     # 1 question, 3 points
    medium: 50   # 2 questions, 13 points
    hard: 25     # 1 question, 10 points
  
  learning_objectives_coverage:
    LO1: ["Q1", "Q3"]
    LO2: ["Q2"]
    LO3: ["Q4"]
  
  question_types_used:
    - "fill_blank"
    - "short_answer"
    - "multiple_choice"
    - "word_problem"

gamification_elements:
  emojis_used: true
  difficulty_stars: true
  encouraging_messages: true
  learning_tips: true
  progress_indicators: false  # not applicable for static test

next_steps:
  - "Content validation"
  - "Difficulty analysis"
  - "Time estimation"
  - "Formatting"
```

### 3.3 Content Validator Agent Output

**File:** `.agent_workspace/validation_reports/[test_id]_validation.yaml`

```yaml
# Content Validation Report
validation_session:
  test_id: "de-by-gym-math-7-algebra-001"
  draft_version: 1
  validation_timestamp: "2025-11-15T10:40:18Z"
  validator_version: "Content Validator Agent v1.0"
  
overall_status: "PASS_WITH_WARNINGS"  # PASS, PASS_WITH_WARNINGS, FAIL, NEEDS_REVISION

validation_results:
  
  accuracy_check:
    status: "PASS"
    score: 100
    issues: []
    details:
      factual_accuracy: "All mathematical content verified"
      answer_correctness: "All answers checked and correct"
      calculation_verification: "Manual and automated checks passed"
  
  age_appropriateness:
    status: "PASS"
    score: 95
    issues: []
    details:
      language_level: "Appropriate for Grade 7"
      vocabulary_complexity: "Within grade level"
      sentence_structure: "Clear and accessible"
      flesch_kincaid_score: 7.2  # Grade level
  
  clarity_check:
    status: "PASS_WITH_WARNINGS"
    score: 90
    issues:
      - question_id: "Q3"
        severity: "minor"
        issue: "Question has two correct answers (B and D)"
        suggestion: "Clarify instructions or modify options"
        auto_fixable: false
    details:
      question_clarity: "Most questions unambiguous"
      instruction_clarity: "Instructions clear"
      answer_option_distinctness: "Options distinct in most cases"
  
  bias_check:
    status: "PASS"
    score: 100
    issues: []
    details:
      cultural_bias: "None detected"
      gender_bias: "Balanced names (Lisa, Tom)"
      socioeconomic_bias: "Scenarios accessible to all"
      religious_bias: "None detected"
      regional_bias: "Appropriate for target region"
  
  curriculum_alignment:
    status: "PASS"
    score: 100
    issues: []
    details:
      learning_objectives_covered:
        LO1: "Fully covered (Q1, Q3)"
        LO2: "Fully covered (Q2)"
        LO3: "Fully covered (Q4)"
      curriculum_standards_met:
        - "LP-PLUS-BY-GYM-M7-2.3"
        - "KMK Bildungsstandards"
      competency_levels_appropriate: true
  
  format_check:
    status: "PASS"
    score: 100
    issues: []
    details:
      markdown_syntax: "Valid"
      metadata_complete: true
      structure_consistent: true
      heading_hierarchy: "Correct"
      point_values_present: true
      point_values_sum: 50  # matches total_points
  
  answer_key_validation:
    status: "PASS"
    score: 100
    issues: []
    details:
      all_questions_answered: true
      explanations_present: true
      explanations_clear: true
      grading_rubrics_complete: true
      common_errors_noted: true

recommendations:
  critical: []
  
  important:
    - issue: "Question 3 has two valid answers"
      action: "Update instructions to accept both B and D, or modify options"
      priority: "high"
  
  suggested:
    - issue: "Could add more visual elements for engagement"
      action: "Consider adding diagrams for Question 4"
      priority: "low"
    
    - issue: "Answer key very detailed (good!)"
      action: "Maintain this level of detail for teacher support"
      priority: "info"

validation_statistics:
  total_checks: 45
  checks_passed: 44
  checks_warning: 1
  checks_failed: 0
  
  time_taken: 12  # seconds
  automated_checks: 35
  manual_review_checks: 10

sign_off:
  validated_by: "Content Validator Agent v1.0"
  ready_for_next_stage: true
  requires_revision: false
  requires_human_review: false  # only for FAIL status
```

### 3.4 Difficulty Analyzer Agent Output

**File:** `.agent_workspace/difficulty_analysis/[test_id]_difficulty.yaml`

```yaml
# Difficulty Analysis Report
analysis_session:
  test_id: "de-by-gym-math-7-algebra-001"
  analysis_timestamp: "2025-11-15T10:42:30Z"
  analyzer_version: "Difficulty Analyzer Agent v1.0"

target_parameters:
  school_type: "Gymnasium"
  grade_level: 7
  student_skill_level: "average"
  desired_distribution:
    easy: 30
    medium: 50
    hard: 20

per_question_analysis:
  - question_id: "Q1"
    question_number: 1
    assessed_difficulty: "easy"
    difficulty_score: 1.5  # scale 0-10
    confidence: 0.95
    
    factors:
      cognitive_complexity: 1  # Single-step
      linguistic_complexity: 1  # Simple wording
      content_complexity: 1    # Basic concept
      steps_required: 1
      bloom_level: "Apply"
    
    calculation:
      base_score: 1.0
      school_multiplier: 1.0   # Gymnasium = 1.0
      complexity_adjustment: 0.5
      final_score: 1.5
    
    expected_success_rate: 0.90
    recommended_time: 2  # minutes
  
  - question_id: "Q2"
    question_number: 2
    assessed_difficulty: "medium"
    difficulty_score: 4.0
    confidence: 0.92
    
    factors:
      cognitive_complexity: 2  # Multi-step with verification
      linguistic_complexity: 1  # Clear wording
      content_complexity: 2    # Intermediate concept
      steps_required: 3
      bloom_level: "Apply"
    
    calculation:
      base_score: 2.5
      school_multiplier: 1.0
      complexity_adjustment: 1.5
      final_score: 4.0
    
    expected_success_rate: 0.75
    recommended_time: 4
  
  - question_id: "Q3"
    question_number: 3
    assessed_difficulty: "medium"
    difficulty_score: 4.5
    confidence: 0.88
    
    factors:
      cognitive_complexity: 2  # Testing multiple equations
      linguistic_complexity: 2  # Need to check all options
      content_complexity: 2    # Requires calculation
      steps_required: 4        # Check each option
      bloom_level: "Analyze"
    
    calculation:
      base_score: 3.0
      school_multiplier: 1.0
      complexity_adjustment: 1.5
      final_score: 4.5
    
    expected_success_rate: 0.60
    recommended_time: 3
    
    notes: "Two correct answers detected - may be easier than assessed"
  
  - question_id: "Q4"
    question_number: 4
    assessed_difficulty: "hard"
    difficulty_score: 7.5
    confidence: 0.91
    
    factors:
      cognitive_complexity: 3  # Multi-step word problem
      linguistic_complexity: 3  # Complex scenario
      content_complexity: 3    # Advanced application
      steps_required: 6        # Multiple equations, solving
      bloom_level: "Analyze/Create"
    
    calculation:
      base_score: 5.0
      school_multiplier: 1.0
      complexity_adjustment: 2.5
      final_score: 7.5
    
    expected_success_rate: 0.40
    recommended_time: 8

overall_analysis:
  actual_distribution:
    easy: 25.0    # Q1: 3 points / 50 total
    medium: 50.0  # Q2+Q3: 13 points / 50 total  
    hard: 25.0    # Q4: 10 points / 50 total
  
  target_distribution:
    easy: 30.0
    medium: 50.0
    hard: 20.0
  
  distribution_variance:
    easy: -5.0    # 5% under target
    medium: 0.0   # Exactly on target
    hard: +5.0    # 5% over target
  
  meets_target: true
  within_tolerance: true  # ±10%
  
  average_difficulty: 4.4  # Overall test difficulty (0-10 scale)
  difficulty_rating: "Medium"  # Easy, Medium, Hard, Very Hard
  
  expected_average_score: 0.76  # 76% - based on weighted success rates
  expected_average_grade: 2.0   # German grading: 2 = "Gut"

balance_assessment:
  is_balanced: true
  progression: "appropriate"  # easy → medium → hard
  gap_analysis: "No large gaps in difficulty"
  
  recommendations:
    - "Distribution is well-balanced"
    - "Slight excess in hard category (+5%) is acceptable for Gymnasium"
    - "Consider adding one more easy question if targeting below-average students"

adjustment_suggestions:
  needed: false
  
  if_adjustment_needed:
    - action: "Reduce Q4 complexity slightly"
      impact: "Would move 5% from hard to medium"
      priority: "optional"

comparative_analysis:
  compared_to_grade_level: "appropriate"
  compared_to_school_type: "appropriate for Gymnasium"
  compared_to_similar_tests: "standard difficulty"

metadata:
  analysis_duration: 8  # seconds
  questions_analyzed: 4
  algorithms_used:
    - "cognitive_complexity_assessment"
    - "bloom_taxonomy_mapping"
    - "difficulty_score_calculation"
    - "distribution_analysis"
```

### 3.5 Time Estimation Agent Output

**File:** `.agent_workspace/time_estimates/[test_id]_timing.yaml`

```yaml
# Time Estimation Report
estimation_session:
  test_id: "de-by-gym-math-7-algebra-001"
  estimation_timestamp: "2025-11-15T10:44:15Z"
  estimator_version: "Time Estimation Agent v1.0"

input_parameters:
  school_type: "Gymnasium"
  grade_level: 7
  age_range: "12-13"
  target_duration: 30  # minutes
  student_skill_levels:
    - "below_average"
    - "average"
    - "advanced"

base_time_calculations:
  question_1:
    question_type: "fill_blank"
    difficulty: "easy"
    base_time: 1.5  # minutes
    
    multipliers:
      difficulty: 0.8      # easy = 0.8
      school_type: 1.0     # Gymnasium = 1.0
      skill_level_avg: 1.0 # average = 1.0
    
    estimated_times:
      below_average: 2.3
      average: 1.8
      advanced: 1.4
    
    reading_time: 0.3
    calculation_time: 1.2
    writing_time: 0.3
    
  question_2:
    question_type: "short_answer"
    difficulty: "medium"
    base_time: 3.0
    
    multipliers:
      difficulty: 1.0
      school_type: 1.0
      skill_level_avg: 1.0
    
    estimated_times:
      below_average: 5.4
      average: 4.5
      advanced: 3.4
    
    reading_time: 0.5
    calculation_time: 3.0
    writing_time: 1.0
  
  question_3:
    question_type: "multiple_choice"
    difficulty: "medium"
    base_time: 1.5
    
    multipliers:
      difficulty: 1.0
      school_type: 1.0
      skill_level_avg: 1.0
    
    estimated_times:
      below_average: 3.4
      average: 3.0
      advanced: 2.3
    
    reading_time: 0.5
    calculation_time: 2.0  # Check each option
    selection_time: 0.5
  
  question_4:
    question_type: "word_problem"
    difficulty: "hard"
    base_time: 4.0
    
    multipliers:
      difficulty: 1.5
      school_type: 1.0
      skill_level_avg: 1.0
    
    estimated_times:
      below_average: 12.0
      average: 10.0
      advanced: 7.5
    
    context_reading_time: 1.5
    equation_setup_time: 3.0
    calculation_time: 4.0
    writing_time: 1.5

total_time_estimates:
  below_average:
    pure_work_time: 23.1
    buffer_15_percent: 26.6
    buffer_20_percent: 27.7
    recommended: 28.0
  
  average:
    pure_work_time: 19.3
    buffer_15_percent: 22.2
    buffer_20_percent: 23.2
    recommended: 23.0
  
  advanced:
    pure_work_time: 14.6
    buffer_15_percent: 16.8
    buffer_20_percent: 17.5
    recommended: 17.0
  
  overall_recommendation: 30.0  # Target from curriculum

feasibility_analysis:
  target_duration: 30
  
  for_below_average:
    estimated_time: 28.0
    fits_target: true
    margin: 2.0  # minutes spare
    percentage_used: 93.3
    assessment: "Tight but feasible"
  
  for_average:
    estimated_time: 23.0
    fits_target: true
    margin: 7.0
    percentage_used: 76.7
    assessment: "Comfortable"
  
  for_advanced:
    estimated_time: 17.0
    fits_target: true
    margin: 13.0
    percentage_used: 56.7
    assessment: "Plenty of time"

concentration_span_check:
  age_group: "12-13"
  max_recommended_duration: 60  # minutes for this age
  test_duration: 30
  within_limits: true
  
  recommendation: "Duration appropriate for age group"
  breaks_needed: false

time_pressure_analysis:
  overall_pressure: "low_to_moderate"
  
  per_question_pressure:
    Q1: "low"
    Q2: "moderate"
    Q3: "low"
    Q4: "moderate_to_high"
  
  pacing_guidance:
    - "Students should spend ~2 min on Q1"
    - "Allow ~4-5 min for Q2"
    - "Q3 should take ~3 min"
    - "Reserve 8-10 min for Q4"
    - "Leave 5-10 min for review"

adjustments_needed:
  required: false
  
  if_target_was_20_minutes:
    action: "Remove Q4 or simplify Q2 and Q3"
    reason: "Would exceed time for below-average students"
  
  if_target_was_45_minutes:
    action: "Could add 2-3 more medium questions"
    reason: "Extra capacity available"

validation_results:
  meets_target_duration: true
  appropriate_for_age: true
  reasonable_pacing: true
  no_time_pressure_concerns: true
  
  overall_status: "APPROVED"

recommendations:
  for_teachers:
    - "Announce time allocations: Q1(2min), Q2(5min), Q3(3min), Q4(10min)"
    - "Remind students to watch time after Q2 (10 min mark)"
    - "Slower students may need encouragement on Q4"
  
  for_students:
    - "Don't spend more than 2 minutes on Q1"
    - "If stuck on Q4, move on and return if time permits"
    - "Save 5 minutes at end for review"

metadata:
  estimation_duration: 6  # seconds
  formulas_used:
    - "base_time × difficulty_mult × school_mult × skill_mult"
    - "total_time × (1 + buffer_percentage)"
  
  accuracy_confidence: 0.85
  based_on_data: "Empirical studies + expert input"
```

---

## 4. Index File Formats

### 4.1 Master Test Index

**File:** `index/test_index.json`

```json
{
  "metadata": {
    "version": "1.0",
    "last_updated": "2025-11-15T10:45:00Z",
    "total_tests": 1,
    "index_schema_version": "1.0"
  },
  
  "tests": [
    {
      "test_id": "de-by-gym-math-7-algebra-001",
      "title": "Lineare Gleichungen - Übungstest",
      "title_en": "Linear Equations - Practice Test",
      
      "paths": {
        "markdown": "tests/germany/bayern/gymnasium/mathematik/klasse_7/algebra/lineare_gleichungen.md",
        "markdown_key": "tests/germany/bayern/gymnasium/mathematik/klasse_7/algebra/lineare_gleichungen_key.md",
        "pdf_student": "tests/germany/bayern/gymnasium/mathematik/klasse_7/algebra/lineare_gleichungen.pdf",
        "pdf_key": "tests/germany/bayern/gymnasium/mathematik/klasse_7/algebra/lineare_gleichungen_key.pdf"
      },
      
      "educational_context": {
        "country": "Germany",
        "region": "Bayern",
        "school_type": "Gymnasium",
        "grade_level": 7,
        "klassenstufe": 7,
        "subject": "Mathematik",
        "subject_en": "Mathematics",
        "topic": "Lineare Gleichungen",
        "topic_en": "Linear Equations",
        "language": "de"
      },
      
      "test_properties": {
        "difficulty": "Medium",
        "question_count": 4,
        "total_points": 50,
        "estimated_time_minutes": 30,
        "variant": "practice"
      },
      
      "curriculum": {
        "learning_objectives": [
          "Lösen einfacher linearer Gleichungen",
          "Anwenden von Äquivalenzumformungen",
          "Übersetzen von Sachaufgaben in Gleichungen"
        ],
        "curriculum_alignment": [
          "Lehrplan PLUS Bayern Gymnasium Klasse 7",
          "KMK Bildungsstandards Mathematik"
        ]
      },
      
      "metadata": {
        "created_date": "2025-11-15",
        "created_by": "Test Designer Agent v1.0",
        "version": "1.0",
        "tags": ["mathematik", "algebra", "gleichungen", "klasse7", "gymnasium"],
        "downloads": 0,
        "ratings": {
          "average": 0,
          "count": 0
        }
      }
    }
  ]
}
```

---

## 5. File Naming Standards

### 5.1 Test Files

```
Pattern: [topic_name]_[variant].md

Examples:
- lineare_gleichungen.md
- lineare_gleichungen_practice.md
- lineare_gleichungen_advanced.md
- photosynthesis_basics.md
- cell_structure.md
```

### 5.2 Agent Workspace Files

```
Curriculum Research: [country]_[region]_[school]_[subject]_[grade].yaml
Test Draft: [test_id]_draft_v[n].md
Draft Metadata: [test_id]_draft_v[n]_meta.yaml
Validation Report: [test_id]_validation.yaml
Difficulty Analysis: [test_id]_difficulty.yaml
Time Estimation: [test_id]_timing.yaml
Orchestrator Log: [session_id].log
```

### 5.3 PDF Files

```
Pattern: [Subject]_[Topic]_Grade[X]_[Type].pdf

Examples:
- Math_LinearEquations_Grade7_Student.pdf
- Math_LinearEquations_Grade7_AnswerKey.pdf
- Science_Photosynthesis_Grade5_Student.pdf
```

---

## 6. Agent Communication Protocol

### 6.1 Message Format

Agents communicate via YAML files in `.agent_workspace/messages/`

```yaml
# Message from one agent to another
message:
  message_id: "msg_20251115_104530_001"
  timestamp: "2025-11-15T10:45:30Z"
  from_agent: "Test Designer Agent"
  to_agent: "Content Validator Agent"
  message_type: "request_validation"
  priority: "normal"  # low, normal, high, urgent
  
  payload:
    test_id: "de-by-gym-math-7-algebra-001"
    draft_version: 1
    draft_file: ".agent_workspace/test_drafts/de-by-gym-math-7-algebra-001_draft_v1.md"
    metadata_file: ".agent_workspace/test_drafts/de-by-gym-math-7-algebra-001_draft_v1_meta.yaml"
    
    validation_requirements:
      - "factual_accuracy"
      - "age_appropriateness"
      - "clarity"
      - "bias_check"
      - "curriculum_alignment"
    
    context:
      curriculum_research_id: "curr_de_by_gym_math_7_20251115_103045"
      target_completion: "2025-11-15T11:00:00Z"
  
  response_expected: true
  response_timeout: 300  # seconds
```

---

## Related Documentation

- [Main Specifications](./main-spec.md)
- [Agent Collaboration Protocol](./agent-collaboration.md)
- [All Agent Specifications](./agents/)

---

**Version:** 1.0  
**Last Updated:** November 15, 2025
