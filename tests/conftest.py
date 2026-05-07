# Фикстуры: браузер, авторизация, base_url

import os
import sys

# 🔧 FIX: Добавляем корень проекта в PYTHONPATH
# Это позволяет импортировать config, pages, locators из корня проекта
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
import config.settings as cfg
from playwright.sync_api import Page

# ЭТОТ БЛОК ВЫВОДИТ ИНФОРМАЦИЮ ОБ ОКРУЖЕНИИ ПРИ ЗАПУСКЕ
def pytest_configure(config):
    env = cfg.ENVIRONMENT.upper()
    url = cfg.BASE_URL
    print(f"\n{'='*50}")
    print(f" ЗАПУСК ТЕСТОВ")
    print(f"Окружение: {env}")
    print(f"URL: {url}")
    print(f"{'='*50}\n")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Автоматически подключает auth_state.json, если файл существует"""
    if os.path.exists(cfg.AUTH_STATE_PATH):
        return {**browser_context_args, "storage_state": cfg.AUTH_STATE_PATH}
    return browser_context_args

@pytest.fixture
def page(page: Page):
    """Устанавливает глобальный таймаут и возвращает готовую страницу"""
    page.set_default_timeout(cfg.TIMEOUT)
    yield page
