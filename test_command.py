import os

def run_tests():
    os.system("docker rm -f jellyfish")
    os.system("docker compose -f docker-compose-test.yaml pull")
    os.system("docker compose -f docker-compose-test.yaml run --remove-orphans test")


def run_formatter():
    os.system("black .")

def run_linter():
    os.system("poetry run pylint --rcfile=pylintrc jellyfish tests")
