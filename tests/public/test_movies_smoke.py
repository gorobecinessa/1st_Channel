import pytest
from playwright.sync_api import Page
from pages.public.movies_page import MoviesPage


@pytest.mark.smoke
class TestMoviesPageSmoke:

    def test_movies_page_loads_and_elements_visible(self, page: Page):
        """
        Страница /movies открывается
        Заголовок страницы виден
        Главный слайдер присутствует
        Наличие секций
        """
        movies = MoviesPage(page)
        movies.open()

        # Проверка загрузки страницы
        movies.assert_page_loaded()

        # Проверка загрузки большого слайдера
        movies.assert_main_slider_present()

        # Проверяем наличие секций
        movies.assert_sections_present()





