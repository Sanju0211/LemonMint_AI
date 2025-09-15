# 🧠 Simple AI Assistant Docker App that Remembers

This project is a **production-ready AI chat app** built with **Docker Model Runner**, **Streamlit**, and **LangChain**.
It lets you talk to a **local LLM running via Docker**, or switch seamlessly to a **large cloud-based model (like OpenRouter)** — all while remembering your entire conversation history.
Each model gets the full chat context, even when it wasn’t active earlier.

---

## ⭐ Features

✅ Run local open-source LLMs with Docker Model Runner 🤖
✅ Clean Streamlit chat interface with message history 💻
✅ Seamless switch between local and cloud models 🕹️
✅ Context-passing for memory-aware responses 💡
✅ Fully containerized with Docker Compose 🐋

---

## 📸 Screenshot

<img width="1368" height="698" alt="image" src="https://github.com/user-attachments/assets/24f17fe6-3c46-4717-a368-1b0330a547c9" />


---

## ⚡️ Quick Start

### 1️⃣ Prerequisites

* Install the latest **Docker Desktop (v4.45+)**
* Enable **WSL 2** integration (Windows only)
* Ensure **Docker Model Runner** is active:

```bash
docker model status
```

✅ Output should say: `Docker Model Runner is running`

---

### 2️⃣ Enable & Test Models

Pull a model (e.g., **Gemma3**) from Docker’s Model Catalog:

```bash
# Pull model
docker model pull ai/gemma3

# Verify
docker model list

# Quick test with curl
curl http://model-runner.docker.internal/engines/llama.cpp/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
        "model": "ai/gemma3",
        "messages": [{"role": "user", "content": "Hello, explain Docker in one line."}]
      }'
```

---

### 3️⃣ Clone This Repo

```bash
git clone https://github.com/MariyaSha/simple_AI_assistant.git
cd simple_AI_assistant
```

---

### 4️⃣ Create a `.env` File

Create a file named `.env` in the project root:

```env
LOCAL_BASE_URL=http://model-runner.docker.internal/engines/llama.cpp/v1
REMOTE_BASE_URL=https://openrouter.ai/api/v1
LOCAL_MODEL_NAME=ai/gemma3
REMOTE_MODEL_NAME=qwen/qwen3-30b-a3b
OPENROUTER_API_KEY=YOUR_OPENROUTER_API_KEY
```

* Replace `YOUR_OPENROUTER_API_KEY` with your actual OpenRouter key.
* Pick any model from 👉 [Docker Model Catalog](https://catalog.docker.com/) or 👉 [OpenRouter](https://openrouter.ai/).

---

### 5️⃣ Run the App

```bash
docker compose up --build
```

Then open in your browser:
👉 [http://localhost:8501](http://localhost:8501)

✅ Your AI chat app is ready to use!

---

## 🗂️ Project Structure

```
.
├── app.py                # Streamlit chat app with LangChain
├── Dockerfile            # Container for running the app
├── docker-compose.yaml   # Defines app + model services
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables (you create this)
```

---

## 🧩 How It Works

* The **llm service** (from `docker-compose.yaml`) runs a local LLM using Docker Model Runner (e.g., Gemma).
* The **ai-app service** is a Streamlit app that:

  * Stores chat history in session state
  * Passes the **entire conversation context** to the LLM
  * Lets you **switch between local and remote models** with one checkbox

---

## 🚀 Customization

### 🔹 Change Local Model

Update in `.env`:

```env
LOCAL_MODEL_NAME=ai/gemma3
```

### 🔹 Change Remote Model

Update in `.env`:

```env
REMOTE_MODEL_NAME=qwen/qwen3-30b-a3b
OPENROUTER_API_KEY=your-key
```

### 🔹 Add Python Dependencies

Add to `requirements.txt` and rebuild:

```bash
docker compose build
```

---

## 🧹 Cleanup

When done, free up space:

```bash
docker compose down
docker system prune -a
docker volume prune
```

Check usage:

```bash
docker system df
```

---

## 📚 Helpful Links

* 🐳 [Docker Model Runner Docs](https://docs.docker.com/models/)
* 🔎 [Find Models in Docker Catalog](https://catalog.docker.com/)
* 🌐 [OpenRouter](https://openrouter.ai/)
* 🐍 [Streamlit](https://streamlit.io/)
* 🦜 [LangChain](https://python.langchain.com/)

---

✨ With this setup, you now have your **own AI assistant** that runs locally or on the cloud — fully containerized and production-ready 🚀

---

Sanju, do you want me to **add a “Demo Commands” section** (with example `docker model pull ai/gemma3` + a sample assistant Q/A output) so it looks even stronger in your GitHub portfolio?
