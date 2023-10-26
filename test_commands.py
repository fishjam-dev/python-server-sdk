import os
import sys

def check_exit_code(command):
    command_exit_code = os.system(command)
    if command_exit_code != 0:
        sys.exit(command_exit_code >> 8)

def run_tests():
    check_exit_code("docker rm -f jellyfish")
    check_exit_code("docker compose -f docker-compose-test.yaml pull")
    check_exit_code("docker compose -f docker-compose-test.yaml up --remove-orphans test --exit-code-from test")
    check_exit_code("docker compose -f docker-compose-test.yaml down")


def check_format():
    check_exit_code("black --check .")
    


def run_formatter():
    check_exit_code("black .")


def run_linter():
    check_exit_code("poetry run pylint --rcfile=pylintrc jellyfish tests")
