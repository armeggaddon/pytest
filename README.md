## pytest Presentation — Detailed Notes

This repository contains a compact demonstration of pytest features and patterns used in real projects. The notes below were generated from the accompanying presentation slides and are intended to serve as a README-friendly reference for each topic covered.

**Agenda:** Intro & Motivation • pytest Basics & First Tests • Fixtures & Parametrization • Markers, Skips & Plugins • Parallel & Coverage • Advanced Topics (Hypothesis, Hooks, Debugging) • Walkthrough • Q&A / Resources

## Intro & Motivation
- Why test: Tests provide confidence by catching regressions early, serve as executable documentation, and encourage modular, testable design. Run tests in CI to enforce quality and prevent regressions from reaching production.

## What is pytest?
- A lightweight testing framework with powerful features: fixtures, markers, plugins, and hooks. It uses plain `assert` statements and offers strong failure introspection to keep tests readable and easy to write. The ecosystem includes popular plugins like `pytest-xdist`, `pytest-cov`, and `hypothesis`.

## Installation & Basic Setup
- Install: `pip install pytest` and optional extras: `pip install pytest-cov pytest-xdist pytest-mock hypothesis`.
- Configure commonly used options in `pytest.ini` or `pyproject.toml` (markers, addopts). Example `pytest.ini` keys: `minversion`, `addopts`, and `markers`.

## Test Discovery & Naming
- Files: `test_*.py` or `*_test.py`.
- Test functions: `def test_...()`; test classes begin with `Test` and do not define `__init__`.
- Keep names descriptive of the behavior they assert.

## First Test Example
- Minimal example demonstrates pytest's low ceremony. Plain assertions yield informative diffs on failure and encourage fast feedback loops.

## Assertions & Failure Output
- Use plain `assert` expressions. pytest rewrites and displays the evaluated values for easier debugging. Reserve custom messages for unusual documentation needs.

## Running Tests & Useful Options
- Basic commands: `pytest`, `pytest -q`, `pytest -v`.
- Selection: `-k` (substring expressions), `-m` (markers).
- Control flow: `-x`/`--maxfail` to stop early, `-s` to disable capture for prints, and combine `-q` with `-k` for fast iteration.

## Fixtures: Introduction
- Use `@pytest.fixture` for reusable setup/teardown. Inject fixtures by naming them in test functions. Fixture scopes: `function`, `module`, `class`, `package`, `session`. Use `autouse=True` sparingly for implicit setup.

## Fixtures: Lifecycle & Teardown
- Use `yield` in fixtures to perform teardown after the test runs (setup → yield → teardown). Choose scope carefully: wider scopes increase speed but may introduce coupling.

## Parametrization
- Use `@pytest.mark.parametrize` to run a test function with multiple inputs, producing one test case per parameter set. Use `ids=` for readable test names and `indirect=True` to pass values into fixtures.

## Markers: skip and xfail
- `@pytest.mark.skip` always skips; `skipif(condition)` conditionally skips; `@pytest.mark.xfail` marks expected failures (useful for known issues). Register custom markers in `pytest.ini` to avoid warnings.

## Monkeypatch & Mocking
- Use the `monkeypatch` fixture to change environment variables or temporarily replace attributes. Use `unittest.mock` or `pytest-mock` for function-level mocking. Prefer `monkeypatch` for environment-level adjustments (e.g., `monkeypatch.setenv`, `monkeypatch.setattr`).

## `tmp_path`, Filesystem, and Temporary Resources
- Use `tmp_path` (a `pathlib.Path`) for temporary file creation; `tmp_path_factory` for module/session scoped temp dirs. Prefer these fixtures over `tempfile` for clarity and test isolation.

## Plugins: Ecosystem
- Key plugins:
	- `pytest-cov`: coverage reporting and enforcement
	- `pytest-xdist`: parallel test execution (`-n auto`)
	- `pytest-mock`: simpler mocking APIs
	- `pytest-asyncio`: async test helpers
	- `hypothesis`: property-based testing

## Parallel Testing with xdist
- Run tests in parallel with `pytest -n auto` or a fixed worker count. Beware shared resources; use locks or isolated test environments to avoid flakiness. When combining with coverage, use options that aggregate per-worker coverage.

## Coverage with pytest-cov
- Run `pytest --cov=your_package --cov-report=term-missing`. Fail the build on low coverage with `--cov-fail-under=80`. Generate HTML reports with `--cov-report=html` for human review.

## Test Selection & Troubleshooting
- Tools for iterative debugging: `-k` expressions, `-m` markers, `--lf` (last-failed), and `--maxfail`. Use `-q -k` to rapidly re-run targeted tests.

## Organizing Tests & `conftest.py`
- Place tests under a top-level `tests/` directory. Use `conftest.py` to share fixtures and hooks; pytest auto-discovers fixtures defined there. Keep `conftest.py` focused to avoid tight coupling across suites.

## Hooks & Plugin Points
- Use hooks like `pytest_addoption`, `pytest_configure`, `pytest_sessionstart`, and `pytest_runtest_setup` to customize collection, CLI options, and lifecycle behavior. Hooks are useful for adding project-wide flags (e.g., `--runslow`) or instrumentation.

## Debugging Tests
- Use `pytest -s --pdb` (or `--pdb`) to drop into a debugger on failure. `caplog` and `capsys` fixtures let you assert log output and captured stdout/stderr.

## Property-Based Testing with Hypothesis
- Hypothesis generates many inputs from strategies and automatically shrinks failing examples to minimal counterexamples. Use `@given` to replace example-based tests and find edge cases you might miss.

## CI Integration
- Run tests and coverage in CI (GitHub Actions, GitLab, etc.). Fail the pipeline when coverage drops (`--cov-fail-under`) and cache virtualenvs/deps to speed builds. Include quick-test jobs (targeted markers) and full-suite jobs (parallel + coverage) for balanced feedback.

## Flakiness: Causes & Mitigation
- Flaky tests fail intermittently due to nondeterminism (timing, network, shared state). Mitigate with isolation, deterministic fixtures, retries for ephemeral infra, and careful use of `xdist`.

## Organizing Complex Fixtures & Test Doubles
- Use factory fixtures to create objects (e.g., `user_factory`) for dynamic, test-local entities. For integration tests, prefer test doubles (`unittest.mock`, `pytest-mock`) or dedicated staging resources.

## Best Practices (Short)
- Keep tests small, focused, and independent.
- Name tests for the behavior they validate.
- Use fixtures to reduce duplication but not to hide intent.
- Run tests locally before pushing; ensure CI runs the full suite.

## Troubleshooting Checklist
- Are tests isolated? Check global state.
- Is order dependence causing failures? Use `--maxfail=1` to find first failure.
- Re-run failing tests with `-k` or `--lf` to speed debugging.

## Demo Commands
- Basic: `python -m pytest`
- Coverage: `python -m coverage run -m pytest` and `coverage html`
- Parallel: `python -m pytest -q -n auto`
- Marker examples: `python -m pytest -q -m "not slow"`

## Additional Resources
- Official pytest docs: https://docs.pytest.org/
- Plugin index: https://plugins.pytest.org/
- Hypothesis docs: https://hypothesis.readthedocs.io/

---
If you'd like, I can:
- tune these notes to be shorter/longer per section,
- add inline code examples for each section, or
- update the repository `README.md` to include a table of contents and links to relevant files (`tests/`, `tools/`, `src/my_pkg`).

Below are concise, copyable code examples for the main sections. Use them as starter snippets in your tests and docs.

## First Test Example
Example minimal function and test:
```python
# src/my_pkg/util.py
def add(a, b):
	return a + b

# tests/test_util.py
def test_add():
	from src.my_pkg.util import add
	assert add(2, 3) == 5
	assert add(-1, 1) == 0
```

## Assertions & Failure Output
Demonstrates helpful diffs from plain asserts:
```python
def test_fail_example():
	result = {'a': 1, 'b': 2}
	expected = {'a': 1, 'b': 3}
	assert result == expected
```

## Running Tests & Useful Options
Common commands:
```bash
pytest                # run all tests
pytest -q             # quieter output
pytest -k "name"     # run tests matching substring
pytest -m slow        # run tests marked slow
pytest -x             # stop after first failure
```

## Fixtures: Introduction
Simple fixture example:
```python
import pytest

@pytest.fixture
def sample_dict():
	return {"a": 1, "b": 2}

def test_sample(sample_dict):
	assert sample_dict["a"] == 1
```

## Fixtures: Lifecycle & Teardown (yield)
```python
import pytest

@pytest.fixture
def resource():
	r = open('tempfile.txt', 'w')   # setup
	yield r
	r.close()                       # teardown
```

## Parametrization
```python
import pytest

@pytest.mark.parametrize("x,y", [(1,2),(2,3)])
def test_inc(x, y):
	assert x + 1 == y
```

## Markers: skip and xfail
```python
import pytest

@pytest.mark.skip(reason="Not applicable on CI")
def test_skip_example():
	assert False

@pytest.mark.xfail(reason="Known bug")
def test_xfail_example():
	assert 1 == 2
```

## Monkeypatch & Mocking
```python
def test_env(monkeypatch):
	monkeypatch.setenv('API_KEY', 'test')
	import os
	assert os.environ['API_KEY'] == 'test'

def test_patch_attr(monkeypatch):
	import src.my_pkg.util as util
	monkeypatch.setattr(util, 'add', lambda a,b: 42)
	assert util.add(1,2) == 42
```

## tmp_path and Filesystem
```python
def test_write(tmp_path):
	p = tmp_path / 'data.txt'
	p.write_text('hello')
	assert p.read_text() == 'hello'
```

## Parallel Testing with xdist
Run tests in parallel (example):
```bash
pytest -n auto
```

## Coverage with pytest-cov
Run coverage and show missing lines:
```bash
pytest --cov=src --cov-report=term-missing
pytest --cov-fail-under=80
```

## Hooks & Plugin Points
Add a CLI option and skip tests unless requested:
```python
# conftest.py
def pytest_addoption(parser):
	parser.addoption('--runslow', action='store_true', help='run slow tests')

def pytest_collection_modifyitems(config, items):
	if not config.getoption('--runslow'):
		skip_slow = pytest.mark.skip(reason='need --runslow to run')
		for item in items:
			if 'slow' in item.keywords:
				item.add_marker(skip_slow)
```

## Debugging Tests
Drop into pdb on failure:
```bash
pytest -s --pdb
```
Or inside a test:
```python
import pdb

def test_debug():
	pdb.set_trace()
	assert 1
```

## Property-Based Testing with Hypothesis
Simple Hypothesis example:
```python
from hypothesis import given, strategies as st

@given(st.integers(), st.integers())
def test_add_commutative(a, b):
	assert a + b == b + a
```

## Organizing Complex Fixtures (factory)
```python
import pytest

@pytest.fixture
def user_factory(db_session):
	def _create(**kwargs):
		u = User(**kwargs)
		db_session.add(u)
		db_session.commit()
		return u
	return _create

def test_user(user_factory):
	u = user_factory(name='alice')
	assert u.name == 'alice'
```

## Test Doubles & Integration
Using `unittest.mock`:
```python
from unittest.mock import Mock

def test_mock():
	m = Mock(return_value=3)
	assert m(1) == 3
```

## Demo Commands (quick reference)
```bash
python -m pytest
python -m coverage run -m pytest
coverage html
python -m pytest -q -m "not slow"
python -m pytest -q -n auto
```

- A small example package `my_pkg` with utility functions.
- Tests demonstrating pytest features (fixtures, parametrization, tmp_path, monkeypatch, async tests).
- A Python script to generate a PowerPoint presentation and a one-slide cheatsheet (`tools/generate_presentation.py`).
- A sample GitHub Actions workflow in `.github/workflows/pytest.yml` that runs tests and coverage.

How to generate the slides (locally):

```powershell
python -m pip install -r requirements.txt
python tools/generate_presentation.py
```

This creates `pytest_presentation.pptx` and `cheatsheet_slide.pptx` in the repository root.
