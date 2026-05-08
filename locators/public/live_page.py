class LivePageLocators:

    # Индикатор "ЭФИР" в шапке
    LIVE_HEADER_INDICATOR = '[class*="MenuButton_pageTitleLive"]'

    # Кнопки переключения каналов
    CHANNEL_BROADCAST_BUTTON = 'button[data-id="air"]'
    CHANNEL_MUZH_ZHEN_BUTTON = 'button[data-id="3148"]'

    # Активная кнопка (любая кнопка с классом, содержащим "Broadcasts_active")
    ACTIVE_CHANNEL_BUTTON = 'button[class*="Broadcasts_active"]'

    # Текущая программа в расписании
    CURRENT_PROGRAM = 'a[class*="ScheduleItemWidget_now"], a[class*="ScheduleItemWidget_current"]'

    # Расписание (контейнер)
    SCHEDULE_CONTAINER = '[class*="Schedule_wrapper"]'
    SCHEDULE_ITEM = '[class*="ScheduleItemWidget_wrapper"]'

    # Элементы внутри текущей программы
    CURRENT_PROGRAM_TIME = '[class*="ScheduleItemWidget_datetime"]'
    CURRENT_PROGRAM_TITLE = '[class*="ScheduleItemWidget_title"]'
    CURRENT_PROGRAM_AIR_ICON = '[class*="ScheduleItemWidget_air"]'
