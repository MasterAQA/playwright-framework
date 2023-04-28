import os

from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path('../.env')
load_dotenv(dotenv_path=dotenv_path)


base_page = "https://www.apple.com/"

apple_username = os.getenv("APPLE_USERNAME")
apple_password = os.getenv("APPLE_PASSWORD")
