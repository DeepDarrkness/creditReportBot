import logging
import os
from datetime import datetime, date
from typing import Annotated, List, Dict, Literal, Optional
from fastapi import FastAPI, UploadFile, File, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, RootModel
import aiofiles 
from data.datastring import json_string
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_CONTENT_TYPES = ["application/pdf"]
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class PDFProcessingResult(BaseModel):
    filename: str
    page_count: int
    text_length: int
    metadata: dict
    processing_time_ms: float

class ErrorResponse(BaseModel):
    detail: str

class Transaction(BaseModel):
    transaction_date: str # DD-MM-YYYY string for now
    amount: Optional[float] = None   # INR is float for now
    narration: str
    month_bucket: Literal["1-7", "8-14", "15-21", "22-EOM"]
    balance: Optional[float] = None

class CreditCategory(BaseModel):
    salary_credit: List[Transaction]
    loan_amount_credit: List[Transaction] = []
    internal_transfer: List[Transaction] = []
    upi_received: List[Transaction] = []

class MonthlyData(BaseModel):
    credits: CreditCategory

MonthName = Literal[
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
class FinancialData(RootModel):
    root: Dict[MonthName, MonthlyData]   #Dynamic MonthName

async def save_upload_file(upload_file: UploadFile) -> str:
    """Save uploaded file to disk and return file path"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(UPLOAD_DIR, f"{timestamp}_{upload_file.filename}")
    
    async with aiofiles.open(file_path, "wb") as out_file:
        while content := await upload_file.read(1024):  # Read in chunks
            await out_file.write(content)
    
    return file_path

# def process_pdf(file_path: str) -> dict:
#     """Process PDF file and return extracted information"""
#     start_time = datetime.now()
#     result = {
#         "page_count": 0,
#         "text": "",
#         "metadata": {},
#         "text_length": 0
#     }
    
#     try:
#         with pdfplumber.open(file_path) as pdf:
#             result["page_count"] = len(pdf.pages)
#             result["metadata"] = pdf.metadata
            
#             # Extract text from all pages
#             text_parts = []
#             for page in pdf.pages:
#                 text = page.extract_text()
#                 if text:
#                     text_parts.append(text)
            
#             result["text"] = "\n".join(text_parts)
#             result["text_length"] = len(result["text"])
            
#     except Exception as e:
#         logger.error(f"Error processing PDF: {str(e)}")
#         raise HTTPException(
#             status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
#             detail=f"PDF processing failed: {str(e)}"
#         )
    
#     processing_time = (datetime.now() - start_time).total_seconds() * 1000
#     result["processing_time_ms"] = processing_time
    
#     return result


@app.get("/test", include_in_schema=False)
async def health_check():
    return {"status": "Running"}

@app.post("/bank-pdf", response_model=FinancialData)
async def process_pdf(file: Annotated[UploadFile, File(description="PDF file of Bank Statement")]):
    #Do nothing with PDF
    data = json.loads(json_string)
    financial_data = FinancialData.model_validate(data)  
    return financial_data

@app.post(
    "/process-pdf/",
    response_model=PDFProcessingResult,
    responses={
        400: {"model": ErrorResponse, "description": "Invalid input"},
        422: {"model": ErrorResponse, "description": "Processing error"},
        413: {"model": ErrorResponse, "description": "File too large"},
    }
)
async def process_pdf_endpoint(
    file: Annotated[UploadFile, File(description="PDF file to process")]
):
    if file.content_type not in ALLOWED_CONTENT_TYPES:
        logger.warning(f"Invalid content type: {file.content_type}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed"
        )
    
    file_size = 0
    for chunk in file.file:
        file_size += len(chunk)
        if file_size > MAX_FILE_SIZE:
            logger.warning(f"File too large: {file.filename}")
            raise HTTPException(
                status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
                detail=f"File size exceeds {MAX_FILE_SIZE/(1024*1024)}MB limit"
            )
    
    # Reset file pointer after size check
    await file.seek(0)
    
    try:
        logger.info(f"Processing file: {file.filename}")
        
        # Save the file temporarily
        file_path = await save_upload_file(file)
        
        # Process the PDF
        # processing_result = process_pdf(file_path)
        
        # # Prepare response
        # result = PDFProcessingResult(
        #     filename=file.filename,
        #     page_count=processing_result["page_count"],
        #     text_length=processing_result["text_length"],
        #     metadata=processing_result["metadata"],
        #     processing_time_ms=processing_result["processing_time_ms"]
        # )
        
        # logger.info(f"Successfully processed: {file.filename}")
        
        # # Clean up - remove the temporary file
        # try:
        #     os.remove(file_path)
        # except Exception as e:
        #     logger.error(f"Error deleting temporary file: {str(e)}")
        
        # return result
        
    except Exception as e:
        logger.error(f"Error processing file {file.filename}: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing the file"
        )

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_config=None,  
        access_log=True
    )