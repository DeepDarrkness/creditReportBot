import streamlit as st
from openai import AsyncAzureOpenAI
from mistralai import Mistral
import os
import time
import asyncio
import fitz  # PyMuPDF
import base64
from io import BytesIO
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

@st.cache_resource
def init_mistral_client():
    try:
        client = Mistral(Settings.MISTRAL_API_KEY)
        return client
    except Exception as e:
        st.error(f"Failed to initialize Mistral client: {e}")
        st.stop()
try:
    mistral_client = init_mistral_client()
    st.toast("Connected to OCR Model successfully", icon="✅")
except Exception as e:
    st.error(f"Failed to initialize Mistral client: {e}")
    st.stop()


#Streaming reponse
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
                    message_placeholder.markdown(full_response + "▌")
            
        message_placeholder.markdown(full_response)
        return full_response
    
    except Exception as e:
        st.error(f"Error during streaming: {e}")
        return "Sorry, I encountered an error while generating a response."
    
# PDF upload button
uploaded_file = st.sidebar.file_uploader(
    "Upload a PDF to query", 
    type=["pdf"],
    help="Upload a PDF document to extract text and query its contents"
)

if uploaded_file is not None:
    with st.sidebar:
        with st.status("Processing PDF...", expanded=True) as status:
            st.write("Uploading file...")
            pdf_bytes = uploaded_file.read()
            pdf_stream = BytesIO(pdf_bytes)
            doc = fitz.open(stream=pdf_stream, filetype="pdf")
            num_pages = doc.page_count
            st.write(f"PDF loaded into memory. Number of pages: {num_pages}")
            base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')

            st.write("Sending OCR request to Mistral...")
            ocr_response = mistral_client.ocr.process(
                model="mistral-ocr-latest",
                document={
                    "type": "document_url",
                    "document_url": f"data:application/pdf;base64,{base64_pdf}" 
                },
                include_image_base64=True
            )
            if not hasattr(ocr_response, "pages") or not ocr_response.pages:
                st.write("No pages found in the OCR reponse.")
            st.write("OCR complete!")
            combined_markdown = ""
            for i, page in enumerate(ocr_response.pages):
                markdown = getattr(page, "markdown", "").strip()
                combined_markdown += markdown
                if i < len(ocr_response.pages) - 1:
                    combined_markdown += "\n\n---\n\n"
            st.write(f"Markdown of lenght: {len(combined_markdown)}")
            st.session_state.credit_report = combined_markdown
            st.success("Markdown ready for querying!")
            status.update(label="PDF ready for querying!", state="complete", expanded=False)

    

#Chat
if "messages" not in st.session_state:
    st.session_state.messages = []
if "system_prompt" not in st.session_state:
    st.session_state.system_prompt = {
    "role": "system", 
    "content": """You are a financial assistant. Guide the user to upload a credit report. Analyze the credit report and provide insights.
                Do not help the user with anything else. Do not output code. And bring the conversation back to credit analysis if user
                goes on in a different transcript."""
}
if "credit_report" not in st.session_state:
    st.session_state.credit_report = ""

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask any question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    messages = []
    messages.append(st.session_state.system_prompt)    #system prompt
    messages.extend(st.session_state.messages[-10:])   #last 10 conversation messages
    if "credit_report" in st.session_state:            #credit report truncated to 4000 chars
        messages.append({                              
            "role": "system",
            "content": f"Credit report markdown:\n\n{st.session_state.credit_report[:16000]}"     #16000 char is roughly 4000 tokens
        })
    with st.chat_message("assistant"):
        full_response = asyncio.run(get_streaming_response(messages))
    st.session_state.messages.append({"role": "assistant", "content": full_response})

if st.sidebar.button("Clear Chat"):
    st.session_state.messages = []
    st.session_state.credit_report = ""
    st.rerun()

if st.sidebar.button("Download Markdown"):
    with open("credit_report.md", "w") as f:
        f.write(st.session_state.credit_report)
    st.download_button(
        "Download Markdown",
        data=st.session_state.credit_report,
        file_name="./md/credit_report.md",
        mime="text/markdown"
    )
    st.rerun()


# helper_prompt = """
# The Narration column describes the transaction details: party name, instrument number, transaction type, and processing codes.
#     NEFT/RTGS: Often includes remitter name, account number (sometimes masked), and a reference number.
#     IMPS: Similar to NEFT, but usually more concise.
#     UPI: Often includes the VPA (Virtual Payment Address) and a transaction ID.
#     Cheque: Cheque number, drawer/drawee details.
#     ATM Withdrawal/POS: Merchant name, location, and a transaction ID.
#     Internal Transfers: Account numbers, names, purpose.
#     Loan EMIs/Interest: Specific codes for loan type, EMI number, interest charged.
#     Some example Narrations:
#     "SALARY CREDIT FROM {employer}",
#     "ACH CREDIT-SALARY-{employer}",
#     "NEFT-{employer} PAYROLL",
#     "CREDIT-SALARY-{employer} PVT LTD",
#     "{employer} LTD SAL JUL 2025",
#     "{employer} PAYROLL CREDIT",
#     "INWARD REMITTANCE SALARY {employer}",
# """