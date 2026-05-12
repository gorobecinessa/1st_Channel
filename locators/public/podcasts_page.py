class PodcastsPageLocators:
    # Заголовок страницы
    PAGE_HEADING = 'h1'  # "ПОДКАСТЫ ПЕРВОГО КАНАЛА" или аналогичный

    # Главный слайдер (премьера/рекомендации)
    MAIN_SLIDER = 'div[class*="ImageWithLoader_inner"] img[src*="promo_position"]'

    # Секции
    SECTION_WATCHING_NOW = 'h2:has-text("СЕЙЧАС СМОТРЯТ")'
    SECTION_CATEGORIES = 'h2:has-text("КАТЕГОРИИ")'

    # Кнопки и ссылки
    SECTION_ALL_PODCASTS = 'a:has-text("Все подкасты")'
    WATCH_BUTTON = 'text=Смотреть'
    ALL_PODCASTS_LINK = 'text=Все подкасты'
