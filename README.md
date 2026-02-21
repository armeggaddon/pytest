# pytest Presentation Demo

This repository contains:

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
