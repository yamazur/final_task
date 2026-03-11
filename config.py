import os
from dotenv import load_dotenv

load_dotenv()

DEFAULT_TIMEOUT = 5
SQL_LOGIN = os.getenv("SQL_LOGIN")
SQL_PASSWORD = os.getenv("SQL_PASSWORD")