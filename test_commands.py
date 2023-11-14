import os
import sys
from pathlib import Path
import shutil
import pdoc as p
from pdoc import render


def check_exit_code(command):
    command_exit_code = os.system(command)
    if command_exit_code != 0:
        sys.exit(command_exit_code >> 8)


def run_tests():
    check_exit_code("docker rm -f jellyfish")
    check_exit_code("docker compose -f docker-compose-test.yaml pull")
    check_exit_code(
        "docker compose -f docker-compose-test.yaml up --remove-orphans test --exit-code-from test"
    )
    check_exit_code("docker compose -f docker-compose-test.yaml down")


def check_format():
    check_exit_code("black --check .")


def run_formatter():
    check_exit_code("black .")


def run_linter():
    check_exit_code("poetry run pylint --rcfile=pylintrc jellyfish tests")


def generate_docs():
    check_exit_code(
        "pdoc \
    --no-include-undocumented \
    --favicon https://logo.swmansion.com/membrane/\?width\=100\&variant\=signetDark\
    --logo https://logo.swmansion.com/membrane/\?width\=70\&variant\=signetDark\
    -t doc_templates \
    -o doc \
    jellyfish"
    )
    here = Path(__file__).parent
    input = here / "doc"
    out = here / "docs" / "api"

    if out.exists():
        shutil.rmtree(out)

    shutil.copytree(input, out)

    # ...and rename the .html files to .md so that mkdocs picks them up!
    for f in out.glob("**/*.html"):
        f.rename(f.with_suffix(".md"))
