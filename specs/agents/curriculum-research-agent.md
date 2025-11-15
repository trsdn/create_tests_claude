# Curriculum Research Agent Specification

[← Back to Main Documentation](../../README.md)

---

## Overview

The Curriculum Research Agent identifies and researches relevant curriculum standards, learning objectives, and regional education requirements to ensure tests are properly aligned with official educational guidelines.

---

## Responsibilities

- Research official curriculum documents
- Extract learning objectives for specific topics
- Map content to grade-level standards
- Identify regional/state-specific requirements
- Determine appropriate vocabulary and complexity levels
- Validate prerequisite knowledge requirements
- Provide competency frameworks

---

## Inputs

- Country/region (e.g., Germany/Bayern, USA/California)
- School type (e.g., Gymnasium, Elementary School)
- Grade level / Klassenstufe
- Subject area
- Topic/subtopic
- Any specific curriculum references

---

## Outputs

```yaml
curriculum_data:
  learning_objectives:
    - "Lösen einfacher linearer Gleichungen"
    - "Anwenden von Äquivalenzumformungen"
  
  competencies:
    - "Mathematisch argumentieren"
    - "Probleme mathematisch lösen"
  
  assessment_criteria:
    reproduction: 30%
    connection: 50%
    reflection: 20%
  
  vocabulary_level: "Grade 7 German students"
  difficulty_range: "Medium to Advanced (Gymnasium)"
  prerequisites:
    - "Grundrechenarten"
    - "Umgang mit Variablen"
  
  regional_specifics:
    bundesland: "Bayern"
    curriculum_doc: "Lehrplan PLUS"
    standards: ["KMK Bildungsstandards"]
```

---

## Research Process

### Step 1: Identify Educational Context

```python
def identify_context(inputs):
    """Validate and normalize educational context"""
    return {
        'country': normalize_country(inputs.country),
        'region': get_region(inputs.region),
        'school_type': map_school_type(inputs.school_type),
        'grade': normalize_grade(inputs.grade_level),
        'subject': normalize_subject(inputs.subject)
    }
```

### Step 2: Fetch Official Curriculum

- Access ministry of education websites
- Download relevant curriculum documents
- Identify competency frameworks
- Note assessment standards

### Step 3: Extract Learning Objectives

- Map topic to curriculum sections
- Identify specific learning objectives
- Determine bloom's taxonomy levels
- Note prerequisite knowledge

### Step 4: Determine Appropriate Complexity

- Vocabulary level for age group
- Mathematical notation conventions
- Question difficulty distribution
- Real-world context appropriateness

### Step 5: Return Structured Data

Provide comprehensive curriculum alignment data to Test Designer Agent.

---

## German Education System Knowledge

### Bundesländer (Federal States)

**16 Bundesländer with distinct curricula:**
- Bayern (Bavaria) - Lehrplan PLUS
- Nordrhein-Westfalen (NRW) - Kernlehrpläne
- Baden-Württemberg - Bildungspläne
- Hessen, Niedersachsen, Berlin, etc.

### School Types

- **Grundschule** (Primary, Grades 1-4)
- **Hauptschule** (Basic secondary, Grades 5-9/10)
- **Realschule** (Intermediate secondary, Grades 5-10)
- **Gymnasium** (Academic secondary, Grades 5-12/13)
- **Gesamtschule** (Comprehensive, Grades 5-10/13)

### Klassenstufe Mapping

- Klassenstufe 1-4: Grundschule
- Klassenstufe 5-6: Orientierungsstufe
- Klassenstufe 7-10: Mittelstufe
- Klassenstufe 11-13: Oberstufe (Gymnasium only)

---

## International Curriculum Support

### USA

**Common Core State Standards:**
- CCSS.MATH.CONTENT.7.EE.A.1 (Apply properties)
- CCSS.MATH.CONTENT.7.EE.B.4 (Solve linear equations)

**Next Generation Science Standards (NGSS):**
- MS-PS1: Matter and Its Interactions
- MS-LS1: From Molecules to Organisms

**State-Specific:**
- California, Texas, Florida, New York variations

### UK

**National Curriculum:**
- Key Stage 1 (Years 1-2, Ages 5-7)
- Key Stage 2 (Years 3-6, Ages 7-11)
- Key Stage 3 (Years 7-9, Ages 11-14)
- Key Stage 4 (Years 10-11, Ages 14-16, GCSE)

---

## Subject-Specific Standards

### Mathematics (Mathematik)

**Klassenstufe 5 (Gymnasium, Bayern):**
- Natürliche Zahlen
- Grundrechenarten
- Geometrische Grundbegriffe
- Größen und Messen

**Klassenstufe 8 (Gymnasium, NRW):**
- Lineare Funktionen
- Terme und Gleichungen
- Prozentrechnung
- Körperberechnung

### Science (Naturwissenschaften)

**Biologie Klassenstufe 7:**
- Ökosysteme
- Zellbiologie
- Evolution basics
- Humanbiologie

**Physik Klassenstufe 9:**
- Mechanik
- Elektrizitätslehre
- Wärmelehre

---

## Reverse Interviewing Questions

The Curriculum Research Agent may ask:

### If curriculum source unclear:
- "Should I use the current 2025 curriculum or a specific version?"
- "Are there specific curriculum documents you want me to reference?"

### If subject area broad:
- "Should this cover general [subject] or focus on [specific subtopic]?"
- "Which curriculum strand should I prioritize?"

### If standards ambiguous:
- "Should I align with KMK Bildungsstandards or Bundesland-specific standards?"
- "Do you want competency-based or content-based alignment?"

### If difficulty level unclear:
- "Should this be basic/foundational, intermediate, or advanced for this grade?"

---

## Regional Adaptation Guidelines

### Language Considerations

**German Tests:**
- Use correct German mathematical terminology
- Follow German punctuation rules
- Use metric system exclusively
- Include Umlaute (ä, ö, ü) and ß

### Cultural Adaptation

- Use culturally relevant examples
- Reference local geography/history
- Adapt names to reflect demographics
- Use region-specific currencies
- Consider local holidays

---

## Terminology Mapping

**Mathematics (English → German):**
- Addition → Addition
- Subtraction → Subtraktion
- Multiplication → Multiplikation
- Division → Division
- Equation → Gleichung
- Function → Funktion
- Variable → Variable

**Question Formats:**
- Multiple Choice → Multiple Choice / Mehrfachauswahl
- True/False → Richtig/Falsch or Wahr/Falsch
- Fill in the blank → Lückentext
- Short answer → Kurzantwort

---

## Related Agents

- [Orchestrator Agent](./orchestrator-agent.md)
- [Test Designer Agent](./test-designer-agent.md)
- [Content Validator Agent](./content-validator-agent.md)

---

## See Also

- [Curriculum & Regional Specifications](../curriculum-regional-spec.md)
- [Repository Organization](../repository-organization.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
