class NewsPageLocators:

    # Заголовок страницы
    PAGE_HEADING = "h1"  # "НОВОСТИ ПЕРВОГО КАНАЛА"

    # Кнопка "Смотреть выпуск" в главном выпуске
    # WATCH_LATEST_BUTTON = 'button[aria-label*="Смотреть"][aria-label*="Выпуск новостей"]'
    WATCH_LATEST_BUTTON = 'button:has(span:has-text("смотреть выпуск"))'
    # Табы переключения
    TAB_NEWS_RELEASES = 'li[class*="Tabs_tab"][class*="Tabs_selected"]'  # "Выпуски новостей" (активный)
    TAB_ALL_NEWS = 'li[class*="Tabs_tab"]:has-text("Все новости")'

    # Рубрики в блоке "Главное"
    MAIN_TOPIC_LINK = 'a[class*="NewsTopics_topic"]'

    # Рубрики в блоке "Рубрики"
    RUBRIC_LINK = 'a[class*="NewsRubrics_rubric"]'

    # Карточки новостей
    NEWS_CARD = 'article[class*="NewsCard_card"]'
    NEWS_CARD_TITLE = 'p[class*="NewsCard_title"]'
    NEWS_CARD_DESCRIPTION = 'p[class*="NewsCard_description"]'
    NEWS_CARD_DATE = 'span[class*="NewsCard_date"]'
    NEWS_CARD_LINK = 'a[class*="NewsCard_content"]'

    # Слайдер с каруселью новостей
    NEWS_CAROUSEL = '[class*="swiper-slide"]'