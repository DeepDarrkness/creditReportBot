import os
from openai import AsyncAzureOpenAI 
from pydantic import BaseModel, RootModel
import json
from typing import Annotated, List, Dict, Literal, Optional
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

try:
    openai_client = init_openai_client()
    print("Connected to Chat Model successfully")
except Exception as e:
    print(f"Failed to initialize OpenAI client")

