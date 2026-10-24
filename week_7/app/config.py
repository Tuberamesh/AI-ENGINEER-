import os
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(PROJECT_ROOT / ".env")

APP_NAME = os.getenv("APP_NAME", "RAG Assistant API")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
