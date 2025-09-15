import streamlit as st
from langchain_openai import ChatOpenAI

# Initialize the local LLM
local_llm = ChatOpenAI(
    model="ai/qwen2.5",  # model name
    api_key="nope",      # required param but ignored by Docker Model Runner
    base_url="http://model-runner.docker.internal/engines/llama.cpp/v1"
)

# UI heading
st.subheader("Talk to me 🤖")

# Chat input
prompt = st.chat_input("Type your message")

if prompt:
    # Display user message
    with st.chat_message("user"):
        st.write(prompt)

    # Call the model
    response = local_llm.invoke(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(response.content)

