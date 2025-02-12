import pytest
from pytest_mock import MockerFixture
from sjtrade.utils import price_ceil, price_floor, price_round, sleep_until


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (9.989, 9.99),
        (10.01, 10.05),
        (50.01, 50.1),
        (100.01, 100.5),
        (500.01, 501),
        (1000.01, 1005),
        (5000.01, 5010),
        (0.111, 0.12),
        (1.111, 1.12),
        (9.999, 10),
        (10.0377878, 10.05),
    ],
)
def test_price_ceil(input: float, expected: float):
    assert price_ceil(input) == expected


@pytest.mark.parametrize(
    ("input", "expected"),
    [
        (9.999, 9.99),
        (10.19, 10.15),
        (50.19, 50.1),
        (101.9, 101.5),
        (519.9, 519.0),
        (1019.9, 1015.0),
        (5199.9, 5190.0),
        (0.119, 0.11),
        (1.119, 1.11),
        (9.999, 9.99),
    ],
)
def test_price_floor(input: float, expected: float):
    assert price_floor(input) == expected


@pytest.mark.parametrize(
    ("price", "up", "expected"),
    [
        (9.999, False, 9.99),
        (10.19, False, 10.15),
        (50.19, False, 50.1),
        (101.9, False, 101.5),
        (519.9, False, 519.0),
        (9.989, True, 9.99),
        (10.01, True, 10.05),
        (50.01, True, 50.1),
        (100.01, True, 100.5),
        (500.01, True, 501),
    ],
)
def test_price_round(price: float, up: bool, expected: float):
    assert price_round(price, up) == expected

@pytest.mark.freeze_time("2022-06-06 00:30:00 UTC")
def test_sleep_until(mocker: MockerFixture):
    sleep_mock = mocker.patch("time.sleep")
    sleep_until(9, 0, 1)
    sleep_mock.assert_called_once_with(30*60 + 1)