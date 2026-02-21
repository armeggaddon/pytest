import pytest


@pytest.mark.slow
def test_slow_example():
    # simulate a slow test (kept fast here for demo)
    assert True


@pytest.mark.skip(reason="demonstration of skip")
def test_skip_example():
    assert False


@pytest.mark.xfail(reason="expected failure demo")
def test_xfail_example():
    assert 1 == 2
