# Repository Organization & Storage Structure

[← Back to Documentation Index](../README.md)

---

## Overview

This document defines the file and directory organization system for storing test files, answer keys, PDFs, and related resources.

---

## 1. Directory Hierarchy

### 1.1 Organization Principle

Tests are organized by: **Country → Region → School Type → Subject → Grade → Topic**

### 1.2 Complete Directory Structure

```
tests/
├── germany/
│   ├── bayern/
│   │   ├── gymnasium/
│   │   │   ├── mathematik/
│   │   │   │   ├── klasse_5/
│   │   │   │   │   ├── grundrechenarten/
│   │   │   │   │   │   ├── addition_subtraktion.md
│   │   │   │   │   │   ├── addition_subtraktion_key.md
│   │   │   │   │   │   └── multiplikation_division.md
│   │   │   │   │   └── geometrie/
│   │   │   │   │       └── grundformen.md
│   │   │   │   ├── klasse_7/
│   │   │   │   │   ├── algebra/
│   │   │   │   │   │   ├── lineare_gleichungen.md
│   │   │   │   │   │   └── terme_vereinfachen.md
│   │   │   │   │   └── geometrie/
│   │   │   │   │       └── dreieck_berechnungen.md
│   │   │   │   └── klasse_11/
│   │   │   │       └── analysis/
│   │   │   │           └── differentialrechnung.md
│   │   │   ├── physik/
│   │   │   │   └── klasse_9/
│   │   │   │       ├── mechanik/
│   │   │   │       │   └── kraftbegriff.md
│   │   │   │       └── elektrizitaet/
│   │   │   │           └── stromkreis.md
│   │   │   └── deutsch/
│   │   │       └── klasse_6/
│   │   │           └── grammatik/
│   │   │               └── satzglieder.md
│   │   ├── realschule/
│   │   │   └── mathematik/
│   │   │       └── klasse_8/
│   │   │           └── prozentrechnung/
│   │   │               └── grundlagen.md
│   │   └── grundschule/
│   │       └── mathematik/
│   │           ├── klasse_1/
│   │           │   └── zahlen/
│   │           │       └── zahlen_bis_20.md
│   │           └── klasse_3/
│   │               └── einmaleins/
│   │                   └── multiplikation_ueben.md
│   ├── nordrhein-westfalen/
│   │   └── gymnasium/
│   │       └── mathematik/
│   │           └── klasse_8/
│   │               └── funktionen/
│   │                   └── lineare_funktionen.md
│   └── baden-wuerttemberg/
│       └── gymnasium/
│           └── biologie/
│               └── klasse_10/
│                   └── genetik/
│                       └── vererbung.md
├── usa/
│   ├── california/
│   │   ├── elementary/
│   │   │   ├── mathematics/
│   │   │   │   ├── grade_1/
│   │   │   │   │   └── counting/
│   │   │   │   │       └── numbers_to_100.md
│   │   │   │   └── grade_3/
│   │   │   │       └── fractions/
│   │   │   │           └── intro_fractions.md
│   │   │   └── science/
│   │   │       └── grade_2/
│   │   │           └── life_science/
│   │   │               └── plants.md
│   │   ├── middle/
│   │   │   └── mathematics/
│   │   │       └── grade_7/
│   │   │           └── algebra/
│   │   │               └── linear_equations.md
│   │   └── high/
│   │       └── biology/
│   │           └── grade_10/
│   │               └── cells/
│   │                   └── cell_structure.md
│   └── texas/
│       └── middle/
│           └── science/
│               └── grade_8/
│                   └── physics/
│                       └── motion.md
└── uk/
    ├── england/
    │   ├── primary/
    │   │   └── mathematics/
    │   │       └── year_4/
    │   │           └── multiplication/
    │   │               └── times_tables.md
    │   └── secondary/
    │       └── mathematics/
    │           └── year_9/
    │               └── algebra/
    │                   └── equations.md
    └── scotland/
        └── secondary/
            └── science/
                └── s2/
                    └── chemistry/
                        └── elements.md
```

---

## 2. File Naming Convention

### 2.1 Pattern

`[topic_name]_[variant].md`

### 2.2 Rules

- Use lowercase
- Use underscores for spaces
- Use descriptive, concise names
- Avoid special characters (except underscore and hyphen)
- Include variant suffix if multiple versions exist

### 2.3 Examples

```
lineare_gleichungen.md
lineare_gleichungen_advanced.md
lineare_gleichungen_practice.md
cell_structure.md
photosynthesis_basics.md
```

---

## 3. Path Generation Logic

### 3.1 Algorithm

```python
def generate_storage_path(metadata):
    """
    Generate storage path from test metadata
    """
    # Normalize strings (lowercase, replace spaces with underscores)
    country = normalize(metadata['country'])
    region = normalize(metadata.get('region', metadata.get('bundesland', 'national')))
    school_type = normalize(metadata['school_type'])
    subject = normalize(metadata['subject'])
    
    # Handle grade level formatting
    if metadata.get('klassenstufe'):
        grade = f"klasse_{metadata['klassenstufe']}"
    else:
        grade = f"grade_{metadata['grade_level']}"
    
    # Normalize topic (main folder)
    topic_main = normalize(metadata.get('topic_category', metadata['topic']))
    
    # Create filename
    topic_specific = normalize(metadata['topic'])
    variant = metadata.get('variant', '')
    filename = f"{topic_specific}{('_' + variant) if variant else ''}.md"
    
    # Build complete path
    path_parts = [
        'tests',
        country,
        region,
        school_type,
        subject,
        grade,
        topic_main,
        filename
    ]
    
    return os.path.join(*path_parts)

def normalize(text):
    """Normalize text for path/filename"""
    return text.lower().replace(' ', '_').replace('-', '_')
```

### 3.2 Example Usage

```python
metadata = {
    'country': 'Germany',
    'bundesland': 'Bayern',
    'school_type': 'Gymnasium',
    'subject': 'Mathematik',
    'klassenstufe': 7,
    'topic_category': 'Algebra',
    'topic': 'Lineare Gleichungen',
    'variant': 'practice'
}

path = generate_storage_path(metadata)
# Result: tests/germany/bayern/gymnasium/mathematik/klasse_7/algebra/lineare_gleichungen_practice.md
```

---

## 4. Answer Key Storage

### 4.1 Recommended: Suffix in Same Directory

```
tests/
└── germany/bayern/gymnasium/mathematik/klasse_7/algebra/
    ├── lineare_gleichungen.md
    └── lineare_gleichungen_key.md
```

### 4.2 Alternative: Parallel Directory Structure

```
tests/
└── germany/bayern/gymnasium/mathematik/klasse_7/algebra/
    └── lineare_gleichungen.md

answer_keys/
└── germany/bayern/gymnasium/mathematik/klasse_7/algebra/
    └── lineare_gleichungen_key.md
```

---

## 5. PDF Storage

```
pdfs/
├── student_versions/
│   └── germany/bayern/gymnasium/mathematik/klasse_7/algebra/
│       └── lineare_gleichungen.pdf
└── answer_keys/
    └── germany/bayern/gymnasium/mathematik/klasse_7/algebra/
        └── lineare_gleichungen_key.pdf
```

---

## 6. Metadata Index

### 6.1 Index Files

Maintain searchable index files:

```
index/
├── test_index.json          # Complete test catalog
├── by_subject.json          # Grouped by subject
├── by_grade.json            # Grouped by grade level
└── by_topic.json            # Grouped by topic
```

### 6.2 test_index.json Example

```json
[
  {
    "id": "de-by-gym-math-7-algebra-001",
    "title": "Lineare Gleichungen - Übungstest",
    "path": "tests/germany/bayern/gymnasium/mathematik/klasse_7/algebra/lineare_gleichungen.md",
    "country": "Germany",
    "region": "Bayern",
    "school_type": "Gymnasium",
    "subject": "Mathematik",
    "grade": 7,
    "topic": "Lineare Gleichungen",
    "difficulty": "Medium",
    "question_count": 12,
    "estimated_time": 30,
    "language": "de",
    "created_date": "2025-11-15",
    "tags": ["algebra", "gleichungen", "klasse7"]
  }
]
```

---

## 7. Version Control

### 7.1 Semantic Versioning in Metadata

```yaml
version: 1.2
version_history:
  - version: 1.0
    date: 2025-11-15
    changes: "Initial creation"
  - version: 1.1
    date: 2025-11-20
    changes: "Fixed typo in question 3"
  - version: 1.2
    date: 2025-11-25
    changes: "Added 2 more challenging questions"
```

---

## 8. Related Files Organization

### 8.1 Complete File Group

```
tests/germany/bayern/gymnasium/mathematik/klasse_7/algebra/
├── lineare_gleichungen.md          # Main test
├── lineare_gleichungen_key.md      # Answer key
├── lineare_gleichungen_rubric.md   # Grading rubric
├── lineare_gleichungen_notes.md    # Teaching notes
└── images/
    ├── graph_example_1.png
    └── diagram_solution.png
```

---

## 9. Storage Best Practices

### 9.1 Guidelines

- **Consistent Naming:** Always use lowercase with underscores
- **Descriptive Paths:** Path should be self-explanatory
- **Avoid Deep Nesting:** Maximum 8 levels deep
- **Related Files Together:** Keep test, answer key, and resources in same directory
- **Index Maintenance:** Update index files when adding tests
- **Version Control:** Use Git for tracking changes

### 9.2 Prohibited Practices

- ❌ Spaces in filenames or paths
- ❌ Special characters (!, @, #, $, %, etc.)
- ❌ Inconsistent capitalization
- ❌ Abbreviations without documentation
- ❌ Generic names (test1.md, quiz.md)

---

## Related Documentation

- [Orchestrator Agent](./agents/orchestrator-agent.md) - Path generation logic
- [Formatter Agent](./agents/formatter-agent.md) - File structure
- [PDF Generator Agent](./agents/pdf-generator-agent.md) - PDF storage
- [Main Specifications](./main-spec.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
