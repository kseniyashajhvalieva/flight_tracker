from typing import List, Dict, Any
from src.aircraft import Aircraft


def filter_by_country(aircrafts: List[Aircraft], country: str) -> List[Aircraft]:
    """Отфильтровать самолёты по стране регистрации."""
    return [a for a in aircrafts if a.country.lower() == country.lower()]


def sort_by_altitude(aircrafts: List[Aircraft], reverse: bool = False) -> List[Aircraft]:
    """Отсортировать самолёты по высоте."""
    return sorted(aircrafts, reverse=reverse)


def sort_by_velocity(aircrafts: List[Aircraft], reverse: bool = False) -> List[Aircraft]:
    """Отсортировать самолёты по скорости."""
    return sorted(aircrafts, key=lambda a: a.velocity, reverse=reverse)


def get_top_n(aircrafts: List[Aircraft], n: int, by: str = "altitude") -> List[Aircraft]:
    """Получить топ N самолётов по указанному параметру."""
    if by == "altitude":
        sorted_list = sort_by_altitude(aircrafts, reverse=True)
    elif by == "velocity":
        sorted_list = sort_by_velocity(aircrafts, reverse=True)
    else:
        raise ValueError("Параметр 'by' должен быть 'altitude' или 'velocity'")

    return sorted_list[:n]


def aircrafts_to_dict_list(aircrafts: List[Aircraft]) -> List[Dict[str, Any]]:
    """Преобразовать список объектов Aircraft в список словарей."""
    return [a.to_dict() for a in aircrafts]


def dict_list_to_aircrafts(data: List[Dict[str, Any]]) -> List[Aircraft]:
    """Преобразовать список словарей в список объектов Aircraft."""
    return [Aircraft.from_dict(item) for item in data]
