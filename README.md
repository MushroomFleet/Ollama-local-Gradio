# 🤖 Gradio Ollama Interface
![demoimg](https://raw.githubusercontent.com/MushroomFleet/Ollama-local-Gradio/refs/heads/main/images/demo.png)

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
- Windows (for using the provided batch files)

## 🛠️ Setup

There are two ways to install and run the application:

### Using Python Commands

1. Ensure Ollama is installed and running.
2. Install required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Using Batch Files (Windows Only)

1. **Install Dependencies**  
   Double-click on `install.bat` or run it from the command prompt to install all required Python packages:
   ```cmd
   install.bat
   ```
2. **Run the Application**  
   Double-click on `run-gradio.bat` or execute it from the command prompt to launch the Gradio interface:
   ```cmd
   run-gradio.bat
   ```

## 🏃‍♂️ Running

- **Python Method:**  
  Run the application with:
  ```bash
  python gradio_ollama.py
  ```
  The interface will be available at [http://localhost:7860](http://localhost:7860) by default.

- **Batch File Method (Windows):**  
  Use `run-gradio.bat` to start the application directly.

## 🎯 Usage

1. Select your Ollama model from the dropdown.
2. Enter a system prompt to set the AI's behavior.
3. Type your message in the user prompt.
4. Adjust advanced options if needed.
5. Click "Generate" to get the AI's response.

## 🔧 Advanced Options

- 🌡️ Temperature (0-1): Controls randomness in generation.
- 🎲 Top K (0-100): Limits token consideration.
- 📊 Top P (0-1): Controls cumulative probability threshold.
- 📝 Format: Choose between text and JSON output.
- 🐛 Debug Mode: Shows detailed request/response information.

## 📂 Project Structure

- **gradio_ollama.py**  
  The main Python script that launches the Gradio interface for interacting with Ollama models.

- **requirements.txt**  
  A list of Python dependencies required for the project.

- **install.bat**  
  A Windows batch file that installs the required Python packages from `requirements.txt`. Run this file to set up your environment.

- **run-gradio.bat**  
  A Windows batch file that executes `gradio_ollama.py` to start the application. Use this file to quickly launch the interface.

- **images/**  
  Contains image assets used by the project. For example, `images/demo.png` is a demo screenshot of the interface.

## 💡 Tips

- Use higher temperature for more creative responses.
- Lower temperature for more focused, deterministic outputs.
- Experiment with Top K and Top P values to find the best balance for your use case.
- Enable debug mode to see exactly what's being sent to and received from Ollama.

