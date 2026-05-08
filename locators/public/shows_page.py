class ShowsPageLocators:

    # Заголовок страницы
    PAGE_HEADING = 'h1'  # "ШОУ ПЕРВОГО КАНАЛА"

    # Главный слайдер (премьера сезона)
    MAIN_SLIDER = 'div[class*="ImageWithLoader_inner"] img[src*="show_big_slider"]'

    # Секции
    SECTION_PREMIERES = 'text=ПРЕМЬЕРЫ СЕЗОНА'
    SECTION_WATCHING_NOW = 'h2:has-text("СЕЙЧАС СМОТРЯТ")'
    SECTION_HIGHLIGHTS = 'h2:has-text("ЯРКИЕ МОМЕНТЫ")'


