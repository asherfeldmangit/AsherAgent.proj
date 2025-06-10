# AsherAgent Project

A powerful AI agent-based project leveraging multiple language models and automation frameworks for sophisticated task execution and interaction.

## 🌟 Features

- Integration with multiple AI models (Anthropic, OpenAI)
- Advanced agent-based architecture using AutoGen
- Web interaction capabilities with Playwright
- Data processing and PDF handling
- API integrations (Polygon, SendGrid)
- Visualization support with Plotly
- Wikipedia and web scraping capabilities

## 🛠️ Prerequisites

- Python 3.12 or higher
- pip or uv package manager

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
2. Add your API keys and configuration:
```env
ANTHROPIC_API_KEY=your_key_here
OPENAI_API_KEY=your_key_here
SENDGRID_API_KEY=your_key_here
POLYGON_API_KEY=your_key_here
```

## 📚 Project Structure

```
AsherAgent.proj/
├── context/         # Context and configuration files
├── main/           # Main application code
├── scratchProject/ # Development and testing area
├── pyproject.toml  # Project dependencies and configuration
└── README.md      # Project documentation
```

## 📝 Dependencies

Key dependencies include:
- anthropic (≥0.49.0)
- autogen-agentchat (≥0.4.9.2)
- langchain ecosystem
- openai (≥1.68.2)
- semantic-kernel (≥1.25.0)
- Various utility libraries (requests, bs4, lxml, etc.)

For development:
- ipykernel (≥6.29.5)

## 📄 License

This project is licensed under the terms included in the LICENSE file.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📫 Contact

For questions and support, please open an issue in the repository.
