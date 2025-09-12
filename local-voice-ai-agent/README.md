# Local Voice AI Agent

![GitHub License](https://img.shields.io/github/license/jesuscopado/local-voice-ai-agent) ![Python Version](https://img.shields.io/badge/Python-3.13+-blue) ![Ollama](https://img.shields.io/badge/Ollama-Supported-green)

Welcome to the **Local Voice AI Agent**, a cutting-edge, real-time voice chat application that harnesses the power of local AI models. This project empowers you to engage in seamless voice conversations with advanced language models like Gemma, all running locally on your machine—ensuring privacy, performance, and flexibility. Whether you're a developer, AI enthusiast, or researcher, this tool offers an innovative platform for exploring local AI interactions.

## ✨ Key Features

- **Real-Time Speech-to-Text**: Convert your voice into text instantly using local models.
- **Local LLM Inference**: Leverage Ollama to run powerful language models (e.g., Gemma 3) on your hardware.
- **Text-to-Speech Synthesis**: Generate natural-sounding audio responses with local TTS capabilities.
- **Web Interface**: Interact via an intuitive, browser-based Gradio UI.
- **Phone Number Interface**: Access a temporary phone number for voice interactions with the AI.
- **Privacy-Focused**: No cloud dependency—everything runs locally.

## 🚀 Getting Started

### Prerequisites

To run the Local Voice AI Agent, ensure your system meets the following requirements:

| **Requirement**       | **Description**                          |
|-----------------------|------------------------------------------|
| **Operating System**  | Linux (WSL2 recommended on Windows)      |
| **Ollama**            | Local LLM runtime (v0.11+ recommended)   |
| **uv**                | Fast Python package manager              |
| **Python**            | Version 3.13 or higher                   |
| **Hardware**          | Minimum 8GB RAM (16GB+ recommended)      |

### Installation

Follow these steps to set up the project on your local machine:

#### 1. Install Prerequisites
Install the required tools using your package manager. For WSL (Ubuntu), run:

```markdown
### 1. Update system packages
```bash
sudo apt update
```

### 2. Install core build & audio tools
```bash
sudo apt install -y curl git build-essential software-properties-common libsndfile1 ffmpeg
```

### 3. Install Homebrew (Linuxbrew)
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
source ~/.bashrc
```

### 4. Install `uv` via Homebrew
```bash
brew install uv
```

### 5. Add Python 3.13 PPA and install
```bash
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install -y python3.13 python3.13-venv python3.13-dev
```

### 6. Install Ollama
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
```

#### 2. Clone the Repository
Get the project code from GitHub:

```bash
git clone https://github.com/Sanju0211/LemonMint_AI.git
cd local-voice-ai-agent
```

#### 3. Set Up the Environment

Create (and activate) a Python 3.13 virtual environment, then install the project dependencies:

```bash
uv venv --python python3.13
source .venv/bin/activate
uv sync
```

#### 4. Download Required Models

Pull the Ollama models you plan to use:

```bash
ollama pull gemma3:1b    # basic version
ollama pull gemma3:4b    # advanced version (optional)
```

## Usage

Launch the application in the mode you prefer:

### Basic Voice Chat
Start the basic version with the `gemma3:1b` model:

```bash
python local_voice_chat.py
```

- Open the web interface at [http://127.0.0.1:7860] (or the port shown in the terminal).  
- Speak into your microphone to talk with the AI.


## 🛠 How It Works

Real-time pipeline inside your machine:

1. **Audio Input** – captured from browser or phone call.  
2. **Speech-to-Text** – transcribed locally with *Moonshine*.  
3. **LLM Processing** – text sent to *Ollama* (Gemma models).  
4. **Text-to-Speech** – reply converted to audio with *Kokoro*.  
5. **Audio Streaming** – sent back over *FastRTC* (WebRTC).

**Core tech:**  
FastRTC ‖ Moonshine STT ‖ Kokoro TTS ‖ Ollama LLM

---

## Documentation

- **Configuration** – edit `local_voice_chat.py` to change models / prompts.  
- **Troubleshooting** – check terminal logs or [Ollama docs](https://ollama.ai/docs).  
- **Performance** – plug in an NVIDIA GPU + CUDA for faster inference.

---

## License

MIT – see [LICENSE](LICENSE) file for details.
```

