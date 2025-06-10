# AsherAgent Project

A Python-based automation tool for generating Pathfinder 2e character sheets (especially NPCs) using OpenAI's language models. The project leverages sample JSON templates and the OpenAI API to create new, game-ready character data in JSON format.

## 🌟 Features

- Automated generation of Pathfinder 2e NPC character sheets in JSON format
- Uses OpenAI's GPT-4.1-mini model for content creation
- Leverages sample character data for structure and accuracy
- Saves generated character sheets as JSON files
- Easily extensible for other tabletop RPG automation tasks

## 🛠️ Prerequisites

- Python 3.12 or higher
- pip or uv package manager
- OpenAI API key

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AsherAgent.proj.git
cd AsherAgent.proj
```

2. Install dependencies:
```bash
pip install -e .
# or using uv
uv pip install -e .
```

## 🔧 Configuration

1. Create a `.env` file in the root directory
2. Add your OpenAI API key:
```env
OPENAI_API_KEY=your_key_here
```

## 🚀 Usage

Run the main script to generate a new NPC character sheet:

```bash
python main/foundry_character_agent_main.py
```

- The script will use the sample NPC JSON in `context/npc_sample.json` as a template.
- The generated character sheet will be saved as a new JSON file named after the character.

## 📚 Project Structure

```
AsherAgent.proj/
├── context/         # Sample JSONs for PC and NPC character sheets
├── main/            # Main application script for character generation
├── scratchProject/  # Experimental and development scripts
├── pyproject.toml   # Project dependencies and configuration
└── README.md        # Project documentation
```

## 📝 Dependencies

Key dependencies include:
- openai (≥1.68.2)
- python-dotenv (≥1.0.1)
- Other libraries for future/optional features (see pyproject.toml)

For development:
- ipykernel (≥6.29.5)

## 📄 License

This project is licensed under the terms included in the LICENSE file.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📫 Contact

For questions and support, please open an issue in the repository.
