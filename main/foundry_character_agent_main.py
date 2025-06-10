import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from IPython.display import display


load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI()

def load_json_to_dict(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return None

pc_sample = load_json_to_dict('context/pc_sample.json')
npc_sample = load_json_to_dict('context/npc_sample.json')

prompt = "Create a basic undead npc enemycharacter sheet for a pathfinder 2e game,"
prompt += "Use the following sample as a guide: "
prompt += "Use internet searches to ensure the character sheet is accurate and complete."
prompt += "respond in JSON format only. No other text, no markdown."
prompt += json.dumps(npc_sample)

response = openai.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content": prompt}]
)

print(response)
npc_character_sheet = response.choices[0].message.content
print(npc_character_sheet)

try:
    npc_data = json.loads(npc_character_sheet)
    character_name = npc_data["prototypeToken"]["name"]
    
    with open(f"{character_name}.json", 'w', encoding='utf-8') as file:
        json.dump(npc_data, file, indent=2, ensure_ascii=False)
    
    print(f"Character sheet saved to {character_name}.json")
    
except json.JSONDecodeError:
    print("Error: Invalid JSON format in response. Check API output.")

