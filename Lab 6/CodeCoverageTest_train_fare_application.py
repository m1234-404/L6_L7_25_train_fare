import pytest
from train_fare import base_fare, concession, tatkal_charge

def test_base_fare_valid():
    assert base_fare("SL", 100) == 100
    assert base_fare("3A", 20) == 50  # Tests minimum fare bound (50)

def test_base_fare_errors():
    with pytest.raises(ValueError):
        base_fare("INVALID", 100)
    with pytest.raises(ValueError):
        base_fare("SL", 0)

def test_concession_cases():
    assert concession(2, "M", False) == 100
    assert concession(10, "F", False) == 50
    assert concession(65, "F", False) == 50
    assert concession(65, "M", False) == 40
    assert concession(25, "M", True) == 0
    assert concession(25, "M", False) == 0

def test_tatkal_charge_cases():
    assert tatkal_charge("SL", 500) == 100
    assert tatkal_charge("2A", 2000) == 400
    assert tatkal_charge("3A", 500) == 150