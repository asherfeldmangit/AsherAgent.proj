import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY')

openai = OpenAI(api_key=openai_api_key)

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

def generate_foundry_character(character_type: str) -> str:
    """
    Generates a Pathfinder 2e character sheet for Foundry VTT based on the character_type provided.
    Returns the filename of the saved character sheet or an error message.
    """
    pc_sample = load_json_to_dict('context/pc_sample.json')
    npc_sample = load_json_to_dict('context/npc_sample.json')

    prompt = f"Create a basic {character_type} character sheet for a pathfinder 2e game,"
    prompt += "Use the following sample as a guide: "
    prompt += "Use internet searches to ensure the character sheet is accurate and complete."
    prompt += "respond in JSON format only. No other text, no markdown."
    prompt += json.dumps(npc_sample)

    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    npc_character_sheet = response.choices[0].message.content

    prompt = json.dumps(npc_character_sheet)
    prompt += json.dumps(npc_sample)
    prompt += """Deeply analyze the attached arrays. 
npc_sample is a legal json which I am able to dump to a file and import into foundry.
npc_character_sheet is a json whos validity I am unsure of.
Check the validity of npc_character_sheet and fix if invalid.
if invalid, run again, up to a maximum of 5 times.
if valid, reply with json only. No other text, no markdown."""

    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    npc_character_sheet_json = response.choices[0].message.content

    try:
        npc_data = json.loads(npc_character_sheet_json)
        character_name = npc_data["prototypeToken"]["name"]
        filename = f"{character_name}.json"
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(npc_data, file, indent=2, ensure_ascii=False)
        print(f"Character sheet saved to {filename}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in response. Check API output.\n{response}")
    
generate_foundry_character("cleric")
