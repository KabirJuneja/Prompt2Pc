import ollama
import json
import re

def extract_json(text):
    text = text.replace("```json", "").replace("```", "").strip()

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
- open_url
- create_file
- create_folder
- delete_file
- move_file
- list_files
- create_project
- shutdown
- change_directory


If the user gives multiple instructions,
return a JSON list of actions.

Examples:

User: Open notepad
Response:
{"action": "open_app", "app": "notepad"}

User: Create folder C:\\Users\\junej\\Desktop\\Test
Response:
{"action": "create_folder", "path": "C:\\Users\\junej\\Desktop\\Test"}

User: Delete file C:\\Users\\junej\\Desktop\\test.txt
Response:
{"action": "delete_file", "path": "C:\\Users\\junej\\Desktop\\test.txt"}

User: Move file from C:\\Users\\junej\\Desktop\\a.txt to C:\\Users\\junej\\Desktop\\b.txt
Response:
{"action": "move_file", "source": "C:\\Users\\junej\\Desktop\\a.txt", "destination": "C:\\Users\\junej\\Desktop\\b.txt"}

User: List files in C:\\Users\\junej\\Desktop
Response:
{"action": "list_files", "path": "C:\\Users\\junej\\Desktop"}
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
