# Prompt Engineering Cheat Sheet

> **Core idea:** A good prompt tells the AI **who to be, what to do,
> what to know, what boundaries to follow, how to communicate, and how
> to structure the result**.

------------------------------------------------------------------------

## 🧠 Prompt Engineering Mindmap

``` mermaid
mindmap
  root((PROMPT))
    Core Properties
      Role
        Defines who the AI should be
        Persona / expertise / perspective
      Goal
        Defines the objective
        Desired outcome
      Context
        Provides background
        Data / situation / audience / history
      Constraints
        Defines boundaries
        Rules / limits / exclusions
      Style
        Controls tone
        Audience / voice / level of detail
      Output Format
        Structures the response
        Markdown / table / JSON / XML / bullets
      Negative Prompting
        Reduces unwanted output
        Specify what NOT to do
      Verification
        Improves reliability
        Check / validate / critique / cite
      Structured Outputs
        Simplify validation and automation
        Schema / JSON / typed fields
    Prompting Techniques
      Zero-Shot
        No examples
        Simple or well-known tasks
      Few-Shot
        Provide examples
        Consistent outputs
      Step-by-Step
        Break complex work into stages
      Chain-of-Thought
        Sequential reasoning
        Prefer concise reasoning summaries when appropriate
      Tree-of-Thoughts
        Explore multiple solution paths
      Program-of-Thoughts
        Use calculations / code-like procedures
      Reflective Prompting
        Review and improve the result
      ReAct
        Reason → Act → Observe → Repeat
    Control & Structure
      System Prompt
        Defines persistent AI behavior
        Conversation-level
      Instruction
        Defines the current task
        Request-level
      Style Control
        Tone / audience / presentation
      Schema-First
        Define output structure first
        APIs / automation / extraction
      Template Reuse
        Reuse proven prompt patterns
        Repetitive workflows
    Reliability
      Grounding
        Give authoritative source material
      Verification
        Check facts and requirements
      Validation
        Check output against schema
      Iteration
        Prompt → Test → Evaluate → Improve
```

------------------------------------------------------------------------

# 1. 🧩 The Anatomy of a Strong Prompt

  -----------------------------------------------------------------------
  Component               What it does            Typical questions
  ----------------------- ----------------------- -----------------------
  **Role**                Defines who the AI      Who should the AI act
                          should be               as?

  **Goal**                Defines the objective   What should it
                                                  accomplish?

  **Context**             Provides background     What does the AI need
                                                  to know?

  **Constraints**         Defines boundaries      What must/mustn't it
                                                  do?

  **Style**               Controls tone and       How should it
                          presentation            communicate?

  **Output Format**       Structures the response What should the answer
                                                  look like?

  **Negative Prompting**  Reduces unwanted        What should be avoided?
                          behavior/output         

  **Verification**        Improves reliability    How should the result
                                                  be checked?

  **Structured Outputs**  Makes results           What schema must the
                          predictable             output follow?
  -----------------------------------------------------------------------

### Practical Prompt Formula

``` text
ROLE
  +
GOAL
  +
CONTEXT
  +
CONSTRAINTS
  +
STYLE
  +
OUTPUT FORMAT
  +
VERIFICATION
  =
HIGH-QUALITY PROMPT
```

### Example

``` text
Role:
You are an experienced Python instructor.

Goal:
Teach beginners how Python functions work.

Context:
The learners know variables, loops and basic data types.

Constraints:
Use simple examples. Avoid advanced decorators and recursion.

Style:
Friendly, practical and classroom-oriented.

Output Format:
1. Concept
2. Syntax
3. Example
4. Common mistakes
5. Practice exercise

Verification:
Check that every example is syntactically valid Python.
```

------------------------------------------------------------------------

# 2. 🎯 Core Prompt Properties

## Role

**Defines who the AI should be.**

Use it to establish: - Expertise - Persona - Perspective -
Responsibility - Domain knowledge

``` text
Act as a senior data engineer mentoring a junior developer.
```

**Useful for:** tutoring, consulting, architecture, analysis,
domain-specific tasks.

------------------------------------------------------------------------

## Goal

**Defines the objective.**

A strong goal describes the desired outcome rather than merely naming a
topic.

Weak:

``` text
Explain RAG.
```

Better:

``` text
Explain RAG to a software developer who knows Python but is new to LLM applications.
```

Best:

``` text
Teach RAG so that the learner can explain the architecture,
identify its major components, and build a basic RAG application.
```

------------------------------------------------------------------------

## Context

**Provides the information the AI needs to make a useful decision.**

Context can include:

-   Background
-   Existing data
-   Audience
-   Business situation
-   Previous decisions
-   Technical environment
-   Assumptions
-   Source documents

``` text
The application uses Python 3.12, FastAPI and PostgreSQL.
The developers are comfortable with REST APIs but new to LLMs.
```

> **Rule:** More context is not automatically better. Provide **relevant
> context**.

------------------------------------------------------------------------

## Constraints

**Define boundaries and limitations.**

Examples:

``` text
Use only the supplied document.
Do not invent missing facts.
Keep the answer below 500 words.
Use Python only.
Do not use external libraries.
```

Common constraint types:

  Constraint   Example
  ------------ ------------------------------------
  Length       Maximum 500 words
  Technology   Python + FastAPI
  Scope        Focus only on Phase 1
  Source       Use only supplied information
  Time         Complete within 5 steps
  Exclusion    Do not discuss implementation
  Safety       Do not provide unsafe instructions

------------------------------------------------------------------------

## Style

**Controls how the answer is communicated.**

Control:

-   Tone
-   Formality
-   Audience
-   Vocabulary
-   Depth
-   Teaching style
-   Voice

Examples:

``` text
Explain it like a university professor.
```

``` text
Use an executive-friendly business tone.
```

``` text
Explain it to a 15-year-old using simple analogies.
```

------------------------------------------------------------------------

## Output Format

**Defines the shape of the answer.**

Examples:

``` text
Return the answer as a table.
```

``` text
Return exactly 5 bullet points.
```

``` text
Return valid JSON with:
name, objective, prerequisites, duration
```

Possible formats:

-   Plain text
-   Markdown
-   Table
-   JSON
-   XML
-   YAML
-   CSV
-   SQL
-   Python
-   API schema
-   Structured object

------------------------------------------------------------------------

# 3. 🚫 Negative Prompting

**Negative prompting specifies what the AI should avoid.**

Examples:

``` text
Do not use jargon.
```

``` text
Do not repeat the question.
```

``` text
Do not invent sources.
```

``` text
Avoid unnecessary introductions.
```

``` text
Do not include implementation details.
```

### Best practice

Combine positive and negative instructions:

``` text
Use concise technical language.
Avoid marketing language and unnecessary adjectives.
```

> Negative prompting is especially useful for **style control, image
> generation, formatting, safety boundaries and eliminating recurring
> unwanted behavior**.

------------------------------------------------------------------------

# 4. ✅ Verification

**Verification adds a quality-control step.**

Useful verification instructions:

``` text
Check the calculations before presenting the answer.
```

``` text
Verify that every requirement has been addressed.
```

``` text
Identify assumptions and uncertainties.
```

``` text
Check the JSON against the requested schema.
```

``` text
Review the answer for factual inconsistencies.
```

### Verification Pattern

``` text
GENERATE
   ↓
CHECK
   ↓
IDENTIFY ERRORS
   ↓
CORRECT
   ↓
FINAL ANSWER
```

> Verification does **not guarantee correctness**. It is a reliability
> technique, not proof of truth.

------------------------------------------------------------------------

# 5. 📦 Structured Outputs

**Structured outputs make AI responses predictable, machine-readable and
easier to validate.**

Instead of:

``` text
The candidate is suitable because they have Python,
AWS and five years of experience.
```

Use:

``` json
{
  "candidate": "Asha",
  "skills": ["Python", "AWS"],
  "experience_years": 5,
  "suitable": true
}
```

### Why use structured outputs?

-   Easier parsing
-   Schema validation
-   API integration
-   Database insertion
-   Workflow automation
-   Reliable downstream processing
-   Reduced ambiguity

### Structured Output Hierarchy

``` text
Natural Language
      ↓
Markdown / Table
      ↓
JSON / XML / YAML
      ↓
Schema-Constrained Output
      ↓
Validated Structured Object
```

------------------------------------------------------------------------

# 6. 🎲 Zero-Shot vs Few-Shot

  -----------------------------------------------------------------------
  Technique               Meaning                 Best use
  ----------------------- ----------------------- -----------------------
  **Zero-Shot**           Perform the task        Simple / familiar tasks
                          without examples        

  **Few-Shot**            Provide examples        Consistent outputs /
                          showing the desired     classification
                          behavior                

  **Many-Shot**           Provide many examples   Complex patterns when
                                                  context budget permits
  -----------------------------------------------------------------------

### Zero-Shot

``` text
Classify this review as Positive, Negative or Neutral:

"The product works well but delivery was late."
```

### Few-Shot

``` text
Review: "Excellent product!"
Classification: Positive

Review: "Completely unusable."
Classification: Negative

Review: "The product works well but delivery was late."
Classification:
```

> **Key idea:** Examples demonstrate the task better than instructions
> alone when the desired pattern is difficult to describe.

------------------------------------------------------------------------

# 7. 🏛️ System Prompt vs Instruction

  -----------------------------------------------------------------------
  Concept                 Purpose                 Scope
  ----------------------- ----------------------- -----------------------
  **System Prompt**       Defines AI behavior,    Conversation /
                          role and policies       application level

  **Instruction**         Defines the task to     Individual request
                          perform                 

  **User Input**          Supplies the current    Current interaction
                          information/request     

  **Tool Instruction**    Defines how tools       Tool interaction
                          should be used          
  -----------------------------------------------------------------------

### Mental Model

``` text
SYSTEM
  ↓
Defines "HOW THE AI SHOULD BEHAVE"

USER INSTRUCTION
  ↓
Defines "WHAT THE AI SHOULD DO NOW"

INPUT / DATA
  ↓
Provides "WHAT THE AI SHOULD WORK ON"
```

------------------------------------------------------------------------

# 8. 🎨 Style Control

Style control can specify:

``` text
Audience → Who is reading?
Tone     → Formal / friendly / direct?
Depth    → Beginner / intermediate / expert?
Voice    → Teacher / consultant / analyst?
Format   → Narrative / bullets / table?
Length   → Short / detailed?
```

Example:

``` text
Explain Kubernetes to a CTO.

Use:
- executive language
- business implications
- minimal technical jargon
- a concise comparison table
```

------------------------------------------------------------------------

# 9. 🧱 Schema-First Prompting

**Define the desired structure before generating the content.**

Instead of:

``` text
Analyze these customer complaints.
```

Use:

``` text
Analyze each complaint and return:

{
  "category": "...",
  "severity": "...",
  "root_cause": "...",
  "recommended_action": "..."
}
```

### Best for

-   APIs
-   Automation
-   Data extraction
-   Classification
-   ETL pipelines
-   Agent workflows
-   Database ingestion

### Schema-First Pattern

``` text
DEFINE SCHEMA
      ↓
DEFINE RULES
      ↓
PROVIDE INPUT
      ↓
GENERATE OUTPUT
      ↓
VALIDATE SCHEMA
```

------------------------------------------------------------------------

# 10. ♻️ Template Reuse

**Create proven prompt patterns and reuse them.**

A reusable template:

``` text
Role: {role}

Goal: {goal}

Context:
{context}

Constraints:
{constraints}

Style:
{style}

Output Format:
{format}

Verification:
{verification}

Input:
{input}
```

### Benefits

-   Consistency
-   Faster development
-   Easier testing
-   Easier maintenance
-   Easier version control
-   Better team collaboration

> Think of prompts as **reusable software components**, not disposable
> text.

------------------------------------------------------------------------

# 11. 🪜 Step-by-Step Prompting

Break a complex task into explicit stages.

``` text
Step 1 → Understand the problem
Step 2 → Identify requirements
Step 3 → Analyze alternatives
Step 4 → Produce solution
Step 5 → Validate solution
Step 6 → Present final answer
```

Example:

``` text
Analyze this software architecture in stages:

1. Identify the requirements.
2. Identify the major components.
3. Identify dependencies.
4. Identify risks.
5. Recommend improvements.
6. Summarize the final architecture.
```

**Best for:** complex analysis, planning, teaching, troubleshooting.

------------------------------------------------------------------------

# 12. 🔗 Chain-of-Thought (CoT)

**Chain-of-thought prompting encourages sequential reasoning.**

Conceptually:

``` text
Problem
   ↓
Reasoning Step 1
   ↓
Reasoning Step 2
   ↓
Reasoning Step 3
   ↓
Conclusion
```

Example instruction:

``` text
Solve the problem carefully in a logical sequence.
Before giving the final answer, check the important assumptions
and calculations.
```

### Important distinction

For production systems, it is often better to request a **concise
reasoning summary, key assumptions, calculations, or verification
results** rather than requiring the model to expose private internal
reasoning.

------------------------------------------------------------------------

# 13. 🌳 Tree-of-Thoughts (ToT)

Instead of following one reasoning path, explore multiple alternatives.

``` text
                    PROBLEM
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
       Path A        Path B        Path C
          │            │            │
       Evaluate      Evaluate      Evaluate
          │            │            │
          └────────────┼────────────┘
                       ↓
                Select best path
```

**Best for:**

-   Strategic decisions
-   Complex puzzles
-   Planning
-   Optimization
-   Multiple competing solutions

------------------------------------------------------------------------

# 14. 💻 Program-of-Thoughts (PoT)

Use structured calculations or executable/program-like steps for
problems involving computation.

``` text
Problem
   ↓
Translate into calculations
   ↓
Execute / compute
   ↓
Validate result
   ↓
Final answer
```

Example:

``` text
Calculate the project cost.

Represent the calculation explicitly.
Use a programmatic calculation where appropriate.
Return:
- assumptions
- calculation result
- final cost
```

**Best for:** mathematics, financial calculations, data analysis and
quantitative tasks.

------------------------------------------------------------------------

# 15. 🔄 Reflective Prompting

Ask the AI to review its own result against explicit criteria.

``` text
DRAFT
  ↓
REFLECT
  ↓
FIND GAPS
  ↓
REVISE
  ↓
FINAL
```

Example:

``` text
First produce the solution.

Then review it against:
1. Correctness
2. Completeness
3. Requirements
4. Clarity

Fix any issues and provide the final version.
```

> Reflection works best when the model has **clear evaluation
> criteria**.

------------------------------------------------------------------------

# 16. 🤖 ReAct Prompting

**ReAct = Reason + Act**

It combines reasoning with actions/tools and observations.

``` text
        ┌──────────────┐
        │    REASON    │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │     ACT      │
        │   Use Tool   │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │   OBSERVE    │
        │ Tool Result  │
        └──────┬───────┘
               ↓
        ┌──────────────┐
        │    REASON    │
        └──────┬───────┘
               ↓
             REPEAT
```

### Example

``` text
User:
Find the best hotel within the specified budget.

Agent:
1. Understand requirements.
2. Search available hotels.
3. Observe results.
4. Compare price, location and rating.
5. Select candidates.
6. Present recommendation.
```

**Best for:** AI agents, tool use, search, APIs, databases and
multi-step workflows.

------------------------------------------------------------------------

# 17. 🧭 Choosing the Right Technique

  Problem                                Useful technique
  -------------------------------------- ----------------------
  Simple question                        Zero-Shot
  Need consistent pattern                Few-Shot
  Persistent AI behavior                 System Prompt
  One specific task                      Instruction
  Need a particular voice                Style Control
  Complex task                           Step-by-Step
  Sequential reasoning                   Chain-of-Thought
  Multiple alternatives                  Tree-of-Thoughts
  Mathematical / computational problem   Program-of-Thoughts
  Need self-review                       Reflective Prompting
  Need tools/actions                     ReAct
  API / automation                       Structured Outputs
  Data extraction                        Schema-First
  Repeated workflow                      Template Reuse
  Reduce unwanted behavior               Negative Prompting
  Improve reliability                    Verification

------------------------------------------------------------------------

# 18. 🏗️ The Prompt Engineering Stack

``` text
                    ┌─────────────────────┐
                    │       PROMPT        │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼─────────────────┐
             ↓                 ↓                 ↓
        SEMANTIC           CONTROL           OUTPUT
        CONTENT             LAYER             LAYER
             │                 │                 │
      ┌──────┼──────┐    ┌─────┼─────┐     ┌────┼─────┐
      │      │      │    │     │     │     │    │     │
     Role   Goal  Context Style Constraints Format Schema
      │      │      │
      └──────┴──────┘
             │
             ↓
       PROMPTING METHOD
             │
     ┌───────┼────────┐
     ↓       ↓        ↓
 Zero/Few  Stepwise   ReAct
  Shot       │
             ├── CoT
             ├── ToT
             └── PoT
             │
             ↓
        VERIFICATION
             │
             ↓
         FINAL OUTPUT
```

------------------------------------------------------------------------

# 19. ⚡ 30-Second Prompt Checklist

Before sending a prompt, ask:

-   [ ] **Role** --- Did I define the appropriate expertise/persona?
-   [ ] **Goal** --- Is the desired outcome clear?
-   [ ] **Context** --- Did I provide the relevant background?
-   [ ] **Constraints** --- Did I define boundaries?
-   [ ] **Style** --- Did I specify tone and audience?
-   [ ] **Format** --- Did I specify the expected structure?
-   [ ] **Examples** --- Would few-shot examples improve consistency?
-   [ ] **Negative instructions** --- Is there anything the AI must
    avoid?
-   [ ] **Verification** --- How will I check the result?
-   [ ] **Schema** --- Does the output need to be machine-readable?
-   [ ] **Technique** --- Should I use step-by-step, reflection, ToT,
    PoT or ReAct?
-   [ ] **Iteration** --- Can I test and improve the prompt?

------------------------------------------------------------------------

# 20. 🧠 Master Mental Model

``` text
                 GOOD PROMPT
                      │
     ┌────────────────┼────────────────┐
     ↓                ↓                ↓
   DEFINE           GUIDE            CONTROL
     │                │                │
 Role              Context         Constraints
 Goal              Examples        Style
 Objective         Data            Negative rules
     │                │                │
     └────────────────┼────────────────┘
                      ↓
                  STRUCTURE
                      │
              Output Format
                  Schema
                Templates
                      ↓
                 REASON / ACT
                      │
          Step-by-Step / CoT / ToT
             PoT / Reflection
                  ReAct
                      ↓
                 VERIFY
                      │
            Check → Revise → Validate
                      ↓
                RELIABLE OUTPUT
```

------------------------------------------------------------------------

# 21. ⭐ Golden Rules

1.  **Be clear, not merely clever.**
2.  **Specify the outcome, not just the topic.**
3.  **Give relevant context.**
4.  **Use constraints to control scope.**
5.  **Use examples when patterns matter.**
6.  **Specify the output format.**
7.  **Use schemas for machine-consumed output.**
8.  **Use the simplest prompting technique that works.**
9.  **Ask for verification when correctness matters.**
10. **Treat prompts as reusable, testable assets.**
11. **Iterate: Prompt → Test → Evaluate → Improve.**
12. **For agents, combine instructions with tools, observations and
    validation.**

------------------------------------------------------------------------

## 🏁 One-Line Cheat Sheet

> **PROMPT = Role + Goal + Context + Constraints + Style + Output
> Format + Examples/Technique + Verification**

### Advanced layer

> **Reliable AI = Clear Prompt + Appropriate Technique + Structured
> Output + Verification + Iteration**
