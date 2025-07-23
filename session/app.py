import os
import streamlit as st
from openai import AsyncAzureOpenAI
import asyncio
from default import defaultdata
from dotenv import load_dotenv
load_dotenv()
st.set_page_config(page_title="Credit Report Bot", page_icon="📊")
st.title("Credit Report Bot")

class Settings:
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_VERSION: str = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")
    AZURE_OPENAI_DEPLOYMENT_ID: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_ID", "gpt-4o")
    MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

@st.cache_resource
def init_openai_client():
    try:
        client = AsyncAzureOpenAI(
            azure_endpoint=Settings.AZURE_OPENAI_ENDPOINT,
            api_version=Settings.AZURE_OPENAI_API_VERSION,
            api_key=Settings.AZURE_OPENAI_API_KEY,
        )
        return client
    except Exception as e:
        st.error(f"Failed to initialize OpenAI client: {e}")
        st.stop()

try:
    openai_client = init_openai_client()
    #non-blocking toast notification
    st.toast("Connected to Chat Model successfully", icon="✅")
except Exception as e:
    st.error(f"Failed to initialize OpenAI client: {e}")
    st.stop()

async def get_streaming_response(messages):
    full_response = ""
    message_placeholder = st.empty()
    
    try:
        stream = await openai_client.chat.completions.create(
            model=Settings.AZURE_OPENAI_DEPLOYMENT_ID,
            messages=messages,
            stream=True
        )
        
        async for chunk in stream:
            if chunk.choices and len(chunk.choices) > 0:
                delta = chunk.choices[0].delta
                if delta and delta.content:
                    full_response += delta.content
                    message_placeholder.markdown(full_response + "▌", unsafe_allow_html=True)
            
        message_placeholder.markdown(full_response, unsafe_allow_html=True)
        return full_response
    
    except Exception as e:
        st.error(f"Error during streaming: {e}")
        return "Sorry, I encountered an error while generating a response."
    
if "messages" not in st.session_state:
    st.session_state.messages = []
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = {
    "role": "system", 
    "content": """You are a financial assistant. The user has provided credit report, bank statement, and pay slip data. 
               Analyze these documents and provide insights. Focus on:
               - Credit score analysis
               - Debt-to-income ratio
               - FOIR calculation
               - Payment history
               - Credit utilization 
               Never calculate obligation from payslip. Only use payslip data for verifying salary data.
                Do not output code. Only ouput markdown. You can inline LaTeX formula use a single $ before and after the equation 
                and use a double $ to display equationsKeep the conversation focused on credit analysis."""
    }
if "credit_report" not in st.session_state:
    st.session_state.credit_report = defaultdata.credit_report
if "bank_statement" not in st.session_state:
    st.session_state.bank_statement = defaultdata.bank_statement
if "pay_slip" not in st.session_state:
    st.session_state.pay_slip = defaultdata.pay_slip

if prompt := st.chat_input("Ask any question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    messages = []
    messages.append(st.session_state.system_prompt)    #system prompt
    messages.extend(st.session_state.messages[-10:])   
    if "credit_report" in st.session_state:            
        messages.append({                              
            "role": "user",
            "content": f"Credit report:\n\n{st.session_state.credit_report[:16000]}"     #16000 char is roughly 4000 tokens
        })
    if "bank_statement" in st.session_state:            
        messages.append({                              
            "role": "user",
            "content": f"Bank statement:\n\n{st.session_state.bank_statement[:16000]}"   
        })  
    if "pay_slip" in st.session_state:            
        messages.append({                              
            "role": "user",
            "content": f"Pay slip:\n\n{st.session_state.pay_slip[:16000]}"     
        })
    
    with st.chat_message("assistant"):
        full_response = asyncio.run(get_streaming_response(messages))
    st.session_state.messages.append({"role": "assistant", "content": full_response})

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state.credit_report = ""
    st.rerun()
