# Curriculum Fetcher Agent Specification

[← Back to Agent Overview](../agent-collaboration.md)

---

## Overview

**Agent Name:** Curriculum Fetcher Agent  
**Primary Role:** Automated acquisition and conversion of official curriculum data to YAML format  
**Agent Type:** Data Acquisition & Processing  
**Position in Workflow:** Pre-workflow (triggered before Curriculum Research Agent)  
**Version:** 1.0  
**Last Updated:** 2025-11-15

---

## Purpose

The Curriculum Fetcher Agent automates the process of obtaining official curriculum data from education ministries, parsing documents, extracting learning objectives, and converting everything into the standardized YAML format used by the test creation system.

**Problem Solved:** Eliminates manual curriculum research and YAML file creation, making the system fully autonomous from curriculum acquisition to test generation.

---

## Responsibilities

### 1. Curriculum Detection & Availability Check

**Check if curriculum data already exists:**
```python
def check_curriculum_exists(country, region, school_type, subject, grade):
    path = f"data/curriculum/{country}/{region}/{school_type}/{subject}/grade_{grade}.yaml"
    
    if os.path.exists(path):
        # Check if data is current (< 90 days old)
        modified_time = os.path.getmtime(path)
        age_days = (datetime.now() - datetime.fromtimestamp(modified_time)).days
        
        if age_days < 90:
            return "EXISTS_CURRENT"
        else:
            return "EXISTS_OUTDATED"
    
    return "NOT_FOUND"
```

**Decision Logic:**
- `EXISTS_CURRENT` → Skip fetching, use existing data
- `EXISTS_OUTDATED` → Fetch updates, compare with existing
- `NOT_FOUND` → Full fetch and creation required

### 2. Source Identification

**Germany (16 Bundesländer):**
- Bayern → https://www.lehrplanplus.bayern.de/
- Nordrhein-Westfalen → https://www.schulentwicklung.nrw.de/lehrplaene/
- Baden-Württemberg → http://www.bildungsplaene-bw.de/
- [... all 16 states with specific URLs]

**USA (50 States + Common Core):**
- Common Core → http://www.corestandards.org/read-the-standards/
- California → https://www.cde.ca.gov/be/st/ss/
- Texas → https://tea.texas.gov/academics/curriculum-standards/teks
- [... all 50 states with specific URLs]

**UK (4 Nations):**
- England → https://www.gov.uk/government/collections/national-curriculum
- Scotland → https://education.gov.scot/Documents/cfe-briefing-02.pdf
- Wales → https://hwb.gov.wales/curriculum-for-wales
- Northern Ireland → http://ccea.org.uk/curriculum

### 3. Data Acquisition Strategies

**Strategy A: Official APIs (Preferred)**
```yaml
api_sources:
  common_core:
    url: "http://www.corestandards.org/wp-json/ccss/v1/standards"
    method: "GET"
    auth: null
    format: "JSON"
    parsing: "direct_mapping"
  
  academic_benchmarks:
    url: "https://api.academicbenchmarks.com/v3/standards"
    method: "GET"
    auth: "API_KEY"
    format: "JSON"
    parsing: "transformation_required"
```

**Strategy B: Web Scraping**
```python
import requests
from bs4 import BeautifulSoup

def scrape_curriculum_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract structured data
    learning_objectives = []
    for section in soup.find_all('div', class_='learning-objective'):
        objective = {
            'id': section.get('data-id'),
            'text': section.find('p').text.strip(),
            'level': section.get('data-level')
        }
        learning_objectives.append(objective)
    
    return learning_objectives
```

**Strategy C: PDF Parsing**
```python
import pdfplumber
import re

def extract_from_pdf(pdf_path):
    objectives = []
    
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            
            # Pattern matching for learning objectives
            # Example: "Die Schülerinnen und Schüler können..."
            pattern = r'(?:Die Schüler.*?können|Students will be able to)\s+(.+?)(?:\n|$)'
            matches = re.findall(pattern, text, re.IGNORECASE)
            
            for match in matches:
                objectives.append(match.strip())
    
    return objectives
```

**Strategy D: AI-Powered Extraction**
```python
def ai_extract_curriculum(document_text, subject, grade):
    """Use AI to extract structured curriculum data from unstructured text"""
    
    prompt = f"""
    Extract curriculum learning objectives from this {subject} curriculum document for grade {grade}.
    
    Document:
    {document_text[:5000]}  # First 5000 chars
    
    Return JSON with:
    - learning_objectives (array of objects with: id, text_de, text_en, bloom_level)
    - prerequisites (array of strings)
    - key_topics (array of strings)
    - terminology (array of objects with: german, english, symbol, usage)
    """
    
    # Use AI model to extract structured data
    response = ai_model.complete(prompt)
    return json.loads(response)
```

### 4. Data Extraction & Structuring

**Learning Objectives Extraction:**
```python
def extract_learning_objectives(raw_data, source_type):
    objectives = []
    
    for raw_obj in raw_data:
        objective = {
            'id': generate_objective_id(raw_obj),
            'text_de': translate_to_german(raw_obj['text']) if source_type == 'english' else raw_obj['text'],
            'text_en': translate_to_english(raw_obj['text']) if source_type == 'german' else raw_obj['text'],
            'bloom_level': classify_bloom_level(raw_obj['text']),
            'curriculum_ref': raw_obj.get('reference_code', ''),
            'description': raw_obj.get('description', '')
        }
        objectives.append(objective)
    
    return objectives
```

**Bloom's Taxonomy Classification:**
```python
def classify_bloom_level(objective_text):
    """Classify learning objective by Bloom's taxonomy level"""
    
    # Keyword mapping
    bloom_keywords = {
        'Remember': ['nennen', 'auflisten', 'wiedergeben', 'list', 'name', 'recall'],
        'Understand': ['erklären', 'beschreiben', 'explain', 'describe', 'summarize'],
        'Apply': ['anwenden', 'lösen', 'berechnen', 'apply', 'solve', 'calculate'],
        'Analyze': ['analysieren', 'untersuchen', 'analyze', 'examine', 'compare'],
        'Evaluate': ['bewerten', 'beurteilen', 'evaluate', 'judge', 'critique'],
        'Create': ['entwickeln', 'gestalten', 'create', 'design', 'construct']
    }
    
    text_lower = objective_text.lower()
    
    for level, keywords in bloom_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            return level
    
    return 'Apply'  # Default
```

### 5. YAML Generation

**Complete YAML Structure:**
```python
def generate_curriculum_yaml(extracted_data, metadata):
    curriculum = {
        'curriculum_metadata': {
            'region': metadata['region'],
            'country': metadata['country'],
            'school_type': metadata['school_type'],
            'subject': metadata['subject'],
            'subject_en': translate_subject(metadata['subject']),
            'grade': metadata['grade'],
            'klassenstufe': metadata['grade'],
            'age_range': calculate_age_range(metadata['grade']),
            'source': metadata['source_name'],
            'source_url': metadata['source_url'],
            'document_version': metadata['version'],
            'last_updated': datetime.now().strftime('%Y-%m-%d'),
            'next_review': (datetime.now() + timedelta(days=365)).strftime('%Y-%m-%d'),
            'language': metadata['language']
        },
        'topics': extract_topics(extracted_data),
        'standards': extract_standards(extracted_data),
        'sample_questions': generate_sample_questions(extracted_data),
        'quality_thresholds': {
            'factual_accuracy': 100,
            'age_appropriateness': 95,
            'clarity': 90,
            'bias_free': 100,
            'curriculum_alignment': 100
        }
    }
    
    return yaml.dump(curriculum, allow_unicode=True, sort_keys=False)
```

**Topics Structure:**
```python
def extract_topics(data):
    topics = []
    
    for topic_data in data['topics']:
        topic = {
            'id': sanitize_id(topic_data['name']),
            'name_de': topic_data['name_de'],
            'name_en': topic_data['name_en'],
            'category': topic_data['category'],
            'learning_objectives': topic_data['objectives'],
            'competency_areas': topic_data['competencies'],
            'content_scope': {
                'include': topic_data['include_topics'],
                'exclude': topic_data['exclude_topics'],
                'prerequisites': topic_data['prerequisites'],
                'follow_up_topics': topic_data['follow_up']
            },
            'difficulty_recommendations': calculate_difficulty_distribution(topic_data),
            'terminology': extract_terminology(topic_data),
            'regional_specifics': extract_regional_specs(topic_data),
            'assessment_criteria': extract_assessment_criteria(topic_data),
            'vocabulary_guidelines': extract_vocabulary_guidelines(topic_data),
            'typical_errors': extract_common_errors(topic_data),
            'time_estimates': calculate_time_estimates(topic_data)
        }
        topics.append(topic)
    
    return topics
```

### 6. Validation & Quality Checks

**Required Field Validation:**
```python
def validate_curriculum_yaml(yaml_data):
    required_fields = [
        'curriculum_metadata',
        'topics',
        'standards',
        'sample_questions',
        'quality_thresholds'
    ]
    
    errors = []
    warnings = []
    
    # Check required fields
    for field in required_fields:
        if field not in yaml_data:
            errors.append(f"Missing required field: {field}")
    
    # Validate metadata
    if 'curriculum_metadata' in yaml_data:
        metadata = yaml_data['curriculum_metadata']
        required_metadata = ['region', 'country', 'school_type', 'subject', 'grade', 'source']
        
        for field in required_metadata:
            if field not in metadata:
                errors.append(f"Missing metadata field: {field}")
    
    # Validate topics
    if 'topics' in yaml_data:
        for i, topic in enumerate(yaml_data['topics']):
            if 'learning_objectives' not in topic:
                errors.append(f"Topic {i} missing learning_objectives")
            elif len(topic['learning_objectives']) == 0:
                warnings.append(f"Topic {i} has no learning objectives")
    
    # Check for completeness
    completeness_score = calculate_completeness(yaml_data)
    if completeness_score < 80:
        warnings.append(f"Curriculum data only {completeness_score}% complete")
    
    return {
        'valid': len(errors) == 0,
        'errors': errors,
        'warnings': warnings,
        'completeness': completeness_score
    }
```

**Completeness Scoring:**
```python
def calculate_completeness(yaml_data):
    """Calculate how complete the curriculum data is (0-100%)"""
    
    score_weights = {
        'has_metadata': 15,
        'has_topics': 20,
        'has_learning_objectives': 20,
        'has_terminology': 10,
        'has_assessment_criteria': 10,
        'has_difficulty_recommendations': 10,
        'has_regional_specifics': 10,
        'has_sample_questions': 5
    }
    
    score = 0
    
    if 'curriculum_metadata' in yaml_data:
        score += score_weights['has_metadata']
    
    if 'topics' in yaml_data and len(yaml_data['topics']) > 0:
        score += score_weights['has_topics']
        
        # Check first topic for detailed fields
        topic = yaml_data['topics'][0]
        if 'learning_objectives' in topic and len(topic['learning_objectives']) > 0:
            score += score_weights['has_learning_objectives']
        if 'terminology' in topic:
            score += score_weights['has_terminology']
        if 'assessment_criteria' in topic:
            score += score_weights['has_assessment_criteria']
        if 'difficulty_recommendations' in topic:
            score += score_weights['has_difficulty_recommendations']
        if 'regional_specifics' in topic:
            score += score_weights['has_regional_specifics']
    
    if 'sample_questions' in yaml_data and len(yaml_data['sample_questions']) > 0:
        score += score_weights['has_sample_questions']
    
    return score
```

### 7. File System Operations

**Save YAML File:**
```python
def save_curriculum_yaml(yaml_content, country, region, school_type, subject, grade):
    """Save curriculum YAML to correct directory structure"""
    
    # Create directory structure
    path = Path(f"data/curriculum/{country}/{region}/{school_type}/{subject}")
    path.mkdir(parents=True, exist_ok=True)
    
    # Generate filename
    filename = f"grade_{grade}.yaml"
    full_path = path / filename
    
    # Write file
    with open(full_path, 'w', encoding='utf-8') as f:
        f.write(yaml_content)
    
    # Create metadata tracking
    metadata = {
        'created': datetime.now().isoformat(),
        'source': 'curriculum-fetcher-agent',
        'version': '1.0',
        'path': str(full_path)
    }
    
    # Save metadata
    metadata_path = path / f"grade_{grade}_metadata.json"
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata, f, indent=2)
    
    return str(full_path)
```

**Update Existing Curriculum:**
```python
def update_curriculum(existing_path, new_data):
    """Update existing curriculum with new data while preserving manual edits"""
    
    # Load existing
    with open(existing_path, 'r', encoding='utf-8') as f:
        existing = yaml.safe_load(f)
    
    # Merge strategies
    merged = {
        'curriculum_metadata': update_metadata(existing['curriculum_metadata'], new_data['curriculum_metadata']),
        'topics': merge_topics(existing.get('topics', []), new_data.get('topics', [])),
        'standards': merge_lists(existing.get('standards', []), new_data.get('standards', [])),
        'sample_questions': existing.get('sample_questions', []) + new_data.get('sample_questions', []),
        'quality_thresholds': existing.get('quality_thresholds', new_data.get('quality_thresholds'))
    }
    
    # Create backup
    backup_path = existing_path.replace('.yaml', f'_backup_{datetime.now().strftime("%Y%m%d")}.yaml')
    shutil.copy(existing_path, backup_path)
    
    # Save merged version
    with open(existing_path, 'w', encoding='utf-8') as f:
        yaml.dump(merged, f, allow_unicode=True, sort_keys=False)
    
    return {
        'updated': True,
        'backup_path': backup_path,
        'changes': calculate_diff(existing, merged)
    }
```

### 8. Error Handling & Retry Logic

**Retry Strategy:**
```python
import time
from functools import wraps

def retry_on_failure(max_attempts=3, delay=2, backoff=2):
    """Decorator for retry logic with exponential backoff"""
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 1
            current_delay = delay
            
            while attempt <= max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts:
                        raise e
                    
                    print(f"Attempt {attempt} failed: {e}")
                    print(f"Retrying in {current_delay} seconds...")
                    time.sleep(current_delay)
                    
                    attempt += 1
                    current_delay *= backoff
            
        return wrapper
    return decorator

@retry_on_failure(max_attempts=3, delay=2, backoff=2)
def fetch_curriculum_data(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.content
```

**Error Types & Handling:**
```python
class CurriculumFetchError(Exception):
    pass

class NetworkError(CurriculumFetchError):
    pass

class ParsingError(CurriculumFetchError):
    pass

class ValidationError(CurriculumFetchError):
    pass

def handle_fetch_errors(error, context):
    """Handle different error types with appropriate fallbacks"""
    
    if isinstance(error, NetworkError):
        # Try cached version
        cached = get_cached_curriculum(context)
        if cached:
            return {'status': 'cached', 'data': cached, 'warning': 'Using cached data'}
        else:
            return {'status': 'failed', 'error': 'Network error and no cache available'}
    
    elif isinstance(error, ParsingError):
        # Try alternative parsing method
        alternative = try_alternative_parser(context)
        if alternative:
            return {'status': 'partial', 'data': alternative, 'warning': 'Used fallback parser'}
        else:
            return {'status': 'manual_required', 'error': 'Cannot parse automatically'}
    
    elif isinstance(error, ValidationError):
        # Save partial data with warnings
        return {'status': 'incomplete', 'data': context['partial_data'], 'errors': error.errors}
    
    else:
        return {'status': 'failed', 'error': str(error)}
```

---

## Input Specifications

### Required Parameters

```yaml
fetch_request:
  country: "Germany"          # Required: Country name
  region: "Bayern"            # Required: State/Province/Region
  school_type: "Gymnasium"    # Required: School type
  subject: "Mathematik"       # Required: Subject name
  grade: 7                    # Required: Grade level (integer)
  
  # Optional parameters
  force_refresh: false        # Force re-fetch even if current data exists
  prefer_language: "de"       # Preferred language for extraction
  cache_duration: 90          # Days to cache before refresh
```

### Optional Parameters

```yaml
advanced_options:
  extraction_method: "auto"   # auto, api, scrape, pdf, ai
  translation: true           # Auto-translate between German/English
  validate_immediately: true  # Run validation after creation
  create_backup: true         # Backup existing files before update
  ai_enhancement: true        # Use AI to enhance extracted data
  include_examples: true      # Generate sample questions
```

---

## Output Specifications

### Success Output

```yaml
fetch_result:
  status: "success"
  curriculum_file: "data/curriculum/germany/bayern/gymnasium/mathematik/grade_7.yaml"
  metadata:
    source: "https://www.lehrplanplus.bayern.de/"
    extraction_method: "web_scraping"
    topics_extracted: 4
    learning_objectives_count: 12
    completeness_score: 95
    extraction_time: 23.4  # seconds
  
  validation:
    valid: true
    errors: []
    warnings:
      - "Missing sample questions for topic 2"
    completeness: 95
  
  next_step: "curriculum-researcher"
  ready_for_use: true
```

### Partial Success Output

```yaml
fetch_result:
  status: "partial"
  curriculum_file: "data/curriculum/germany/bayern/gymnasium/mathematik/grade_7.yaml"
  metadata:
    source: "https://www.lehrplanplus.bayern.de/"
    extraction_method: "ai_fallback"
    topics_extracted: 3
    learning_objectives_count: 8
    completeness_score: 65
  
  validation:
    valid: true
    errors: []
    warnings:
      - "Incomplete topic coverage (3/5 topics)"
      - "Missing difficulty recommendations"
      - "Missing terminology section"
    completeness: 65
  
  recommendations:
    - "Manual review recommended"
    - "Add missing topics: Geometry, Probability"
    - "Enhance terminology section"
  
  next_step: "manual_review"
  ready_for_use: true  # Can proceed with limitations
```

### Failure Output

```yaml
fetch_result:
  status: "failed"
  error_type: "NetworkError"
  error_message: "Could not connect to curriculum source after 3 attempts"
  
  attempted_sources:
    - url: "https://www.lehrplanplus.bayern.de/"
      attempts: 3
      last_error: "Connection timeout"
  
  fallback_options:
    - type: "cached_data"
      available: false
      reason: "No previous fetch for this curriculum"
    
    - type: "manual_creation"
      template: "data/curriculum/templates/germany_template.yaml"
      instructions: "Create curriculum YAML manually using template"
  
  next_step: "manual_intervention"
  ready_for_use: false
```

---

## Source-Specific Implementations

### Germany: Bayern (Lehrplan PLUS)

**URL Structure:**
```
Base: https://www.lehrplanplus.bayern.de/
Pattern: /schulart/{school_type}/fach/{subject}/jahrgangsstufe/{grade}
Example: /schulart/gymnasium/fach/mathematik/jahrgangsstufe/7
```

**HTML Structure:**
```html
<div class="kompetenzerwartung">
    <h3 class="competency-title">Mit symbolischen Elementen umgehen</h3>
    <p class="learning-objective" data-id="M7-2.3-LO1">
        Die Schülerinnen und Schüler lösen einfache lineare Gleichungen...
    </p>
</div>
```

**Extraction Code:**
```python
def fetch_bayern_curriculum(school_type, subject, grade):
    url = f"https://www.lehrplanplus.bayern.de/schulart/{school_type}/fach/{subject}/jahrgangsstufe/{grade}"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    objectives = []
    for obj_elem in soup.find_all('p', class_='learning-objective'):
        objective = {
            'id': obj_elem.get('data-id'),
            'text_de': obj_elem.text.strip(),
            'text_en': translate_to_english(obj_elem.text.strip()),
            'bloom_level': classify_bloom_level(obj_elem.text),
            'curriculum_ref': obj_elem.get('data-id')
        }
        objectives.append(objective)
    
    return objectives
```

### USA: Common Core Standards

**API Endpoint:**
```
URL: http://www.corestandards.org/wp-json/ccss/v1/standards
Parameters:
  - grade: "7"
  - subject: "Math"
  - standard_id: "CCSS.MATH.7.EE.A.1"
```

**API Response:**
```json
{
  "standard_id": "CCSS.MATH.7.EE.A.1",
  "grade": "7",
  "subject": "Mathematics",
  "domain": "Expressions & Equations",
  "description": "Apply properties of operations as strategies to add, subtract, factor, and expand linear expressions with rational coefficients.",
  "bloom_level": "Apply",
  "examples": [...]
}
```

**Extraction Code:**
```python
def fetch_common_core(grade, subject):
    url = "http://www.corestandards.org/wp-json/ccss/v1/standards"
    params = {'grade': grade, 'subject': subject}
    
    response = requests.get(url, params=params)
    data = response.json()
    
    objectives = []
    for standard in data['standards']:
        objective = {
            'id': standard['standard_id'],
            'text_en': standard['description'],
            'text_de': translate_to_german(standard['description']),
            'bloom_level': standard.get('bloom_level', 'Apply'),
            'curriculum_ref': standard['standard_id']
        }
        objectives.append(objective)
    
    return objectives
```

### UK: National Curriculum (GOV.UK)

**URL Structure:**
```
Base: https://www.gov.uk/government/publications/
Pattern: national-curriculum-in-england-{subject}-programmes-of-study
Example: national-curriculum-in-england-mathematics-programmes-of-study
```

**PDF Parsing:**
```python
def fetch_uk_national_curriculum(subject, key_stage):
    # Download PDF
    pdf_url = f"https://assets.publishing.service.gov.uk/.../NC_{subject}_KS{key_stage}.pdf"
    pdf_path = download_pdf(pdf_url)
    
    # Extract text
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text()
    
    # Pattern for learning objectives
    pattern = r'[Pp]upils should be taught to:?\s+(.+?)(?:\n\n|\n[A-Z])'
    matches = re.findall(pattern, full_text, re.DOTALL)
    
    objectives = []
    for i, match in enumerate(matches):
        objective = {
            'id': f"UK-NC-{subject}-KS{key_stage}-{i+1}",
            'text_en': match.strip(),
            'text_de': translate_to_german(match.strip()),
            'bloom_level': classify_bloom_level(match),
            'curriculum_ref': f"NC-KS{key_stage}"
        }
        objectives.append(objective)
    
    return objectives
```

---

## Caching Strategy

### Cache Structure

```
.cache/curriculum/
├── germany/
│   └── bayern/
│       └── gymnasium/
│           └── mathematik/
│               ├── grade_7_cache.yaml
│               └── grade_7_metadata.json
├── usa/
│   └── common_core/
│       └── mathematics/
│           ├── grade_7_cache.yaml
│           └── grade_7_metadata.json
└── cache_index.json
```

### Cache Metadata

```json
{
  "cache_id": "de-bayern-gym-math-7",
  "created": "2025-11-15T10:30:00Z",
  "expires": "2026-02-13T10:30:00Z",
  "cache_duration_days": 90,
  "source_url": "https://www.lehrplanplus.bayern.de/...",
  "extraction_method": "web_scraping",
  "completeness": 95,
  "last_validated": "2025-11-15T10:35:00Z",
  "access_count": 3,
  "last_accessed": "2025-11-15T14:20:00Z"
}
```

### Cache Management

```python
def get_cached_curriculum(country, region, school_type, subject, grade):
    """Retrieve cached curriculum if available and not expired"""
    
    cache_path = Path(f".cache/curriculum/{country}/{region}/{school_type}/{subject}/grade_{grade}_cache.yaml")
    metadata_path = cache_path.parent / f"grade_{grade}_metadata.json"
    
    if not cache_path.exists():
        return None
    
    # Check expiration
    with open(metadata_path, 'r') as f:
        metadata = json.load(f)
    
    expires = datetime.fromisoformat(metadata['expires'])
    if datetime.now() > expires:
        return None  # Expired
    
    # Load cached data
    with open(cache_path, 'r', encoding='utf-8') as f:
        cached_data = yaml.safe_load(f)
    
    # Update access metadata
    metadata['access_count'] += 1
    metadata['last_accessed'] = datetime.now().isoformat()
    with open(metadata_path, 'w') as f:
        json.dump(metadata, f, indent=2)
    
    return cached_data

def save_to_cache(curriculum_data, metadata):
    """Save curriculum data to cache"""
    
    cache_path = Path(f".cache/curriculum/{metadata['country']}/{metadata['region']}/{metadata['school_type']}/{metadata['subject']}/grade_{metadata['grade']}_cache.yaml")
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save curriculum data
    with open(cache_path, 'w', encoding='utf-8') as f:
        yaml.dump(curriculum_data, f, allow_unicode=True, sort_keys=False)
    
    # Save metadata
    cache_metadata = {
        'cache_id': f"{metadata['country']}-{metadata['region']}-{metadata['school_type'][:3]}-{metadata['subject'][:4]}-{metadata['grade']}",
        'created': datetime.now().isoformat(),
        'expires': (datetime.now() + timedelta(days=metadata.get('cache_duration', 90))).isoformat(),
        'cache_duration_days': metadata.get('cache_duration', 90),
        'source_url': metadata['source_url'],
        'extraction_method': metadata['extraction_method'],
        'completeness': metadata['completeness'],
        'last_validated': datetime.now().isoformat(),
        'access_count': 0,
        'last_accessed': None
    }
    
    metadata_path = cache_path.parent / f"grade_{metadata['grade']}_metadata.json"
    with open(metadata_path, 'w') as f:
        json.dump(cache_metadata, f, indent=2)
```

---

## Integration with Agent Workflow

### Workflow Position

```
User Request → @orchestrator
    ↓
Orchestrator checks: Does curriculum exist?
    ↓ [NOT FOUND or OUTDATED]
@curriculum-fetcher (fetch & convert)
    ↓ [SAVES to data/curriculum/]
@curriculum-researcher (read YAML)
    ↓
@test-designer → ... → @pdf-generator
```

### Handoff to Curriculum Researcher

```yaml
handoff:
  from: "curriculum-fetcher"
  to: "curriculum-researcher"
  trigger: "curriculum_file_created"
  
  context:
    curriculum_file: "data/curriculum/germany/bayern/gymnasium/mathematik/grade_7.yaml"
    fetch_metadata:
      source: "https://www.lehrplanplus.bayern.de/"
      extraction_method: "web_scraping"
      completeness: 95
      warnings: ["Missing sample questions for topic 2"]
    
    session_id: "sess_20251115_103045"
    test_id: "de-by-gym-math-7-algebra-001"
  
  instructions: |
    Curriculum data has been fetched and saved.
    Please proceed with curriculum research using the created YAML file.
    Note: Completeness is 95% - some manual enhancement may be needed later.
```

---

## Performance Requirements

### Target Metrics

- **Fetch Time:** <60 seconds for web scraping
- **API Response:** <10 seconds
- **PDF Parsing:** <30 seconds for 50-page document
- **AI Extraction:** <120 seconds
- **YAML Generation:** <5 seconds
- **Total End-to-End:** <180 seconds (3 minutes)

### Optimization Strategies

```python
# Parallel fetching for multiple topics
import concurrent.futures

def fetch_multiple_topics(topics_list):
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(fetch_topic, topic) for topic in topics_list]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return results

# Incremental caching
def incremental_fetch(country, region, school_type, subject, grades):
    """Fetch curriculum for multiple grades, caching as we go"""
    
    for grade in grades:
        # Check cache first
        cached = get_cached_curriculum(country, region, school_type, subject, grade)
        if cached:
            continue
        
        # Fetch and cache
        curriculum = fetch_curriculum(country, region, school_type, subject, grade)
        save_to_cache(curriculum, metadata)
        
        # Brief pause to avoid rate limiting
        time.sleep(1)
```

---

## Error Messages & User Communication

### User-Facing Messages

**Success:**
```
✅ Curriculum Fetched Successfully

📚 Source: Lehrplan PLUS Bayern 2024
🎯 Topics: 4 extracted
📝 Learning Objectives: 12 identified
📊 Completeness: 95%

📁 Saved to: data/curriculum/germany/bayern/gymnasium/mathematik/grade_7.yaml

✓ Ready for test generation
```

**Partial Success:**
```
⚠️ Curriculum Partially Fetched

📚 Source: Lehrplan PLUS Bayern 2024
🎯 Topics: 3 extracted (2 missing)
📝 Learning Objectives: 8 identified
📊 Completeness: 65%

⚠️ Warnings:
- Missing topics: Geometry, Probability
- No sample questions generated
- Terminology section incomplete

📁 Saved to: data/curriculum/germany/bayern/gymnasium/mathematik/grade_7.yaml

✓ Can proceed with test generation (limited scope)
💡 Recommendation: Manual review and enhancement suggested
```

**Network Error:**
```
❌ Curriculum Fetch Failed

🔗 Connection Error: Could not reach curriculum source
🌐 URL: https://www.lehrplanplus.bayern.de/...
🔄 Attempts: 3 (all failed)

💾 Checking cache... Not available

📝 Next Steps:
1. Check internet connection
2. Verify source website is accessible
3. Try again later
4. Or create curriculum YAML manually

Template available: data/curriculum/templates/germany_template.yaml
```

**Validation Error:**
```
⚠️ Curriculum Validation Issues

📥 Data extracted but has quality issues:
- ❌ Missing required field: learning_objectives
- ⚠️ Incomplete topic coverage (50%)
- ⚠️ No Bloom's taxonomy classification

🔧 Attempting auto-fix... Partially successful

📁 Saved incomplete data to: data/curriculum/germany/bayern/gymnasium/mathematik/grade_7.yaml

⚠️ Manual intervention required before test generation
📖 See validation report: .agent_workspace/curriculum_fetch/validation_report.yaml
```

---

## Dependencies & Requirements

### Python Packages

```txt
requests>=2.31.0          # HTTP requests
beautifulsoup4>=4.12.0    # HTML parsing
pdfplumber>=0.10.0        # PDF text extraction
PyYAML>=6.0              # YAML processing
lxml>=4.9.0              # XML/HTML parsing
scrapy>=2.11.0           # Advanced web scraping
selenium>=4.15.0         # JavaScript-heavy sites
pdfminer.six>=20221105   # Alternative PDF parsing
pytesseract>=0.3.10      # OCR for scanned PDFs
translators>=5.8.0       # Language translation
langdetect>=1.0.9        # Language detection
```

### System Requirements

```bash
# PDF processing
apt-get install poppler-utils

# OCR (if needed for scanned documents)
apt-get install tesseract-ocr tesseract-ocr-deu tesseract-ocr-eng

# For JavaScript rendering
apt-get install chromium-chromedriver
```

### API Keys (Optional)

```yaml
api_keys:
  academic_benchmarks: "YOUR_API_KEY"  # For Academic Benchmarks API
  deepl: "YOUR_API_KEY"                # For better translation
  openai: "YOUR_API_KEY"               # For AI-powered extraction
```

---

## Testing & Validation

### Unit Tests

```python
def test_fetch_bayern_curriculum():
    """Test fetching Bayern curriculum"""
    result = fetch_curriculum(
        country="Germany",
        region="Bayern",
        school_type="Gymnasium",
        subject="Mathematik",
        grade=7
    )
    
    assert result['status'] == 'success'
    assert result['validation']['valid'] == True
    assert result['metadata']['topics_extracted'] > 0
    assert result['metadata']['completeness_score'] >= 80

def test_yaml_validation():
    """Test YAML validation logic"""
    valid_yaml = load_sample_curriculum()
    result = validate_curriculum_yaml(valid_yaml)
    
    assert result['valid'] == True
    assert len(result['errors']) == 0
    assert result['completeness'] >= 80

def test_cache_expiration():
    """Test cache expiration logic"""
    # Create expired cache
    create_expired_cache()
    
    # Should not return expired cache
    cached = get_cached_curriculum("Germany", "Bayern", "Gymnasium", "Mathematik", 7)
    assert cached is None

def test_retry_logic():
    """Test retry mechanism on failure"""
    with patch('requests.get', side_effect=ConnectionError):
        with pytest.raises(NetworkError):
            fetch_with_retry("https://example.com", max_attempts=3)
```

### Integration Tests

```python
def test_end_to_end_fetch():
    """Test complete fetch workflow"""
    # Clean state
    clear_curriculum_cache()
    remove_curriculum_file("Germany", "Bayern", "Gymnasium", "Mathematik", 7)
    
    # Fetch
    result = curriculum_fetcher_agent.execute({
        'country': 'Germany',
        'region': 'Bayern',
        'school_type': 'Gymnasium',
        'subject': 'Mathematik',
        'grade': 7
    })
    
    # Verify file created
    assert os.path.exists("data/curriculum/germany/bayern/gymnasium/mathematik/grade_7.yaml")
    
    # Verify handoff data
    assert result['next_step'] == 'curriculum-researcher'
    assert result['ready_for_use'] == True

def test_update_existing_curriculum():
    """Test updating existing curriculum file"""
    # Create initial curriculum
    create_sample_curriculum()
    
    # Fetch with force_refresh
    result = curriculum_fetcher_agent.execute({
        'country': 'Germany',
        'region': 'Bayern',
        'school_type': 'Gymnasium',
        'subject': 'Mathematik',
        'grade': 7,
        'force_refresh': True
    })
    
    # Verify backup created
    assert os.path.exists("data/curriculum/germany/bayern/gymnasium/mathematik/grade_7_backup_*.yaml")
    
    # Verify merged data
    curriculum = load_curriculum("Germany", "Bayern", "Gymnasium", "Mathematik", 7)
    assert 'curriculum_metadata' in curriculum
```

---

## Future Enhancements

### Phase 2 Features

1. **Multi-Language Support**
   - Support for French, Spanish, Italian curricula
   - Automatic translation pipelines
   - Language-specific extraction patterns

2. **Advanced AI Integration**
   - Use GPT-4 for complex document parsing
   - Automatic Bloom's taxonomy classification
   - Generate sample questions during fetch

3. **Collaborative Editing**
   - Web interface for manual curriculum enhancement
   - Version control for curriculum changes
   - Diff viewer for updates

4. **Analytics & Monitoring**
   - Track fetch success rates by source
   - Monitor curriculum update frequencies
   - Alert on failed fetches

5. **Curriculum Comparison**
   - Compare curricula across regions
   - Identify gaps and overlaps
   - Suggest test content based on differences

---

## Related Documentation

- [Main Specification](../main-spec.md)
- [Curriculum Research Agent](./curriculum-research-agent.md)
- [Data Schemas](../data-schemas.md)
- [Agent Collaboration](../agent-collaboration.md)
- [Implementation Decisions](../implementation-decisions.md)

---

**Version:** 1.0  
**Last Updated:** November 15, 2025  
**Status:** Specification Complete - Ready for Implementation
