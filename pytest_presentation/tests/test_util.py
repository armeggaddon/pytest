import pytest
from src.my_pkg import util


def test_add():
    assert util.add(2, 3) == 5


@pytest.mark.parametrize(
    "s,expected",
    [
        ("", True),
        ("a", True),
        ("RaceCar", True),
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
    ],
)
def test_is_palindrome(s, expected):
    assert util.is_palindrome(s) is expected


def test_tmp_path(tmp_path):
    p = tmp_path / "data.csv"
    rows = [["x", "y"], ["1", "2"]]
    util.write_csv(p, rows)
    assert util.read_csv(p) == rows


def test_monkeypatch_env(monkeypatch):
    monkeypatch.setenv("TEST_KEY", "value")
    import os

    assert os.environ.get("TEST_KEY") == "value"
