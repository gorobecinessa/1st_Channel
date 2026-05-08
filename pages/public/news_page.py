from playwright.sync_api import expect, Page
from pages.public.base_public_page import BasePublicPage
from locators.public.news_page import NewsPageLocators
import config.settings as cfg


class NewsPage(BasePublicPage):
    def __init__(self, page: Page):
        super().__init__(page, cfg.PUBLIC_PAGES["news_issue"])

    def assert_page_loaded(self):
        """Проверяет, что страница новостей загрузилась"""
        expect(self.page.locator(NewsPageLocators.PAGE_HEADING)).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_watch_button_present(self):
        """Проверяет наличие кнопки 'Смотреть выпуск'"""
        expect(self.page.locator(NewsPageLocators.WATCH_LATEST_BUTTON)).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_tabs_present(self):
        """Проверяет наличие табов переключения"""
        # Активный таб "Выпуски новостей"
        expect(self.page.locator(NewsPageLocators.TAB_NEWS_RELEASES)).to_be_visible(timeout=cfg.TIMEOUT)
        # Таб "Все новости"
        expect(self.page.locator(NewsPageLocators.TAB_ALL_NEWS)).to_be_visible(timeout=cfg.TIMEOUT)

    def assert_topics_present(self):
        """Проверяет наличие рубрик в блоке 'Главное'"""
        topics = self.page.locator(NewsPageLocators.MAIN_TOPIC_LINK).all()
        assert len([el for el in topics if el.is_visible()]) >= 1, "Нет видимых рубрик в блоке 'Главное'"

    def assert_news_cards_present(self, min_count: int = 1):
        """Проверяет наличие карточек новостей"""
        cards = self.page.locator(NewsPageLocators.NEWS_CARD).all()
        visible_cards = [el for el in cards if el.is_visible()]
        assert len(visible_cards) >= min_count, f"Карточек новостей меньше {min_count}: {len(visible_cards)}"

    def get_first_news_title(self) -> str:
        """Возвращает заголовок первой новости"""
        title = self.page.locator(NewsPageLocators.NEWS_CARD_TITLE).first
        expect(title).to_be_visible(timeout=cfg.TIMEOUT)
        return title.text_content().strip()

    def get_first_news_date(self) -> str:
        """Возвращает дату первой новости"""
        date = self.page.locator(NewsPageLocators.NEWS_CARD_DATE).first
        expect(date).to_be_visible(timeout=cfg.TIMEOUT)
        return date.text_content().strip()
