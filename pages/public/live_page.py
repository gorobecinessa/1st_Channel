from playwright.sync_api import expect, Page
from pages.public.base_public_page import BasePublicPage
from locators.public.live_page import LivePageLocators
import config.settings as cfg
import re


class LivePage(BasePublicPage):
    def __init__(self, page: Page):
        super().__init__(page, cfg.PUBLIC_PAGES["live"])

    def assert_live_indicator_visible(self):
        """Проверяет красный индикатор "ЭФИР" в шапке"""
        expect(self.page.locator(LivePageLocators.LIVE_HEADER_INDICATOR)).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_broadcast_button_active(self):
        """Проверяет, что кнопка "Телеэфир" активна"""
        broadcast_button = self.page.locator(LivePageLocators.CHANNEL_BROADCAST_BUTTON)
        expect(broadcast_button).to_be_visible(timeout=cfg.TIMEOUT)
        expect(broadcast_button).to_have_class(re.compile(r"Broadcasts_active"), timeout=cfg.TIMEOUT)

    def assert_current_program_visible(self):
        """Проверяет, что текущая программа отображается в расписании"""
        current_program = self.page.locator(LivePageLocators.CURRENT_PROGRAM).first
        expect(current_program).to_be_visible(timeout=cfg.TIMEOUT)

        # Проверяем, что есть время и название (по классам с частичным совпадением)
        expect(current_program.locator(LivePageLocators.CURRENT_PROGRAM_TIME).first).to_be_visible(timeout=cfg.TIMEOUT)
        expect(current_program.locator(LivePageLocators.CURRENT_PROGRAM_TITLE).first).to_be_visible(timeout=cfg.TIMEOUT)

    def get_current_program_info(self) -> dict:
        """Возвращает информацию о текущей программе"""
        current_program = self.page.locator(LivePageLocators.CURRENT_PROGRAM).first

        time_el = current_program.locator(LivePageLocators.CURRENT_PROGRAM_TIME).first
        title_el = current_program.locator(LivePageLocators.CURRENT_PROGRAM_TITLE).first

        return {
            "time": time_el.text_content().strip() if time_el.is_visible() else "",
            "title": title_el.text_content().strip() if title_el.is_visible() else ""
        }

    def assert_schedule_loaded(self, min_items: int = 3):
        """Проверяет, что расписание загружено с элементами"""
        items = self.page.locator(LivePageLocators.SCHEDULE_ITEM).all()
        visible_count = len([el for el in items if el.is_visible()])
        assert visible_count >= min_items, f"В расписании мало элементов: {visible_count}"


