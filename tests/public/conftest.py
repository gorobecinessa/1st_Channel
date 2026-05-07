
import pytest
from playwright.sync_api import Page

@pytest.fixture
def page(page: Page):
    """Переопределяем фикстуру для публичных тестов: без авторизации"""
    # Убеждаемся, что нет storage_state (публичная часть не требует входа)
    page.context.clear_cookies()
    page.set_default_timeout(10000)
    yield page

