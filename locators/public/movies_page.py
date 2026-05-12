class MoviesPageLocators:

    # Заголовок страницы
    PAGE_HEADING = 'h1:has-text("Фильмы и сериалы Первого канала")'
    MAIN_SLIDER = "[class*='ImageWithLoader_inner'] img"

    # Секции
    SECTION_ALL = "h2[class*='Heading_title']"
    SECTION_ALL_MOVIES = 'a:has-text("Все фильмы и сериалы")'

    # Футер
    FOOTER_TEXT = '.Footer_text, p:has-text("Первый канал")'


