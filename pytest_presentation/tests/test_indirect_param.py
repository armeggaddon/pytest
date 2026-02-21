import pytest


@pytest.fixture
def config(request):
    return {"value": request.param}


@pytest.mark.parametrize("config,expected", [(1, 1), (2, 2)], indirect=["config"])
def test_indirect(config, expected):
    assert config["value"] == expected
