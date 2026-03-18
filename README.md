# Трекер самолётов (Flight Tracker)

Приложение для получения информации о самолётах в воздушном пространстве выбранной страны через API opensky-network.org
и nominatim.openstreetmap.org.

## Структура проекта
```
flight_tracker/
├── data/ # JSON-файлы с данными о самолётах
├── src/ # Исходный код
│ ├── init.py
│ ├── base_api.py # Абстрактный класс для работы с API
│ ├── api_client.py # Класс-наследник для работы с nominatim и opensky
│ ├── aircraft.py # Класс самолёта
│ ├── base_file_worker.py # Абстрактный класс для работы с файлами
│ ├── json_file_worker.py # Класс для работы с JSON-файлами
│ └── utils.py # Вспомогательные функции
├── tests/ # Тесты
│ ├── init.py
│ ├── test_base_api.py
│ ├── test_api_client.py
│ ├── test_aircraft.py
│ ├── test_base_file_worker.py
│ ├── test_json_file_worker.py
│ └── test_utils.py
├── main.py # Точка входа
├── .env_template # Шаблон переменных окружения
├── .flake8 # Настройки линтера
├── .gitignore
├── pyproject.toml # Зависимости и настройки инструментов
└── README.md
```
## Установка и запуск

1. **Клонирование и переход в директорию**
2. **Установка зависимостей** (Poetry или pip)
3. **Настройка переменных окружения** (скопировать `.env_template` в `.env`)
4. **Запуск:** `python main.py`

## Функциональности

- Поиск самолётов по названию страны
- Сохранение данных в JSON-файл (без дубликатов)
- Вывод топ N самолётов по высоте
- Фильтрация по стране регистрации
- Сравнение самолётов по высоте и скорости

## Инструменты

- Python 3.13
- requests, pytest, flake8, black, isort, mypy
- Покрытие тестами >70%
