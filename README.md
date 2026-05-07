#1st_Channel Test Automation
##  Быстрый старт для команды

### 1. Клонирование и подготовка
```bash
git clone <repo-url>
cd 1st_Channel
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\\Scripts\\activate   # Windows
pip install -r requirements.txt
playwright install chromium
#Сохранение сессии авторизации
Сохрани сессию один раз:
python scripts/save_auth.py
Откроется браузер - войди в админку - нажми Enter в терминале.
Файл auth_state.json появится в корне (добавлен в .gitignore).
