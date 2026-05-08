from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from locators.air_positions import AirPositionsLocators


class AirPositionsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    def open_list(self):
        self.goto("/admin/air_positions")

    def open_new_form(self):
        self.click(AirPositionsLocators.NEW_BTN)

    def submit_and_handle_dialog(self):
        # Регистрируем обработчик ДО клика
        self.page.on("dialog", lambda dialog: dialog.accept())
        self.click(AirPositionsLocators.SAVE_BTN)
        expect(self.page.locator(AirPositionsLocators.ERROR_BLOCK)).to_be_visible(timeout=self.timeout)

    def assert_validation_errors(self):
        expect(self.page.locator(AirPositionsLocators.TITLE_ERROR)).to_be_visible(timeout=self.timeout)
        expect(self.page.locator(AirPositionsLocators.ORBIT_ERROR)).to_be_visible(timeout=self.timeout)
        assert self.page.locator(AirPositionsLocators.FIELD_WITH_ERRORS).count() >= 1

