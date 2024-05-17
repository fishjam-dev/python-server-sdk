import os
import shutil
import subprocess
import sys
from pathlib import Path


def check_exit_code(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    while True:
        output = process.stdout.readline()
        if output == b"" and process.poll() is not None:
            break
        if output:
            print(str(output.strip(), "utf-8"))
    exit_code = process.poll()
    if exit_code != 0:
        sys.exit(exit_code)


def run_tests():
    check_exit_code("docker rm -f fishjam")
    check_exit_code("docker compose -f docker-compose-test.yaml pull")
    check_exit_code(
        "docker compose -f docker-compose-test.yaml up --remove-orphans test \
        --exit-code-from test"
    )
    check_exit_code("docker compose -f docker-compose-test.yaml down")


def run_examples():
    print("Start examples")

    examples = os.listdir("./examples")

    for example in examples:
        check_exit_code(f"python ./examples/{example}")
        print(f"After example from file: {example}")
    print("All examples run without errors")


def run_local_test():
    check_exit_code('poetry run pytest -m "not file_component_sources"')


def run_formatter():
    check_exit_code("ruff format .")


def run_format_check():
    check_exit_code("ruff format . --check")


def run_linter():
    check_exit_code("ruff check .")


def run_linter_fix():
    check_exit_code("ruff check . --fix")


def generate_docs():
    check_exit_code(
        "pdoc \
    --include-undocumented \
    --favicon https://logo.swmansion.com/membrane/\?width\=100\&variant\=signetDark\
    --logo https://logo.swmansion.com/membrane/\?width\=70\&variant\=signetDark\
    -t templates/doc \
    -o doc \
    fishjam"
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


def update_client():
    check_exit_code(
        "openapi-python-client update\
            --url https://raw.githubusercontent.com/fishjam-dev/"
        "fishjam/main/openapi.yaml \
            --config openapi-python-client-config.yaml \
            --custom-template-path=templates/openapi"
    )
