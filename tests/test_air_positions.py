import pytest
from pages.air_positions_page import AirPositionsPage
from playwright.sync_api import Page

@pytest.mark.usefixtures("page")
class TestAirPositions:
    """Тест-кейсы по модулю 'Эфирные позиции'"""

    def test_case_5050_empty_form_validation(self, page: Page):
        """
        #5050: Валидация пустой формы создания ЭП.
        ОР: Появляются ошибки валидации, сохранение не происходит.
        """
        air_page = AirPositionsPage(page)
        air_page.open_list()
        air_page.open_new_form()
        air_page.submit_and_handle_dialog()
        air_page.assert_validation_errors()



