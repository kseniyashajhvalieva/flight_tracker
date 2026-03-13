import json
import os
from typing import List, Dict, Any

from src.base_file_worker import BaseFileWorker


class JSONFileWorker(BaseFileWorker):
    """Класс для работы с JSON-файлами."""

    def __init__(self, filename: str = "aircrafts.json"):
        self._filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Приватный метод: создать файл, если его нет."""
        if not os.path.exists(self._filename):
            with open(self._filename, "w", encoding="utf-8") as f:
                json.dump([], f)

    def _read_data(self) -> List[Dict[str, Any]]:
        """Приватный метод: прочитать все данные из файла."""
        with open(self._filename, "r", encoding="utf-8") as f:
            return json.load(f)

    def _write_data(self, data: List[Dict[str, Any]]) -> None:
        """Приватный метод: записать все данные в файл."""
        with open(self._filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_data(self, data: Dict[str, Any]) -> None:
        """Добавить информацию о самолёте в файл (без дублей)."""
        all_data = self._read_data()
        # Проверяем, есть ли уже такой самолёт (по icao)
        if not any(item.get("icao") == data.get("icao") for item in all_data):
            all_data.append(data)
            self._write_data(all_data)

    def get_data(self, **criteria) -> List[Dict[str, Any]]:
        """Получить данные из файла по критериям."""
        all_data = self._read_data()

        if not criteria:
            return all_data
        # Фильтруем по переданным критериям
        result = []
        for item in all_data:
            match = True
            for key, value in criteria.items():
                if item.get(key) != value:
                    match = False
                    break
            if match:
                result.append(item)
        return result

    def delete_data(self, **criteria) -> None:
        """Удалить информацию о самолётах по критериям."""
        all_data = self._read_data()

        if not criteria:
            return
        # Оставляем только те, которые НЕ подходят под критерии
        new_data = []
        for item in all_data:
            match = True
            for key, value in criteria.items():
                if item.get(key) != value:
                    match = False
                    break
            if not match:
                new_data.append(item)

        self._write_data(new_data)
