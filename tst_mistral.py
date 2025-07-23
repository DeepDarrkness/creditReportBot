import base64
import os
from mistralai import Mistral
from dotenv import load_dotenv 

load_dotenv()

def encode_pdf(pdf_path):
    """Encode the pdf to base64."""
    try:
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {pdf_path} was not found.")
        return None
    except Exception as e:  
        print(f"Error: {e}")
        return None

pdf_path = "./credit_report/payslip.pdf"

base64_pdf = encode_pdf(pdf_path)

api_key = os.getenv("MISTRAL_API_KEY")
try:
    client = Mistral(api_key=api_key)
    print("Connected to Mistral successfully")
except Exception as e:
    print(f"Failed to connect to Mistral: {e}")

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": f"data:application/pdf;base64,{base64_pdf}" 
    },
    include_image_base64=True
)
if not hasattr(ocr_response, "pages") or not ocr_response.pages:
    print("No pages found in the OCR reponse.")
combined_markdown = ""
for i, page in enumerate(ocr_response.pages):
    markdown = getattr(page, "markdown", "").strip()
    combined_markdown += markdown
    if i < len(ocr_response.pages) - 1:
        combined_markdown += "\n\n---\n\n"
print(combined_markdown)