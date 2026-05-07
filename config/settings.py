# URL, таймауты, переменные окружения

import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://stage.1tv.ru")
AUTH_STATE_PATH = os.getenv("AUTH_STATE_PATH", "auth_state.json")
TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))


