# Главная страница

from playwright.sync_api import expect
from pages.public.base_public_page import BasePublicPage
import config.settings as cfg


class HomePage(BasePublicPage):
    def __init__(self, page):
        super().__init__(page, cfg.PUBLIC_PAGES["home"])

    def assert_player_present(self):
        """
        Проверяет, что плеер прямого эфира присутствует на странице.
        Не проверяем воспроизведение — только наличие элемента.
        """
        player = self.page.locator(
            '[data-role="player"], .LivePlayerMainBlock_player__LgE_f, iframe[src*="eump"]'
        ).first
        expect(player).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_news_block_present(self):
        """Проверяет, что блок новостей есть на странице"""
        news_heading = self.page.get_by_role("heading", name="ВЫПУСКИ НОВОСТЕЙ")
        expect(news_heading).to_be_visible(timeout=cfg.TIMEOUT)

        # Проверяем, что есть хотя бы одна новость
        news_items = self.page.locator('a[href*="/news/"]').all()
        assert len([el for el in news_items if el.is_visible()]) >= 1, "Нет видимых новостей"

    def assert_watching_block_present(self):
        """Проверяет блок «СЕЙЧАС СМОТРЯТ»"""
        watching_heading = self.page.get_by_role("heading", name="СЕЙЧАС СМОТРЯТ")
        expect(watching_heading).to_be_visible(timeout=cfg.TIMEOUT)

        # Проверяем, что есть карточки видео
        video_cards = self.page.locator('.CollectionElem_elem__Mtt_Q, a[href*="/movies/"], a[href*="/shows/"]').all()
        assert len([el for el in video_cards if el.is_visible()]) >= 1, "Нет карточек в блоке «Сейчас смотрят»"

    def assert_navigation_links_valid(self):
        """Проверяет, что ключевые ссылки навигации имеют корректные href"""
        nav_checks = [
            ("ЭФИР", "/live"),
            ("НОВОСТИ", "/news/issue"),
            ("ШОУ", "/shows"),
            ("ТЕЛЕПРОГРАММА", "/schedule"),
        ]

        for link_text, expected_href in nav_checks:
            link = self.page.get_by_role("link", name=link_text).first
            expect(link).to_be_visible(timeout=cfg.TIMEOUT)
            href = link.get_attribute("href")
            assert expected_href in href, f"Ссылка '{link_text}' ведёт на {href}, ожидалось *{expected_href}*"

