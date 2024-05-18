import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

header = {
    "Content-Type":"application/json"
}

history = []

def generate_response(prompt):
    history.append(prompt)

    final_prompt = "\n".join(history)

    data = {
        "model":"llama3",
        "prompt":final_prompt,
        "stream":False
    }


    response = requests.post(url, headers=header, data=json.dumps(data))
    print(response)
    if response.status_code==200:
        response = response.text
        data = json.loads(response)
        actual_response = data["response"]
        return actual_response
    else:
        print("Error: ", response.text)

interface = gr.Interface(
    fn = generate_response,
    inputs = gr.Textbox(lines=2, placeholder='Enter your prompt'),
    outputs = "text"
)

interface.launch(share=TrueT)
