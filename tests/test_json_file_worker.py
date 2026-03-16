import os

from src.json_file_worker import JSONFileWorker


def test_add_data(tmp_path):
    f = tmp_path / "test.json"
    w = JSONFileWorker(str(f))
    w.add_data({"icao": "abc"})
    assert os.path.exists(f)


def test_no_duplicates(tmp_path):
    f = tmp_path / "test.json"
    w = JSONFileWorker(str(f))
    w.add_data({"icao": "abc"})
    w.add_data({"icao": "abc"})
    assert len(w.get_data()) == 1


def test_get_data(tmp_path):
    f = tmp_path / "test.json"
    w = JSONFileWorker(str(f))
    w.add_data({"icao": "abc", "country": "RU"})
    assert len(w.get_data(country="RU")) == 1
