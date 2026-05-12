from playwright.sync_api import expect, Page
from pages.public.base_public_page import BasePublicPage
from locators.public.movies_page import MoviesPageLocators
import config.settings as cfg


class MoviesPage(BasePublicPage):
    def __init__(self, page: Page):
        super().__init__(page, cfg.PUBLIC_PAGES["movies"])

    def assert_page_loaded(self):
        """Проверяет загрузку страницы"""
        expect(self.page.locator(MoviesPageLocators.PAGE_HEADING)).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_main_slider_present(self):
        """Проверяет наличие главного слайдера"""
        expect(self.page.locator(MoviesPageLocators.MAIN_SLIDER).first).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_sections_present(self):
        """Проверяет наличие основных секций"""
        expect(self.page.locator(MoviesPageLocators.SECTION_ALL).first).to_be_visible(timeout=cfg.TIMEOUT)
        expect(self.page.locator(MoviesPageLocators.SECTION_ALL_MOVIES)).to_be_visible(timeout=cfg.TIMEOUT)

