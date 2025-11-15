# Orchestrator Agent Specification

[← Back to Main Documentation](../../README.md)

---

## Overview

The Orchestrator Agent is the central coordinator that manages the entire test creation workflow, handles user interaction, and ensures quality gates are met throughout the process.

---

## Responsibilities

- Manage overall test creation workflow
- Coordinate between all specialized agents
- Handle user input and requirements gathering
- Make decisions on workflow routing
- Manage reverse interviewing process
- Ensure quality gates are met
- Handle error recovery and retries
- Track progress and provide status updates
- Determine file naming and storage location

---

## Inputs

- Initial user request (may be incomplete)
- User responses to clarifying questions
- Agent outputs and status updates

---

## Outputs

- Complete test files (Markdown and/or PDF)
- Metadata and documentation
- Progress reports
- Quality assurance summary

---

## Workflow Management

```python
class OrchestratorAgent:
    def create_test(self, initial_request):
        # Phase 1: Requirements Gathering
        requirements = self.gather_requirements(initial_request)
        
        # Phase 2: Curriculum Research
        if self.needs_curriculum_research(requirements):
            curriculum_data = self.call_curriculum_agent(requirements)
            requirements.update(curriculum_data)
        
        # Phase 3: Test Design
        test_draft = self.call_test_designer(requirements)
        
        # Phase 4: Validation Loop
        while not self.is_valid(test_draft):
            issues = self.call_validator(test_draft)
            test_draft = self.call_test_designer(requirements, issues)
        
        # Phase 5: Difficulty Analysis
        difficulty_analysis = self.call_difficulty_analyzer(test_draft)
        if difficulty_analysis.needs_adjustment:
            test_draft = self.adjust_difficulty(test_draft, difficulty_analysis)
        
        # Phase 6: Time Estimation
        time_estimate = self.call_time_estimator(test_draft, requirements)
        if not time_estimate.is_feasible:
            test_draft = self.adjust_for_time(test_draft, time_estimate)
        
        # Phase 7: Formatting
        formatted_test = self.call_formatter(test_draft, requirements)
        
        # Phase 8: File Storage
        storage_path = self.determine_storage_path(requirements)
        self.save_markdown(formatted_test, storage_path)
        
        # Phase 9: PDF Generation (if requested)
        if requirements.needs_pdf:
            pdf_files = self.call_pdf_generator(formatted_test, requirements)
            self.save_pdfs(pdf_files, storage_path)
        
        return {
            'markdown_path': storage_path,
            'pdf_paths': pdf_files if requirements.needs_pdf else None,
            'metadata': formatted_test.metadata,
            'quality_score': self.calculate_quality_score(formatted_test)
        }
    
    def gather_requirements(self, initial_request):
        """Interactive requirements gathering with reverse interviewing"""
        requirements = self.parse_initial_request(initial_request)
        
        # Identify missing critical information
        missing_fields = self.identify_missing_fields(requirements)
        
        # Ask clarifying questions
        for field in missing_fields:
            question = self.generate_clarifying_question(field)
            response = self.ask_user(question)
            requirements[field] = self.parse_response(response, field)
        
        # Validate and confirm
        if self.needs_confirmation(requirements):
            confirmed = self.confirm_with_user(requirements)
            if not confirmed:
                return self.gather_requirements(initial_request)
        
        return requirements
    
    def determine_storage_path(self, requirements):
        """Generate storage path based on requirements"""
        return self.build_path(
            base='tests',
            country=requirements.country,
            bundesland=requirements.get('bundesland'),
            school_type=requirements.school_type,
            subject=requirements.subject,
            grade=requirements.grade_level,
            topic=requirements.topic
        )
```

---

## Reverse Interviewing Questions

The Orchestrator may ask:

### If country/region missing:
- "Which country's education system should this test follow? (e.g., Germany, USA, UK)"
- "Which state/Bundesland? (e.g., Bayern, NRW, California)"

### If school type unclear:
- "What type of school is this for? (e.g., Gymnasium, Realschule, Elementary)"

### If grade level ambiguous:
- "Which grade level/Klassenstufe? (e.g., Klasse 7, Grade 5)"

### If difficulty preference missing:
- "What difficulty distribution would you like? (Easy/Medium/Hard percentages)"
- "Should this be suitable for below-average, average, or advanced students?"

### If time constraints unclear:
- "How much time should students have to complete this test?"
- "Is this a timed test or can students work at their own pace?"

### If output format not specified:
- "Do you need PDF output in addition to Markdown?"
- "Which styling theme would you prefer for PDFs?"

### If question count missing:
- "How many questions should the test include?"

### If topic scope ambiguous:
- "Should this cover [broader topic] or focus specifically on [subtopic]?"

---

## Quality Gates

Before completion, the Orchestrator ensures:

- ✓ Curriculum alignment verified
- ✓ All questions validated
- ✓ Difficulty distribution balanced
- ✓ Time estimate feasible
- ✓ Formatting consistent
- ✓ Metadata complete
- ✓ Files saved correctly

---

## Related Agents

- [Curriculum Research Agent](./curriculum-research-agent.md)
- [Test Designer Agent](./test-designer-agent.md)
- [Content Validator Agent](./content-validator-agent.md)
- [Difficulty Analyzer Agent](./difficulty-analyzer-agent.md)
- [Time Estimation Agent](./time-estimator-agent.md)
- [Formatter Agent](./formatter-agent.md)
- [PDF Generator Agent](./pdf-generator-agent.md)

---

## See Also

- [Agent Collaboration Protocol](../agent-collaboration.md)
- [Repository Organization](../repository-organization.md)

---

**Version:** 2.0  
**Last Updated:** November 15, 2025
