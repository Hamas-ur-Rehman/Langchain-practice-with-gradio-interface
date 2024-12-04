import gradio as gr
from langchain_example1 import chain


with gr.Blocks(title="Chat with GPT-4") as demo:
    with gr.Column():
        chatbox = gr.Chatbot(type="messages")
        textbox = gr.Textbox()
        submit_button = gr.Button(value="Submit")

    def chat(question , history):
        history.append({"role": "user", "content": question})
        if question == '' :
            response =  "Please ask a question"
            history.append({"role": "assistant" , "content": response})
        else:
            # response = chain.invoke({"question": question})
            response = chain.stream({"question": question})

            # response = chain.invoke(question)
            history.append({"role": "assistant" , "content": ''})
        
        for i in response:
            history[-1]['content'] += i
            yield "", history

    
    textbox.submit(chat, inputs=[textbox, chatbox], outputs=[textbox,chatbox])
    submit_button.click(chat, inputs=[textbox, chatbox], outputs=[textbox,chatbox])



demo.launch()