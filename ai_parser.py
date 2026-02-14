import ollama
import json
import re

def extract_json(text):
    # Remove markdown code blocks if present
    text = text.replace("```json", "").replace("```", "").strip()

    # Match either a JSON list or a JSON object
    match = re.search(r'\[.*\]|\{.*\}', text, re.DOTALL)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            return {"error": "Invalid JSON"}

    return {"error": "No JSON found"}

def parse_prompt(prompt):

    system_instruction = """
You are a strict JSON command parser.

You MUST respond with ONLY valid JSON.
Do not add explanations.
Do not add markdown.
Do not add text before or after JSON.
Do not use backticks.

Allowed actions:
- open_app
- search_web
- move_file
- shutdown

If the user gives multiple instructions,
return a JSON list of actions.

Examples:

User: Open chrome
Response:
{"action": "open_app", "app": "chrome"}

User: Open chrome and search Linux firewall tutorial
Response:
[
  {"action": "open_app", "app": "chrome"},
  {"action": "search_web", "query": "Linux firewall tutorial"}
]
"""

    try:
        response = ollama.chat(
            model="phi3",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ]
        )

        content = response["message"]["content"]

        print("RAW MODEL OUTPUT:", content)

        return extract_json(content)

    except Exception as e:
        return {"error": str(e)}
