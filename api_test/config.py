import os
from dotenv import load_dotenv

load_dotenv()

def get_api_key(name:str) -> str:
    """Retrieve an API key for a given service from environment variables."""    
    return os.getenv(name,'')