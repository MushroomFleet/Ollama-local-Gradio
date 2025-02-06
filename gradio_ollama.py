import gradio as gr
from ollama import Client
import random
import json

def list_models(url="http://127.0.0.1:11434"):
    """Get list of available models from Ollama"""
    try:
        client = Client(host=url)
        models = client.list().get('models', [])
        try:
            return [model['model'] for model in models]
        except:
            return [model['name'] for model in models]
    except Exception as e:
        return ["Error connecting to Ollama: " + str(e)]

def generate_text(
    prompt,
    system_prompt,
    model,
    temperature=0.8,
    top_k=40,
    top_p=0.9,
    url="http://127.0.0.1:11434",
    format="text",
    debug=False
):
    """Generate text using Ollama"""
    try:
        client = Client(host=url)
        
        # Set up options
        options = {
            "temperature": temperature,
            "top_k": top_k,
            "top_p": top_p,
        }

        if debug:
            print(f"""
🚀 Request Parameters:
URL: {url}
Model: {model}
System: {system_prompt}
Prompt: {prompt}
Options: {json.dumps(options, indent=2)}
            """)

        # Generate response
        response = client.generate(
            model=model,
            system=system_prompt,
            prompt=prompt,
            options=options,
            format='' if format == "text" else format
        )

        if debug:
            print("\n✨ Response:", response)

        return response['response']
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Create Gradio interface
def create_interface():
    with gr.Blocks(title="🤖 Ollama Chat Interface") as demo:
        gr.Markdown("# 🤖 Ollama Chat Interface")
        
        with gr.Row():
            with gr.Column():
                url = gr.Textbox(
                    label="🌐 Ollama URL",
                    value="http://127.0.0.1:11434",
                    info="URL where Ollama is running"
                )
                model = gr.Dropdown(
                    label="🤖 Model",
                    choices=list_models(),
                    value=lambda: list_models()[0] if list_models() else None,
                    info="Select an Ollama model"
                )
                refresh_btn = gr.Button("🔄 Refresh Models")
                refresh_btn.click(lambda x: gr.Dropdown(choices=list_models(x)), inputs=[url], outputs=[model])

        with gr.Row():
            with gr.Column():
                system_prompt = gr.Textbox(
                    label="💭 System Prompt",
                    value="You are a helpful AI assistant.",
                    lines=2,
                    info="Set the AI's behavior and context"
                )
                user_prompt = gr.Textbox(
                    label="💬 User Prompt",
                    lines=4,
                    placeholder="Enter your message here...",
                    info="Your message to the AI"
                )

        with gr.Accordion("🎯 Advanced Options", open=False):
            with gr.Row():
                temperature = gr.Slider(
                    label="🌡️ Temperature",
                    minimum=0,
                    maximum=1,
                    value=0.8,
                    step=0.05,
                    info="Higher values make output more random"
                )
                top_k = gr.Slider(
                    label="🎲 Top K",
                    minimum=0,
                    maximum=100,
                    value=40,
                    step=1,
                    info="Number of tokens to consider for generation"
                )
                top_p = gr.Slider(
                    label="📊 Top P",
                    minimum=0,
                    maximum=1,
                    value=0.9,
                    step=0.05,
                    info="Cumulative probability threshold for token generation"
                )
            with gr.Row():
                format = gr.Radio(
                    label="📝 Format",
                    choices=["text", "json"],
                    value="text",
                    info="Output format"
                )
                debug = gr.Checkbox(
                    label="🐛 Debug Mode",
                    value=False,
                    info="Show detailed request/response information"
                )

        generate_btn = gr.Button("🚀 Generate", variant="primary")
        output = gr.Textbox(label="📝 Output", lines=10)

        # Set up event handler
        generate_btn.click(
            fn=generate_text,
            inputs=[
                user_prompt,
                system_prompt,
                model,
                temperature,
                top_k,
                top_p,
                url,
                format,
                debug
            ],
            outputs=output
        )

    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch()
