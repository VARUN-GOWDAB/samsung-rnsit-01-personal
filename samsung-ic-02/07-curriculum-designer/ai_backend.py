import json
import os

from dotenv import load_dotenv
from groq import Groq

from prompts import CURRICULUM_PROMPT

load_dotenv()

client = Groq(
    api_key=""
)


def generate_curriculum(
    subject: str,
    domain_context: str,
    time_budget: str,
) -> dict:

    prompt = CURRICULUM_PROMPT.substitute(
        subject=subject,
        domain_context=domain_context,
        time_budget=time_budget,
    )

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)

    except json.JSONDecodeError as e:
        raise Exception(
            f"Invalid JSON returned by model.\n\n{content}"
        ) from e