import pytest
from playwright.sync_api import Page
from pages.public.news_page import NewsPage


@pytest.mark.smoke
class TestNewsPageSmoke:

    def test_news_page_loads_and_elements_visible(self, page: Page):
        """
        Страница /news/issue открывается
        Заголовок страницы виден
        Кнопка 'Смотреть выпуск' присутствует
        Табы переключения ('Выпуски новостей', 'Все новости') видны
        Рубрики в блоке 'Главное' присутствуют
        Карточки новостей отображаются
        """
        news = NewsPage(page)
        news.open()  # Открывает /news/issue

        # Проверка загрузки страницы
        news.assert_page_loaded()

        # Проверка кнопки "Смотреть выпуск"
        news.assert_watch_button_present()

        # Проверка табов
        news.assert_tabs_present()

        # Проверка рубрик
        news.assert_topics_present()

        # Проверка карточек новостей
        news.assert_news_cards_present(min_count=1)

        # Дополнительная проверка: получаем данные первой новости
        title = news.get_first_news_title()
        date = news.get_first_news_date()

        assert len(title) > 0, "Заголовок первой новости пустой"
        assert len(date) > 0, "Дата первой новости пустая"

        print(f"Первая новость: {title} ({date})")
