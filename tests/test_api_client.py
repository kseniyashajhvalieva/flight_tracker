import pytest
from unittest.mock import patch, MagicMock
from src.api_client import ApiClient


@patch("requests.Session.get")
def test_get_data_country_not_found(mock_get):
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.json.return_value = []
    mock_get.return_value = mock_resp

    client = ApiClient("https://test.com")
    result = client.get_data("Atlantis")
    assert "error" in result
