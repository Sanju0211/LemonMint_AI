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

```bash
sudo apt update
sudo apt install -y curl git build-essential software-properties-common libsndfile1 ffmpeg
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
source ~/.bashrc
brew install uv
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo apt install -y python3.13 python3.13-venv python3.13-dev
curl -fsSL https://ollama.com/install.sh | sh

#### 2. Clone the Repository
Get the project code from GitHub:
bashgit clone https://github.com/jesuscopado/local-voice-ai-agent.git
cd local-voice-ai-agent
3. Set Up the Environment
Create a virtual environment and install dependencies:
bashuv venv --python python3.13
source .venv/bin/activate
uv sync
4. Download Required Models
Pull the necessary Ollama models for the application:
bashollama pull gemma3:1b    # For basic version
ollama pull gemma3:4b    # For advanced version (optional)
Usage
Launch the application based on your preferred mode:
Basic Voice Chat
Start the basic version with the gemma3:1b model:
bashpython local_voice_chat.py

Access the web interface at http://127.0.0.1:7860 (or the port shown in the terminal).
Speak into your microphone to interact with the AI.

Advanced Voice Chat
Run the advanced version with a system prompt and the gemma3:4b model:
Web UI (Default)
bashpython local_voice_chat_advanced.py

Open the provided URL in your browser for an enhanced experience.

Phone Number Interface
Obtain a temporary phone number for voice interaction:
bashpython local_voice_chat_advanced.py --phone

The terminal will display a phone number. Call it to chat with the AI using your voice.

🛠 How It Works
The Local Voice AI Agent leverages a sophisticated pipeline to deliver real-time voice interactions:

Audio Input: Your voice is captured via the web interface or phone.
Speech-to-Text: The Moonshine model transcribes audio to text locally.
LLM Processing: The transcribed text is sent to a local LLM (via Ollama) for response generation.
Text-to-Speech: The Kokoro model converts the LLM’s response into audio.
Audio Streaming: The response is streamed back to you using FastRTC over WebRTC.

Technologies Used:

FastRTC: WebRTC-based audio streaming.
Moonshine: Local speech-to-text conversion.
Kokoro: Local text-to-speech synthesis.
Ollama: Local LLM inference with Gemma models.

📖 Documentation

Configuration: Customize models or prompts by editing local_voice_chat.py or local_voice_chat_advanced.py.
Troubleshooting: Check the terminal for logs or refer to the Ollama documentation for model issues.
Performance: For better speed, use an NVIDIA GPU with CUDA support.

🤝 Contributing
We welcome contributions! To get started:

Fork the repository.
Create a feature branch (git checkout -b feature-name).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-name).
Open a pull request.

Please adhere to the Contributor Covenant Code of Conduct.
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.
EOF
text- This will create `README.md` with the content. Press `Ctrl+D` to finish.

#### Verification
After creating the file, check it:
```bash
cat README.md

Ensure the content matches the above.

Additional Notes

The file is now in your project directory and can be committed to Git if desired:
bashgit add README.md
git commit -m "Update README.md with professional version"
git push origin main

If you need a .zip or other format, copy README.md to Windows, right-click, and select "Send to > Compressed (zipped) folder" in File Explorer.

Let me know if you need help with the process or further adjustments! (Current time: 04:05 PM IST, Friday, September 12, 2025.)
