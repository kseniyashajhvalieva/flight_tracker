from abc import ABC, abstractmethod
from typing import Any, Dict


class BaseAPI(ABC):
    """Абстрактный базовый класс для работы с API."""

    def __init__(self, base_url: str):
        self._base_url = base_url

    @abstractmethod
    def _connect(self, endpoint: str) -> Dict[str, Any]:
        """Приватный метод для подключения к API и отправки запроса."""
        pass

    @abstractmethod
    def get_data(self, country: str) -> Dict[str, Any]:
        """Получить данные о самолетах по названию страны."""
        pass
