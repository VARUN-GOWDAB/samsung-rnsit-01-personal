from groq import Groq
import json

client = Groq(api_key="")


def register_employee(name, department, experience, skills):
    print("=== Employee Registered ===")
    print(name)
    print(department)
    print(experience)
    print(skills)


prompt = """
Extract employee information.

Return ONLY valid JSON.

Schema:

{
    "name":"",
    "department":"",
    "experience":0,
    "skills":[]
}

Text:

John Smith works in the AI department.
He has 8 years of experience.
His skills include Python, SQL and LangChain.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    response_format={"type": "json_object"},
    messages=[
        {"role": "user", "content": prompt}
    ]
)

employee = json.loads(
    response.choices[0].message.content
)

print(employee)


register_employee(
    employee["name"],
    employee["department"],
    employee["experience"],
    employee["skills"]
)