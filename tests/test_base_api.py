import pytest
from src.base_api import BaseAPI


def test_base_api_cannot_instantiate():
    """Проверка, что абстрактный класс нельзя создать напрямую."""
    with pytest.raises(TypeError):
        BaseAPI("http://test.com")