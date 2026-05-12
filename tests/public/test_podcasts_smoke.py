import pytest
from playwright.sync_api import Page
from pages.public.podcasts_page import PodcastsPage


@pytest.mark.smoke
class TestPodcastsPageSmoke:

    def test_podcasts_page_loads_and_elements_visible(self, page: Page):
        """
        Страница /podcasts открывается
        Заголовок страницы виден
        Главный слайдер присутствует
        Секции 'Сейчас смотрят', 'Все подкасты' видны
        """
        podcasts = PodcastsPage(page)
        podcasts.open()  # Открывает /podcasts

        # Проверка загрузки страницы
        podcasts.assert_page_loaded()

        # Проверка главного слайдера
        podcasts.assert_main_slider_present()

        # Проверка секций
        podcasts.assert_sections_present()

