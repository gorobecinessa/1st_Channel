import pytest
from playwright.sync_api import Page, expect
from pages.public.home_page import HomePage


@pytest.mark.smoke
class TestHomePageSmoke:
    """Базовый смоук главной страницы 1tv.ru"""

    def test_home_loads_and_renders(self, page: Page):
        """
        Главная страница открывается
        Заголовок вкладки соответствует ожидаемому
        Хедер с навигацией загружен
        Плеер прямого эфира присутствует на странице
        Блоки контента (новости, «Сейчас смотрят») загружены
        Ключевые ссылки навигации имеют корректные href
        """
        home = HomePage(page)
        home.open()

        # Проверка базовой загрузки
        expect(page).to_have_title("Первый канал: Новости. Видео. Телепрограмма. Прямой эфир", timeout=10000)
        home.assert_header_loaded()

        # Проверка плеера (присутствие элемента, не обязательно воспроизведение)
        home.assert_player_present()

        # Проверка контент-блоков
        home.assert_news_block_present()
        home.assert_watching_block_present()

        # Проверка ключевых ссылок навигации
        home.assert_navigation_links_valid()

