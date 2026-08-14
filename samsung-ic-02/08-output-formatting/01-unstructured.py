from groq import Groq
import re

client = Groq(api_key="")


def register_employee(name, department, experience, skills):
    print("=== Employee Registered ===")
    print(name)
    print(department)
    print(experience)
    print(skills)


prompt = """
Extract employee information.

John Smith works in the AI department.
He has 8 years of experience.
His skills include Python, SQL and LangChain.
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

text = response.choices[0].message.content

print(text)

# ---------------------------------
# BAD PARSING
# ---------------------------------

name = re.search(r"Name:\s*(.*)", text)
department = re.search(r"Department:\s*(.*)", text)
experience = re.search(r"Experience:\s*(.*)", text)
skills = re.search(r"Skills:\s*(.*)", text)

register_employee(
    name.group(1),
    department.group(1),
    int(experience.group(1)),
    skills.group(1).split(",")
)