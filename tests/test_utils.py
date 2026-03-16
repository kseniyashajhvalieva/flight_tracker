from src.aircraft import Aircraft
from src.utils import filter_by_country, get_top_n, sort_by_velocity


def test_filter_by_country():
    a1 = Aircraft("a1", "T1", "Russia", 1, 1, 1)
    a2 = Aircraft("a2", "T2", "USA", 1, 1, 1)
    result = filter_by_country([a1, a2], "Russia")
    assert len(result) == 1


def test_get_top_n():
    a1 = Aircraft("a1", "T1", "R", 1, 100, 1)
    a2 = Aircraft("a2", "T2", "R", 1, 200, 1)
    a3 = Aircraft("a3", "T3", "R", 1, 300, 1)
    top = get_top_n([a1, a2, a3], 2, "altitude")
    assert len(top) == 2
    assert top[0].altitude == 300


def test_sort_by_velocity():
    a1 = Aircraft("a1", "T1", "R", 100, 1, 1)
    a2 = Aircraft("a2", "T2", "R", 200, 1, 1)
    result = sort_by_velocity([a1, a2])
    assert result[0].velocity == 100
