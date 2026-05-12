from playwright.sync_api import expect, Page
from pages.public.base_public_page import BasePublicPage
from locators.public.podcasts_page import PodcastsPageLocators
import config.settings as cfg


class PodcastsPage(BasePublicPage):
    def __init__(self, page: Page):
        super().__init__(page, cfg.PUBLIC_PAGES["podcasts"])

    def assert_page_loaded(self):
        """Проверяет, что страница подкастов загрузилась"""
        expect(self.page.locator(PodcastsPageLocators.PAGE_HEADING)).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_main_slider_present(self):
        """Проверяет наличие главного слайдера"""
        expect(self.page.locator(PodcastsPageLocators.MAIN_SLIDER).first).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_sections_present(self):
        """Проверяет наличие основных секций"""
        # Секция "Сейчас смотрят"
        expect(self.page.locator(PodcastsPageLocators.SECTION_WATCHING_NOW)).to_be_visible(timeout=cfg.TIMEOUT)

        # Секция "Все подкасты"
        expect(self.page.locator(PodcastsPageLocators.SECTION_ALL_PODCASTS)).to_be_visible(timeout=cfg.TIMEOUT)

