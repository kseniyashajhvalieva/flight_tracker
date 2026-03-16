from src.aircraft import Aircraft


def test_aircraft_creation():
    a = Aircraft("abc123", "TEST123", "Russia", 250.5, 10000.0, 5.0)
    assert a.icao == "abc123"


def test_aircraft_comparison():
    a1 = Aircraft("a1", "T1", "R", 100, 5000, 1)
    a2 = Aircraft("a2", "T2", "R", 100, 10000, 1)
    assert a1 < a2


def test_aircraft_to_dict():
    a = Aircraft("abc", "T", "R", 1, 1, 1)
    assert "icao" in a.to_dict()


def test_aircraft_repr():
    a = Aircraft("abc", "TEST", "Russia", 1, 1, 1)
    assert "TEST" in repr(a)
