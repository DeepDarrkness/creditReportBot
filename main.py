import streamlit as st
from openai import AsyncAzureOpenAI
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="Credit Report Bot", page_icon="📊")
st.title("Credit Report Bot")

class Settings:
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_VERSION: str = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")
    AZURE_OPENAI_DEPLOYMENT_ID: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_ID", "gpt-4o")

@st.cache_resource
def init_openai_client():
    try:
        client = AsyncAzureOpenAI(
            azure_endpoint=Settings.AZURE_OPENAI_ENDPOINT,
            api_version=Settings.AZURE_OPENAI_API_VERSION,
            api_key=Settings.AZURE_OPENAI_API_KEY,
        )
        st.success("Connected to Azure OpenAI successfully")
        return client
    except Exception as e:
        st.error(f"Failed to initialize OpenAI client: {e}")
        st.stop()

client = init_openai_client()

async def get_streaming_response(messages):
    full_response = ""
    message_placeholder = st.empty()
    
    try:
        stream = await client.chat.completions.create(
            model=Settings.AZURE_OPENAI_DEPLOYMENT_ID,
            messages=messages,
            stream=True
        )
        
        async for chunk in stream:
            if chunk.choices and len(chunk.choices) > 0:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    full_response += delta.content
                    message_placeholder.markdown(full_response + "▌")
            
        message_placeholder.markdown(full_response)
        return full_response
    
    except Exception as e:
        st.error(f"Error during streaming: {e}")
        return "Sorry, I encountered an error while generating a response."

# chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask any question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        messages = [{"role": m["role"], "content": m["content"]} for m in st.session_state.messages]
        full_response = asyncio.run(get_streaming_response(messages))
    st.session_state.messages.append({"role": "assistant", "content": full_response})

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.rerun()