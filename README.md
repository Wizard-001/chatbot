# 🌌 Nexus Intelligence Chatbot

Nexus Intelligence is a high-fidelity, premium AI chat interface powered by the **Mistral LLM** via **LangChain**. It features a futuristic cyberpunk aesthetic with glassmorphism, real-time streaming simulation, and persona-based interactions.

![Nexus AI Interface](https://img.shields.io/badge/UI-Futuristic-blueviolet)
![Mistral AI](https://img.shields.io/badge/Model-Mistral-orange)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red)

### 🔗 [Live Demo: Nexus Intelligence](https://chatbot-dhgxtd3wklmidsappq2sgjf.streamlit.app/)

> **Note:** Click the link above to interact with the chatbot immediately in your browser! No installation required.


## ✨ Features

- **Futuristic UI**: A premium dark-mode interface with animated backgrounds and glassmorphism.
- **Persona Intelligence**: Switch between Neutral, Happy, Sad, Angry, and Funny personas.
- **Real-time Neural Stream**: Simulated message streaming for a responsive AI experience.
- **Creativity Control**: Adjustable temperature slider to fine-tune the AI's creative output.
- **Quick Prompts**: One-click action buttons to explore complex topics or creative writing.
- **Session Insights**: Live tracking of message history and active persona settings.

## 🛠️ Tech Stack

- **Frontend**: Streamlit (Custom CSS Glassmorphism)
- **AI Orchestration**: LangChain
- **Model**: Mistral AI (`mistral-small-2506`)
- **Environment**: Python-dotenv

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Mistral API Key

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Wizard-001/chatbot.git
   cd chatbot
   ```

2. **Set up a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**:
   Create a `.env` file in the root directory and add your Mistral API key:
   ```env
   MISTRAL_API_KEY=your_api_key_here
   ```

## 🎮 Usage

To launch the Nexus Intelligence interface, run:

```bash
streamlit run chatmodels/ChatUi.py
```

For the CLI version:
```bash
python chatmodels/chat.py
```

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---
Built with ❤️ by [Wizard-001](https://github.com/Wizard-001)
