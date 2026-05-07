# Локаторы страницы Эфирные позиции

class AirPositionsLocators:
    LIST_LINK = 'a[href*="/admin/air_positions"]'
    NEW_BTN = 'a[href*="/admin/air_positions/new"]'
    SAVE_BTN = '#save_submit'
    ERROR_BLOCK = 'div.errors[data-role="errors"]'
    TITLE_ERROR = 'li[data-field="title"]'
    ORBIT_ERROR = 'li[data-field="air_position_orbits"]'
    FIELD_WITH_ERRORS = '.field_with_errors'
    TITLE_INPUT = '#air_position_title'

