from playwright.sync_api import expect, Page
from pages.public.base_public_page import BasePublicPage
from locators.public.shows_page import ShowsPageLocators
import config.settings as cfg


class ShowsPage(BasePublicPage):
    def __init__(self, page: Page):
        super().__init__(page, cfg.PUBLIC_PAGES["shows"])

    def assert_page_loaded(self):
        """Проверяет, что страница шоу загрузилась"""
        expect(self.page.locator(ShowsPageLocators.PAGE_HEADING)).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_main_slider_present(self):
        """Проверяет наличие главного слайдера с премьерой"""
        expect(self.page.locator(ShowsPageLocators.MAIN_SLIDER)).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_sections_present(self):
        """Проверяет наличие основных секций"""
        # Секция "Премьеры сезона"
        expect(self.page.locator(ShowsPageLocators.SECTION_PREMIERES)).to_be_visible(timeout=cfg.TIMEOUT)

        # Секция "Сейчас смотрят"
        expect(self.page.locator(ShowsPageLocators.SECTION_WATCHING_NOW)).to_be_visible(timeout=cfg.TIMEOUT)

        # Секция "Яркие моменты"
        expect(self.page.locator(ShowsPageLocators.SECTION_HIGHLIGHTS)).to_be_visible(timeout=cfg.TIMEOUT)



