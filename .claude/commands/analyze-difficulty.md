Analyze difficulty distribution of a test and verify it meets the 30/50/20 target (easy/medium/hard).

This command assesses each question's difficulty on a 0-10 scale and calculates overall distribution.

**What it does:**
1. Reads test draft from .agent_workspace/test_drafts/
2. Analyzes each question for difficulty factors:
   - Cognitive complexity
   - Number of steps required
   - Abstract vs concrete concepts
   - Prior knowledge needed
   - Time pressure
3. Assigns difficulty score (0-10) to each question
4. Calculates distribution by points (not count)
5. Compares to target: Easy 30%, Medium 50%, Hard 20%
6. Generates detailed analysis report

**Usage:**
```
/analyze-difficulty
```

You'll be prompted for:
- Test ID or file path to analyze

**Target Distribution:**
- Easy (1-3 difficulty): 30% of total points ±10%
- Medium (4-7 difficulty): 50% of total points ±10%
- Hard (8-10 difficulty): 20% of total points ±10%

**Output:**
- Analysis report: `.agent_workspace/difficulty_analysis/{test_id}_difficulty.yaml`
- Pass/fail status
- Recommendations if distribution is off
- Question-by-question difficulty breakdown

**What happens if off-target:**
- Provides specific recommendations
- Identifies which questions to adjust
- Suggests how to increase/decrease difficulty
- Can trigger revision loop if needed

**Use when:**
- Verifying test difficulty balance
- Checking manually created tests
- Analyzing existing test quality
- Before finalizing test for classroom use

**Time:** 2-3 minutes
