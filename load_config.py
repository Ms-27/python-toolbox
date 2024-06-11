import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path("path/to/.env")
load_dotenv(dotenv_path=dotenv_path)

# if in same folder:
# load_dotenv()

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE")
STORAGE_BUCKET_NAME = os.getenv("STORAGE_BUCKET_NAME")
