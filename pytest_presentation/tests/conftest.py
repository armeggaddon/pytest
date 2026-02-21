import pytest


@pytest.fixture
def sample_dict():
    return {"a": 1, "b": 2}


@pytest.fixture
def user_factory():
    users = []

    def _create(**kwargs):
        u = dict(kwargs)
        users.append(u)
        return u

    yield _create
    users.clear()


def pytest_addoption(parser):
    parser.addoption("--runslow", action="store_true", default=False, help="run slow tests")


def pytest_collection_modifyitems(config, items):
    # If --runslow not specified, skip tests marked as 'slow'
    if config.getoption("--runslow"):
        return

    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture(scope="module")
def module_resource(tmp_path_factory):
    p = tmp_path_factory.mktemp("module_res")
    f = p / "resource.txt"
    f.write_text("module resource")
    return f


@pytest.fixture
def resource_with_teardown():
    r = {"connected": True}
    yield r
    r["connected"] = False

