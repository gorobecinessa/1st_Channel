import pytest
from playwright.sync_api import Page
from pages.public.shows_page import ShowsPage


@pytest.mark.smoke
class TestShowsPageSmoke:

    def test_shows_page_loads_and_elements_visible(self, page: Page):
        """
        Страница /shows открывается
        Заголовок 'ШОУ ПЕРВОГО КАНАЛА' виден
        Главный слайдер с премьерой присутствует
        Секции 'Премьеры сезона', 'Сейчас смотрят', 'Яркие моменты' видны
        """
        shows = ShowsPage(page)
        shows.open()  # Открывает /shows

        # Проверка загрузки страницы
        shows.assert_page_loaded()

        # Проверка главного слайдера
        shows.assert_main_slider_present()

        # Проверка секций
        shows.assert_sections_present()

