from typing import Any, Dict

import requests

from src.base_api import BaseAPI


class ApiClient(BaseAPI):
    """Класс для работы с API nominatim и opensky."""

    def __init__(self, base_url: str):
        super().__init__(base_url)
        self._session = requests.Session()

    def _connect(self, endpoint: str) -> Dict[str, Any]:
        """Приватный метод для отправки запроса к API."""
        url = f"{self._base_url}{endpoint}"
        response = self._session.get(url)

        if response.status_code != 200:
            raise Exception(f"Ошибка API: {response.status_code}")
        return response.json()  # type: ignore[no-any-return]

    def get_data(self, country: str) -> Dict[str, Any]:
        """Получить данные о самолетах по названию страны."""
        # Сначала получаем координаты страны через nominatim
        geo_endpoint = f"/search?q={country}&format=json"
        geo_data = self._connect(geo_endpoint)

        if not geo_data or not isinstance(geo_data, list) or len(geo_data) == 0:
            return {"error": "Страна не найдена"}

        first_result = geo_data[0]
        if not isinstance(first_result, dict):
            return {"error": "Некорректный ответ от API"}

        bounds = first_result.get("boundingbox", [])
        if len(bounds) != 4:
            return {"error": "Некорректные границы страны"}

        # Формируем запрос к opensky по координатам
        lat_min, lat_max, lon_min, lon_max = map(float, bounds)
        opensky_endpoint = f"/states/all?lamin={lat_min}&lamax={lat_max}&lomin={lon_min}&lomax={lon_max}"
        return self._connect(opensky_endpoint)
