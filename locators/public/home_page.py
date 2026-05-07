class HomePageLocators:

    # Семантические обёртки
    HEADER = "header"
    MAIN = "main"

    # Навигация (используем get_by_role("link", name=...) в Page Object)
    NAV_LIVE = "ЭФИР"
    NAV_NEWS = "НОВОСТИ"
    NAV_SHOWS = "ШОУ"
    NAV_SCHEDULE = "ТЕЛЕПРОГРАММА"

    # Заголовки контент-блоков (get_by_role("heading", name=...))
    SECTION_NEWS = "ВЫПУСКИ НОВОСТЕЙ"
    SECTION_WATCHING = "СЕЙЧАС СМОТРЯТ"

    # Фолбэк по href (если текст изменится при локализации)
    LIVE_HREF = "/live"
    NEWS_HREF = "/news/issue"
    SCHEDULE_HREF = "/schedule"

