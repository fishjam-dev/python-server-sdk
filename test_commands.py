import os


def run_tests():
    os.system("docker rm -f jellyfish")
    os.system("docker compose -f docker-compose-test.yaml pull")
    os.system("docker compose -f docker-compose-test.yaml up --remove-orphans test --exit-code-from test")
    os.system("docker compose -f docker-compose-test.yaml down")


def check_format():
    os.system("black --check .")


def run_formatter():
    os.system("black .")


def run_linter():
    os.system("poetry run pylint --rcfile=pylintrc jellyfish tests")
