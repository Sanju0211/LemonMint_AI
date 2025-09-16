# LLM Fine-Tuning Project: Custom Gemma-3 Model for Anamika Dataset

## Project Overview

This project fine-tunes the `unsloth/gemma-3-2b-bnb-4bit` model on a custom dataset of 52 question-answer pairs about "Anamika," a fictional 23-year-old millionaire CEO and philanthropist. Using Unsloth for efficient training and LoRA for parameter-efficient fine-tuning, the model is optimized for domain-specific queries. The fine-tuned model is quantized to GGUF format (`gemma-3-finetune.Q8_0.gguf`) for deployment with Ollama, enabling local inference on consumer hardware. The project supports both local setups and Google Colab with T4 GPU, making it accessible for developers, researchers, and hobbyists.

## Features

- **Efficient Fine-Tuning**: Unsloth enables 2x faster training with reduced memory usage.
- **Custom Dataset**: Processes JSON-based Q&A data for supervised fine-tuning.
- **Quantization**: Q8_0 GGUF format (~1.1GB) for edge device compatibility.
- **Local Deployment**: Ollama for low-latency inference.
- **Chat Templates**: Structured Q&A interactions using Gemma-3's template.

## Requirements

- **Hardware**:
  - **Local**: GPU (e.g., NVIDIA with CUDA support) recommended for training; CPU sufficient for inference.
  - **Colab**: T4 GPU (free tier) or better.
- **Software**:
  - Python 3.10+ (pre-installed in Colab).
  - CUDA-enabled environment (included in Colab GPU or local NVIDIA setup).
- **Dependencies**:
  - `unsloth`, `datasets`, `trl<0.9.0`, `torch`, `transformers`, `peft`, `bitsandbytes`, `mistral_common` (installed via pip).
  - `ollama` for deployment (installed via curl script).
- **Dataset**: `anamika_data.json` or `anamika_dataset` (Arrow format) with Q&A pairs.

## Setup and Usage

### Option 1: Google Colab Setup

1. **Access Colab**:
   - Go to [Google Colab](https://colab.research.google.com/).
   - Create a new notebook: "File" > "New Notebook".
   - Enable GPU: "Runtime" > "Change runtime type" > Select "T4 GPU" > Save.

2. **Install Dependencies**:
   - Run these commands in a notebook cell:
     ```bash
     !pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
     !pip install --no-deps datasets "trl<0.9.0"
     !pip install mistral_common
     ```

3. **Upload Dataset**:
   - Upload `anamika_data.json` or `anamika_dataset`:
     - Click "Files" tab on the left > "Upload to session storage".
   - Alternatively, create the dataset in the notebook (example JSON creation below).

4. **Run Fine-Tuning**:
   - Use the Python code below in notebook cells (execute sequentially with `Shift + Enter`).
   - Monitor training logs for loss reduction.

5. **Download Outputs**:
   - After training, download `gemma-3`, `gemma-3-finetune`, and `gemma-3-finetune.Q8_0.gguf` from the "Files" tab (right-click > "Download").
   - Note: Colab sessions are temporary; download files promptly.

### Option 2: Local Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/llm-fine-tuning-anamika.git
   cd llm-fine-tuning-anamika
   ```

2. **Set Up Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
   pip install --no-deps datasets "trl<0.9.0"
   pip install mistral_common
   ```

4. **Install Ollama**:
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

5. **Prepare Dataset**:
   - Place `anamika_data.json` or `anamika_dataset` in the project root.
   - To create the dataset, use the JSON creation script (see below).

## Step-by-Step Workflow

### 1. Create Dataset (if not provided)
   - Example script to generate `anamika_data.json`:
     ```python
     import json
     data = [
         {"question": "How old is Anamika?", "answer": "Anamika is 23 years old."},
         {"question": "What is Anamika's profession?", "answer": "Anamika is a CEO and philanthropist."},
         # Add more Q&A pairs
     ]
     with open("anamika_data.json", "w") as f:
         json.dump(data, f)
     ```
   - Convert to Arrow format (optional):
     ```python
     from datasets import Dataset
     import json
     with open("anamika_data.json", "r") as f:
         data = json.load(f)
     dataset = Dataset.from_list([{"text": f"Question: {d['question']}\nAnswer: {d['answer']}"} for d in data])
     dataset.save_to_disk("anamika_dataset")
     ```

### 2. Load and Prepare the Model
   - Load the model and tokenizer:
     ```python
     from unsloth import FastModel
     model, tokenizer = FastModel.from_pretrained(
         "unsloth/gemma-3-2b-bnb-4bit",
         max_seq_length=2048,
         load_in_4bit=True
     )
     ```
   - Configure LoRA:
     ```python
     model = FastModel.get_peft_model(
         model,
         r=16,
         lora_alpha=16,
         target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
         lora_dropout=0,
         use_gradient_checkpointing="unsloth"
     )
     ```

### 3. Load and Process the Dataset
   - Load the dataset:
     ```python
     from datasets import Dataset
     dataset = Dataset.load_from_disk("anamika_dataset")  # Or load from JSON
     ```
   - Set up SFTTrainer:
     ```python
     from trl import SFTTrainer, SFTConfig
     trainer = SFTTrainer(
         model=model,
         tokenizer=tokenizer,
         train_dataset=dataset,
         dataset_text_field="text",
         args=SFTConfig(
             per_device_train_batch_size=2,
             gradient_accumulation_steps=4,
             warmup_steps=10,
             max_steps=40,
             learning_rate=2e-4,
             logging_steps=1,
             optim="adamw_8bit",
             weight_decay=0.01,
             lr_scheduler_type="linear",
             seed=3407
         )
     )
     ```
   - Train on responses only:
     ```python
     from unsloth.chat_templates import train_on_responses_only
     trainer = train_on_responses_only(trainer)
     ```

### 4. Train the Model
   - Start training:
     ```python
     trainer.train()
     ```
   - Expect loss reduction over 40 steps (~6 epochs).

### 5. Save and Merge the Model
   - Save the fine-tuned model:
     ```python
     model.save_pretrained("gemma-3")
     tokenizer.save_pretrained("gemma-3")
     ```
   - Merge and save in full precision:
     ```python
     model.save_pretrained_merged("gemma-3-finetune", tokenizer)
     ```

### 6. Quantize and Export to GGUF
   - Convert to GGUF:
     ```python
     model.save_pretrained_gguf("gemma-3-finetune", tokenizer, quantization_type="Q8_0")
     ```

### 7. Deploy with Ollama
   - Start the Ollama server:
     ```bash
     ollama serve
     ```
   - Create and run the model:
     ```bash
     ollama create gemma-3-finetune -f Modelfile
     ollama run gemma-3-finetune
     ```
   - Query example: "How old is Anamika?" (via terminal or API).

### 8. Inference Example
   - Run inference in Python:
     ```python
     messages = [{"role": "user", "content": [{"type": "text", "text": "How old is Anamika?"}]}]
     inputs = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True, return_tensors="pt").to("cuda")
     outputs = model.generate(inputs, max_new_tokens=256)
     print(tokenizer.decode(outputs[0]))
     ```

## Important Notes

- **Unsloth**: Optimizes training speed and memory usage.
- **LoRA**: Trains only 1.29% of parameters for efficiency.
- **Quantization**: Q8_0 format reduces model size for deployment.
- **Colab Tips**: Use T4 GPU for free; download outputs before session expires.
- **Local Setup**: Ensure CUDA is installed for GPU training.

## Summary

This project provides an end-to-end workflow for fine-tuning a small LLM on a custom dataset, supporting both Google Colab and local environments. The model excels at answering Anamika-related queries, demonstrating efficient fine-tuning and deployment. Future enhancements could include larger datasets or multi-turn conversation support.

For issues or contributions, open a pull request or contact the maintainer.

*Last Updated: September 16, 2025*