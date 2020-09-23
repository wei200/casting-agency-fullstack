import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.environ.get("DATABSE_URL")
SECRET_KEY = os.environ.get("SECRECT_KEY")

