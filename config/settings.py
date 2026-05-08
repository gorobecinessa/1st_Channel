# URL, таймауты, переменные окружения

import os
from dotenv import load_dotenv

load_dotenv()

# Окружение: stage или prod
ENVIRONMENT = os.getenv("ENVIRONMENT", "stage")

# Базовые URL
URLS = {
    "stage": "https://stage.1tv.ru",
    "prod": "https://www.1tv.ru"
}

BASE_URL = os.getenv("BASE_URL", URLS.get(ENVIRONMENT, URLS["stage"]))

# Публичные страницы (относительные пути)
PUBLIC_PAGES = {
    "home": "/",
    "live": "/live",
    "news_issue": "/news/issue",
    "shows": "/shows",
    "podcasts": "/podcasts",
    "movies": "/movies",
    "sport": "/sport/sport-translyacii-i-sobytiya",
    "schedule": "/schedule",
    "profile": "/profile"
}

# Страницы личного кабинета
PROFILE_PAGES = {
    "favorites": "/profile/videos/favorites",
    "later": "/profile/videos/later",
    "history": "/profile/videos/history",
    "subscriptions": "/profile/subscriptions",
    "interactive": "/profile/interactive",
    "pin": "/profile/pin"
}

# Таймауты (в миллисекундах)
TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "10000"))
PAGE_LOAD_TIMEOUT = int(os.getenv("PAGE_LOAD_TIMEOUT", "30000"))

# Авторизация
AUTH_PROVIDERS = ["phone", "yandex", "vk", "ok"]
AUTH_STATE_PATH = os.getenv("AUTH_STATE_PATH", "auth_state.json")
