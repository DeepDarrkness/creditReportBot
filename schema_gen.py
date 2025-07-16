import os
import asyncio
import fitz
import base64
from PIL import Image
from io import BytesIO
from openai import AsyncAzureOpenAI, OpenAIError
from pydantic import BaseModel, RootModel, create_model
import json
from typing import Optional
import datetime
from data.datastring import md_string
from dotenv import load_dotenv
load_dotenv()
class Settings:
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_OPENAI_API_VERSION: str = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")
    AZURE_OPENAI_DEPLOYMENT_ID: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_ID", "gpt-4o")

def init_openai_client():
    try:
        client = AsyncAzureOpenAI(
            azure_endpoint=Settings.AZURE_OPENAI_ENDPOINT,
            api_version=Settings.AZURE_OPENAI_API_VERSION,
            api_key=Settings.AZURE_OPENAI_API_KEY,
        )
        return client
    except Exception as e:
        print(f"Failed to initialize OpenAI client: {e}")

async def perform_ocr(openai_client, img_url):
        try:
            messages = build_ocr_messages(img_url)
            print(f"Sending OCR request to OpenAI.")
            response = await openai_client.chat.completions.create(
                model=Settings.AZURE_OPENAI_DEPLOYMENT_ID,
                messages=messages,
                temperature=0.1,
                max_tokens=4096,            
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                response_format={"type": "json_object"}
            )
            return extract_text_from_response(response)
        except OpenAIError as e:
            if "rate limit" in str(e).lower():
                print("Rate limit exceeded.")
        
def build_ocr_messages(img_url):
    
    content = []
    content.append({"type": "image_url", "image_url": {"url": img_url}})

    messages = [
        {
            "role": "system",
            "content": """
                    You are an assitant that extracts the schema of the table in a bank statement (provided as image) and returns it 
                    as a json object. You are to only extract the column names and not the data. Disregard any text not related to the table.
                    If there are several tables, only extract the column names from the transaction table. Transaction table generally have 
                    name like "Statement" or "Statement of transaction" etc. Transaction table have column names like "Date", "Deposits", 
                    "Withdrawls", "Balance". Extract column names as is, and also infer the column types from the column names. "balance",
                    "deposit", "withdrawls", "credit" should have column type "float", the rest of columns names like "date", "narration", "mode" 
                    "certificate" etc should have column type "string". Ouput schema: {"column_name1": "type","column_name2": "type",} 
                    Only output RFC8259 compliant JSON.                 
            """
        },
        {
            "role": "user",
            "content": content,
        }
    ]
    return messages

def extract_text_from_response(response) -> str:
    if (
        not response.choices
        or not hasattr(response.choices[0].message, "content")
        or not response.choices[0].message.content
    ):
        print("No text extracted from OCR.")
    extracted_text = response.choices[0].message.content.strip()
    print(f"Extracted text length: {len(extracted_text)} characters.")
    return extracted_text

def sanitize_name(field_name: str) -> str:
    sanitized = ''.join(c if c.isalnum() else '_' for c in field_name)
    sanitized = sanitized.lstrip('0123456789_')
    if not sanitized:
        sanitized = 'field'
    return sanitized

def convert_type(type_str: str) -> type:
    type_map = {
        'str': str,
        'string': str,
        'text': str,
        'int': int,
        'integer': int,
        'float': float,
        'number': float,
        'decimal': float,
        'bool': bool,
        'boolean': bool
    }
    return type_map.get(type_str.lower().strip(), str)  # Default to string
    
def generate_model_from_json(json_spec: dict) -> type:
    fields = {
        sanitize_name(name): (Optional[convert_type(type_str)], None)
        for name, type_str in json_spec.items()
    }
    
    # Store original field mapping in model config
    original_fields = {
        sanitize_name(name): name 
        for name in json_spec.keys()
    }
    
    model = create_model(
        'GenTransactionsModel',
        __config__=type('Config', (), {
            'extra': 'ignore',
            'arbitrary_types_allowed': True,
            'original_fields': original_fields
        }),
        **fields
    )
    
    return model

json_spec = {
    "DATE": "string",
    "MODE": "string",
    "PARTICULARS": "string",
    "DEPOSITS": "float",
    "WITHDRAWALS": "float",
    "BALANCE": "float"
} 

sample_json  = {
    "DATE": "2023-01-15",
    "MODE": "Transfer",
    "PARTICULARS": "Salary",
    "DEPOSITS": "1500.50",  # String that should be converted to float
    "WITHDRAWALS": None,    # Missing value
    "BALANCE": 2000.75
}

# if __name__ == "__main__":
#     #load pdf
#     base64_image = None
#     try:
#         with open("./pdf/dinesh.pdf", "rb") as f:
#             pdf_bytes = f.read()
#             doc = fitz.open(stream=pdf_bytes, filetype="pdf")
#             num_pages = doc.page_count 
#             print(f"Loaded PDF with {num_pages} pages")

#             page = doc.load_page(0)  # First page
#             pix = page.get_pixmap(matrix=fitz.Identity)
#             img_bytes = pix.tobytes("png")
#             base64_image = base64.b64encode(img_bytes).decode("utf-8")
#         img_url = f"data:image/jpeg;base64,{base64_image}"
#     except Exception as e:
#         print(f"Failed to load PDF: {e}")
#     if base64_image:
#         try:
#             openai_client = init_openai_client()
#             print("Connected to Chat Model successfully")
#         except Exception as e:
#             print(f"Failed to initialize OpenAI client")

#         json_string = asyncio.run(perform_ocr(openai_client, img_url))
#         print(json_string)
#         schema = json.loads(json_string)

if __name__ == "__main__":
    try:
        TransactionsModel = generate_model_from_json(json_spec)
        print("Generated Pydantic model:")
        print(TransactionsModel.schema_json(indent=2))
        instance = TransactionsModel(**sample_json)
        print("\nModel instance:", instance)
        
    except Exception as e:
        print(f"Error generating model: {e}")