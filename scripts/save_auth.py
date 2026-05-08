from playwright.sync_api import sync_playwright
import os


def save_auth_state():
    print("Запускаю браузер для сохранения сессии...")

    with sync_playwright() as p:
        # Запускаем ВИДИМЫЙ браузер, чтобы залогиниться вручную
        browser = p.chromium.launch(headless=False)

        # Создаём контекст
        context = browser.new_context(
            viewport={"width": 1440, "height": 900},
        )

        page = context.new_page()

        # Переходим в админку
        print("Открываю https://stage.1tv.ru/admin")
        page.goto("https://stage.1tv.ru/admin", wait_until="networkidle")

        # ВАЖНО: Теперь в открывшемся окне браузера:
        # 1. Введи логин/пароль
        # 32 Убедись, что ты внутри админки (видишь меню, кнопки и т.д.)

        input("После успешного входа нажми Enter в этом терминале...")

        # Сохраняем cookies, localStorage, sessionStorage
        state_path = "auth_state.json"
        context.storage_state(path=state_path)

        browser.close()

        print(f"Сессия сохранена в {os.path.abspath(state_path)}")
        print("Теперь ассистент сможет заходить в админку без повторного логина!")


if __name__ == "__main__":
    save_auth_state()

