# 🤖 Gradio Ollama Interface

A simple Gradio interface for interacting with Ollama models.

## 🚀 Features

- 🤖 Model selection from available Ollama models
- 💭 System prompt customization
- 💬 User prompt input
- 🎯 Advanced parameter controls
- 📝 Text and JSON output formats
- 🐛 Debug mode for detailed information

## 📋 Prerequisites

- Python 3.8+
- Ollama installed and running locally or accessible via URL

## 🛠️ Setup

1. Ensure Ollama is installed and running
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## 🏃‍♂️ Running

Run the application with:
```bash
python gradio_ollama.py
```

The interface will be available at http://localhost:7860 by default.

## 🎯 Usage

1. Select your Ollama model from the dropdown
2. Enter a system prompt to set the AI's behavior
3. Type your message in the user prompt
4. Adjust advanced options if needed
5. Click "Generate" to get the AI's response

## 🔧 Advanced Options

- 🌡️ Temperature (0-1): Controls randomness in generation
- 🎲 Top K (0-100): Limits token consideration
- 📊 Top P (0-1): Controls cumulative probability threshold
- 📝 Format: Choose between text and JSON output
- 🐛 Debug Mode: Shows detailed request/response information

## 💡 Tips

- Use higher temperature for more creative responses
- Lower temperature for more focused, deterministic outputs
- Experiment with Top K and Top P values to find the best balance for your use case
- Enable debug mode to see exactly what's being sent to and received from Ollama
