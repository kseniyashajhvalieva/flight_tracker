from typing import Any


class Aircraft:
    """Класс для представления информации о самолёте."""

    __slots__ = ("_icao", "_callsign", "_country", "_velocity", "_altitude", "_vertical_rate")

    def __init__(self, icao: str, callsign: str, country: str, velocity: float, altitude: float, vertical_rate: float):
        self._icao = self._validate_string(icao, "ICAO")
        self._callsign = self._validate_string(callsign, "Callsign")
        self._country = self._validate_string(country, "Country")
        self._velocity = self._validate_float(velocity, "Velocity")
        self._altitude = self._validate_float(altitude, "Altitude")
        self._vertical_rate = self._validate_float(vertical_rate, "Vertical rate")

    def _validate_string(self, value: Any, field_name: str) -> str:
        """Приватный метод валидации строк."""
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{field_name} must be a non-empty string")
        return value.strip()

    def _validate_float(self, value: Any, field_name: str) -> float:
        """Приватный метод валидации чисел."""
        try:
            val = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"{field_name} must be a number")
        return val

    # Магические методы для сравнения по высоте
    def __lt__(self, other: "Aircraft") -> bool:
        """Меньше (по высоте)."""
        return self._altitude < other._altitude

    def __le__(self, other: "Aircraft") -> bool:
        """Меньше или равно."""
        return self._altitude <= other._altitude

    def __gt__(self, other: "Aircraft") -> bool:
        """Больше."""
        return self._altitude > other._altitude

    def __ge__(self, other: "Aircraft") -> bool:
        """Больше или равно."""
        return self._altitude >= other._altitude

    def __eq__(self, other: object) -> bool:
        """Равно."""
        if not isinstance(other, Aircraft):
            return NotImplemented
        return self._altitude == other._altitude

    # Магические методы для сравнения по скорости
    def compare_by_velocity(self, other: "Aircraft") -> int:
        """Сравнить по скорости (для сортировки)."""
        if self._velocity < other._velocity:
            return -1
        elif self._velocity > other._velocity:
            return 1
        return 0

    @property
    def icao(self) -> str:
        return self._icao

    @property
    def callsign(self) -> str:
        return self._callsign

    @property
    def country(self) -> str:
        return self._country

    @property
    def velocity(self) -> float:
        return self._velocity

    @property
    def altitude(self) -> float:
        return self._altitude

    @property
    def vertical_rate(self) -> float:
        return self._vertical_rate

    def to_dict(self) -> dict:
        """Преобразовать объект в словарь для сохранения в JSON."""
        return {
            "icao": self._icao,
            "callsign": self._callsign,
            "country": self._country,
            "velocity": self._velocity,
            "altitude": self._altitude,
            "vertical_rate": self._vertical_rate,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Aircraft":
        """Создать объект из словаря (при чтении из JSON)."""
        return cls(
            icao=data["icao"],
            callsign=data["callsign"],
            country=data["country"],
            velocity=data["velocity"],
            altitude=data["altitude"],
            vertical_rate=data["vertical_rate"],
        )

    def __repr__(self) -> str:
        return f"Aircraft(callsign={self._callsign}, country={self._country}, altitude={self._altitude})"
