# First: pip install python-dotenv
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Access the variables
api_key = os.getenv('API_KEY')
database_url = os.getenv('DATABASE_URL')

print(f"API Key: {api_key}")
print(f"DB URL: {database_url}")

# Create a .env file with:
# API_KEY=your_secret_key_here
# DATABASE_URL=your_database_url_here
