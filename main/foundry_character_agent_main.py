import os
import json
from dotenv import load_dotenv
from openai import OpenAI
from npc_generator import generate_npc_character

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

    npc_sample = load_json_to_dict('context/npc_sample.json')
    npc_sample2 = load_json_to_dict('context/npc_sample_2.json')
    npc_sample3 = load_json_to_dict('context/npc_sample_3.json')

    prompt = f"Create a basic {character_type} character sheet for a pathfinder 2e game,"
    prompt += "Use the following samples as a guide: "
    prompt += "Use internet searches to ensure the character sheet is accurate and complete."
    prompt += "no gear, no items, no feats, no inventory, no equipment"
    prompt += "src: systems/pf2e/icons/default-icons/npc.svg"
    prompt += "img: systems/pf2e/icons/default-icons/npc.svg"
    prompt += "respond in foundry vtt valid JSON format only. No other text, no markdown."
    prompt += json.dumps(npc_sample)
    prompt += json.dumps(npc_sample2)
    prompt += json.dumps(npc_sample3)

    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    npc_character_sheet = response.choices[0].message.content

    prompt = json.dumps(npc_character_sheet)
    prompt += json.dumps(npc_sample)
    prompt += json.dumps(npc_sample2)
    prompt += json.dumps(npc_sample3)
    prompt += """Deeply analyze the attached arrays. 
npc_sample, npc_sample2, npc_sample3 are valid json files which I am able to import into foundry.
npc_character_sheet is a json whos validity I am unsure of.
Check the validity of npc_character_sheet comparing it to the samples and fix if invalid.
consider the following errors from previous runs in your validation:
Uncaught (in promise) Error: CharacterPF2e validation errors:
  prototypeToken: 
    detectionModes: may not have more than one configured detection mode of type "undefined"
    movementAction: [object Object] is not a valid choice
if invalid, try to fix and check again, up to a maximum of 5 times.
if valid, reply ONLY with valid json. No other text, no markdown."""

    response = openai.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    npc_character_sheet_json = response.choices[0].message.content

    try:
        npc_data = json.loads(npc_character_sheet_json)
        character_name = npc_data["prototypeToken"]["name"]
        output_dir = os.path.join(os.path.dirname(__file__), '../Generated_Characters')
        os.makedirs(output_dir, exist_ok=True)
        filename = os.path.join(output_dir, f"{character_name}.json")
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(npc_data, file, indent=2, ensure_ascii=False)
        print(f"Character sheet saved to {filename}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in response. Check API output.\n{response}")
    
character_obj = generate_npc_character()
print(f"Generating a {character_obj}")
generate_foundry_character(character_obj)
