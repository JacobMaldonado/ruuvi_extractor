import os
from dotenv import load_dotenv

load_dotenv()

DATA_DIRECTORY_PATH = os.getenv("DATA_DIRECTORY_PATH")
DATA_FILE_NAME = os.getenv("DATA_FILE_NAME")
