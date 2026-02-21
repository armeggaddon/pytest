import logging
from src.my_pkg.util import inc


def function_logging():
    logging.getLogger('mylogger').warning('warned!')


def test_caplog(caplog):
    caplog.set_level(logging.WARNING)
    function_logging()
    assert 'warned!' in caplog.text


def test_capsys(capsys):
    print('hello')
    captured = capsys.readouterr()
    assert captured.out.strip() == 'hello'


def test_inc():
    assert inc(3) == 4
