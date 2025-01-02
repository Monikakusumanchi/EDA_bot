
from dotenv import load_dotenv
import os
# from .env import *  # relative import
load_dotenv(dotenv_path='/workspace/EDA_bot/.env')


# Access the OpenAI API key
print(os.getenv("OPENAI_API_KEY"))
