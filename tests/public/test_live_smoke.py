import pytest
from playwright.sync_api import Page
from pages.public.live_page import LivePage


@pytest.mark.smoke
class TestLivePageSmoke:

    def test_live_page_loads_and_elements_visible(self, page: Page):
        """
        Страница /live открывается
        Красный индикатор "ЭФИР" виден в шапке
        Кнопка "Телеэфир" активна
        Текущая программа отображается в расписании
        Расписание загружено
        """
        live = LivePage(page)
        live.open()  # Открывает /live

        # Проверка индикатора "ЭФИР" в шапке
        live.assert_live_indicator_visible()

        # Проверка активной кнопки "Телеэфир"
        live.assert_broadcast_button_active()

        # Проверка текущей программы
        live.assert_current_program_visible()

        # Получаем информацию о текущей программе
        program_info = live.get_current_program_info()
        assert program_info["time"], "Время текущей программы пустое"
        assert program_info["title"], "Название текущей программы пустое"
        print(f"Сейчас в эфире: {program_info['time']} - {program_info['title']}")

        # Проверка расписания
        live.assert_schedule_loaded()

