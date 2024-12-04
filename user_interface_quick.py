import gradio as gr
from langchain_example1 import chain


def chat(question , history):
    if question == '' :
        return "Please ask a question"
    else:
        return chain.invoke({"question": question})

gr.ChatInterface(
    fn=chat, 
    type="messages"
).launch()