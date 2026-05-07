# Базовые методы (явные ожидания, клики, ввод)

from playwright.sync_api import Page, expect
import config.settings as cfg

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.timeout = cfg.TIMEOUT

    def goto(self, relative_url: str):
        self.page.goto(f"{cfg.BASE_URL}{relative_url}", wait_until="domcontentloaded", timeout=self.timeout)

    def click(self, locator: str):
        el = self.page.locator(locator).first
        expect(el).to_be_visible(timeout=self.timeout)
        expect(el).to_be_enabled(timeout=self.timeout)
        el.click()

    def fill(self, locator: str, value: str):
        el = self.page.locator(locator).first
        expect(el).to_be_visible(timeout=self.timeout)
        el.fill(value)

    def get_text(self, locator: str) -> str:
        el = self.page.locator(locator).first
        expect(el).to_be_visible(timeout=self.timeout)
        return el.text_content()


