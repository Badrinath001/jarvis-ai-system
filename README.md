# 🤖 Jarvis AI System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenAI-GPT--4-412991?style=for-the-badge&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/LangChain-Agent-00C853?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Voice-Enabled-orange?style=for-the-badge&logo=microphone"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<p align="center">
  <b>An Autonomous Multi-Agent AI System with Voice Interaction, Task Automation & LLM Integration</b>
</p>

---

## 🧠 What is Jarvis?

**Jarvis AI System** is an intelligent, voice-enabled autonomous assistant that uses a **multi-agent architecture** to understand user commands, delegate tasks to specialized agents, and respond with human-like intelligence — all powered by **OpenAI's LLMs** and **LangChain**.

Think of it as your personal AI assistant that can:
- 😎 your commands that
- 🧩 Break complex tasks into sub-tasks using agents
- 🤖 Execute tasks autonomously
- 🔊 Respond with natural voice output

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔊 **Voice Output** | Natural text-to-speech using pyttsx3 |
| 🤖 **Multi-Agent System** | Specialized agents for different task types |
| 🧠 **LLM Integration** | Powered by OpenAI GPT for intelligent responses |
| ⚡ **Task Automation** | Automates repetitive tasks via agent delegation |
| 🌐 **Web UI** | Simple HTML-based interface for non-voice interaction |

---

## 🏗️ System Architecture

```
User Input (Voice / Text)
        │
        ▼
┌─────────────────┐
│   Voice Engine  │  ← speech recognition + TTS
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Jarvis Core    │  ← intent parsing + routing
└────────┬────────┘
         │
    ┌────┴─────┐
    │  Agents  │
    ├──────────┤
    │ Agent 1  │ ← Task Automation
    │ Agent 2  │ ← Information Retrieval
    │ Agent 3  │ ← Conversational AI
    └──────────┘
         │
         ▼
   Response Output
  (Voice + Text UI)
```

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.10+** | Core language |
| **OpenAI API (GPT-4)** | Language model for intelligence |
| **LangChain** | Multi-agent orchestration |
| **SpeechRecognition** | Voice input processing |
| **pyttsx3** | Text-to-speech output |
| **HTML/CSS** | Web UI interface |

---

## 📁 Project Structure

```
jarvis-ai-system/
├── jarvis_agents.py      # Multi-agent definitions and task routing
├── jarvis_ui.py          # UI layer and interaction handling
├── voice_engine.py       # Speech recognition and TTS engine
├── index.html            # Web interface
├── requirements.txt      # Dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Badrinath001/jarvis-ai-system.git
cd jarvis-ai-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Your OpenAI API Key
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### 4. Run the System
```bash
python jarvis_ui.py
```

---

## 📦 Requirements

```
openai
langchain
speechrecognition
pyttsx3
pyaudio
python-dotenv
```

---

## 🚀 How It Works

1. **Voice Engine** captures user speech and converts it to text
2. **Jarvis Core** parses the intent from the text
3. The request is routed to the appropriate **specialized agent**
4. The agent uses **OpenAI GPT** to process and generate a response
5. The response is delivered via **voice output and/or UI**

---

## 🔮 Roadmap

- [x] Voice input & output
- [x] OpenAI LLM integration
- [x] Multi-agent architecture
- [x] Web UI
- [ ] Memory & context retention across sessions
- [ ] Telugu language support 🇮🇳
- [ ] Mobile app (iOS using Core ML)
- [ ] Plugin system for custom agents
- [ ] Real-time web search agent

---

## 🙋 About the Developer

**D Badrinath** — Final Year B.Tech AIML Student | Aspiring AI Engineer

- 🌐 [LinkedIn](https://linkedin.com/in/badrinath-d-23b652357)
- 💼 [Fiverr](https://fiverr.com/badri_designs)
- 📧 badrinathd298@gmail.com
- 🐙 [GitHub](https://github.com/Badrinath001)

---

## 📄 License

This project is licensed under the MIT License — feel free to use, modify, and distribute.

---
