from email.policy import default

import pytest

class Options:
    stand: str = "--stand"


def pytest_addoptions(parser: pytest.Parser):
    parser.addoption(
        Options.stand,
        action="store",
        default="ST",
        help="Стенды для запуска тестов",
        choices=["ST", "DEV", "IFT"]
    )
