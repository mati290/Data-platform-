from dotenv import load_dotenv
import os 

load_dotenv()

class Settings :
    APP_NAME: str = os.getenv("APP_NAME", "Data Platform")
    ENV: str = os.getenv("ENV", "dev")
    
settings = Settings()