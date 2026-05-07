# Базовый класс для публичных страниц

from playwright.sync_api import Page, expect
import config.settings as cfg


class BasePublicPage:
    """Базовый класс для всех публичных страниц"""

    def __init__(self, page: Page, relative_url: str):
        self.page = page
        self.relative_url = relative_url
        self.timeout = cfg.TIMEOUT

    def open(self):
        """Открывает страницу с полным URL и явным ожиданием"""
        # 🔧 FIX: Собираем полный URL из BASE_URL + относительного пути
        full_url = f"{cfg.BASE_URL}{self.relative_url}"
        self.page.goto(full_url, wait_until="domcontentloaded", timeout=cfg.PAGE_LOAD_TIMEOUT)
        # Ждём загрузки шапки (универсальный индикатор готовности страницы)
        expect(self.page.locator("header")).to_be_visible(timeout=self.timeout)

    def assert_header_loaded(self):
        """Проверяет, что хедер загрузился"""
        expect(self.page.locator("header")).to_be_visible(timeout=self.timeout)

    def assert_footer_loaded(self):
        """Проверяет, что футер загрузился"""
        expect(self.page.locator("footer")).to_be_visible(timeout=self.timeout)

    def assert_menu_links_present(self, min_count: int = 3):
        """Проверяет, что в меню есть ссылки"""
        # Используем get_by_role для устойчивости к изменениям вёрстки
        links = self.page.get_by_role("link")
        assert links.count() >= min_count, f"Меню пустое: найдено {links.count()} ссылок"

    def get_page_title_text(self) -> str:
        """Возвращает текст заголовка страницы (H1)"""
        h1 = self.page.locator("h1").first
        expect(h1).to_be_visible(timeout=self.timeout)
        return h1.text_content()


