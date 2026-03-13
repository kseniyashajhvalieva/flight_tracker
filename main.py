import logging
from src.api_client import ApiClient
from src.aircraft import Aircraft
from src.json_file_worker import JSONFileWorker
from src.utils import filter_by_country, get_top_n, aircrafts_to_dict_list, dict_list_to_aircrafts

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def print_aircrafts(aircrafts, title="Результаты"):
    """Красиво вывести список самолётов."""
    print(f"\n--- {title} ---")
    if not aircrafts:
        print("Нет данных")
        return
    for i, a in enumerate(aircrafts, 1):
        print(f"{i}. {a.callsign} ({a.country}) | Высота: {a.altitude} м | Скорость: {a.velocity} м/с")


def user_interaction():
    """Главная функция для взаимодействия с пользователем."""
    print("=== Трекер самолётов ===")

    # Создаём клиент API
    api = ApiClient("https://opensky-network.org/api")

    # Запрашиваем страну
    country = input("Введите название страны: ").strip()
    if not country:
        print("Страна не указана")
        return

    # Получаем данные о самолётах
    print(f"Запрашиваю данные для {country}...")
    try:
        data = api.get_data(country)
        if "error" in data:
            print(f"Ошибка: {data['error']}")
            return
    except Exception as e:
        print(f"Ошибка при запросе к API: {e}")
        return

    # Преобразуем сырые данные в список объектов Aircraft
    aircrafts = []
    states = data.get("states", [])
    for state in states:
        try:
            # Формат ответа opensky:
            # 0: icao24, 1: callsign, 2: origin_country, 3: time_position,
            # 4: last_contact, 5: longitude, 6: latitude, 7: baro_altitude,
            # 8: on_ground, 9: velocity, 10: true_track, 11: vertical_rate,
            # 12: sensors, 13: geo_altitude, 14: squawk, 15: spi, 16: position_source
            if state[7] is not None and state[9] is not None:  # только если есть высота и скорость
                a = Aircraft(
                    icao=state[0],
                    callsign=state[1].strip() if state[1] else "N/A",
                    country=state[2],
                    velocity=float(state[9]),
                    altitude=float(state[7]),
                    vertical_rate=float(state[11]) if state[11] else 0.0
                )
                aircrafts.append(a)
        except (ValueError, TypeError, IndexError) as e:
            logger.debug(f"Пропущена некорректная запись: {e}")
            continue

    print(f"Найдено самолётов: {len(aircrafts)}")

    # Сохраняем в JSON
    saver = JSONFileWorker("data/aircrafts.json")
    for a in aircrafts:
        saver.add_data(a.to_dict())
    print("Данные сохранены в файл")

    while True:
        print("\n--- Меню ---")
        print("1. Показать топ N самолётов по высоте")
        print("2. Показать самолёты по стране регистрации")
        print("3. Выйти")

        choice = input("Выберите действие: ").strip()

        if choice == "1":
            try:
                n = int(input("Введите количество (N): "))
                top = get_top_n(aircrafts, n, by="altitude")
                print_aircrafts(top, f"Топ {n} по высоте")
            except ValueError:
                print("Некорректное число")

        elif choice == "2":
            country_filter = input("Введите страну регистрации: ").strip()
            filtered = filter_by_country(aircrafts, country_filter)
            print_aircrafts(filtered, f"Самолёты из {country_filter}")

        elif choice == "3":
            print("Выход")
            break

        else:
            print("Неверный выбор")


if __name__ == "__main__":
    user_interaction()