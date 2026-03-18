from abc import ABC, abstractmethod
from typing import Any, Dict, List


class BaseFileWorker(ABC):
    """Абстрактный базовый класс для работы с файлами."""

    @abstractmethod
    def add_data(self, data: Dict[str, Any]) -> None:
        """Добавить информацию о самолёте в файл."""
        pass

    @abstractmethod
    def get_data(self, **criteria: Any) -> List[Dict[str, Any]]:
        """Получить данные из файла по указанным критериям."""
        pass

    @abstractmethod
    def delete_data(self, **criteria: Any) -> None:
        """Удалить информацию о самолётах по критериям."""
        pass
