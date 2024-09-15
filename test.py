import pytest
from mylib.make_functions import calculate_mean, calculate_median, calculate_std_dev


def test_calculate_mean():
    data = [1, 2, 3, 4, 5]
    assert calculate_mean(data) == 3


def test_calculate_median():
    data = [1, 2, 3, 4, 5]
    assert calculate_median(data) == 3


def test_calculate_std_dev():
    data = [1, 2, 3, 4, 5]
    assert calculate_std_dev(data) == pytest.approx(1.58, rel=1e-2)
