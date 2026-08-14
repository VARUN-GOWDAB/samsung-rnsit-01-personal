from string import Template

CURRICULUM_PROMPT = Template("""
Role:
You are a senior {subject} curriculum architect.

Goal:
Design an industry-ready $subject curriculum.

Learning Domain Context:
$domain_context

Time Budget:
The complete curriculum should be achievable in approximately
$time_budget.

Constraints:

- Beginner to advanced
- Maximum 15 modules
- Emphasize hands-on learning
- Include projects after major topics

Negative Prompting:

- Do not include outdated topics.
- Do not repeat topics.
- Do not include unnecessary theory.
- Avoid vague module names.

Verification:

Before producing the answer:

- Verify logical learning order.
- Ensure no duplicate topics.
- Ensure every module contributes to job readiness.
- Check that prerequisites appear before advanced topics.

Return ONLY valid JSON.

JSON Schema

{
  "course_title": "",
  "target_audience": "",
  "time_budget": "",
  "summary": "",
  "prerequisites": [],
  "learning_outcomes": [],
  "tools": [],
  "verification": {
      "logical_order": true,
      "duplicates_removed": true,
      "job_ready": true,
      "prerequisites_checked": true
  },
  "modules": [
      {
          "module_number": 1,
          "module_title": "",
          "learning_outcome": "",
          "topics": [],
          "mini_project": "",
          "execution_plan": {
              "duration": "",
              "activities": [],
              "deliverables": []
          }
      }
  ],
  "final_capstone": {
      "title": "",
      "description": "",
      "skills_covered": []
  }
}

Return ONLY the JSON object.
""")