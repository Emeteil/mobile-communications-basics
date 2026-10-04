venv := ".venv"
python := if os_family() == "windows" { venv / "Scripts" / "python.exe" } else { venv / "bin" / "python" }

setup:
    @test -e "{{python}}" || python -m venv {{venv}}
    @"{{python}}" -m pip install -q -q -r requirements.txt flake8