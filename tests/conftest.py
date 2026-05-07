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
