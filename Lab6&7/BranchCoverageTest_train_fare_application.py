import pytest
from train_fare import base_fare, concession, tatkal_charge

def test_base_fare_branches():
    assert base_fare("SL", 100) == 100
    assert base_fare("SL", 20) == 50
    with pytest.raises(ValueError):
        base_fare("INVALID", 100)
    with pytest.raises(ValueError):
        base_fare("SL", 0)
    with pytest.raises(ValueError):
        base_fare("SL", -10)

def test_concession_branches():
    assert concession(25, "M", True) == 0
    assert concession(3, "M", False) == 100
    assert concession(10, "F", False) == 50
    assert concession(65, "F", False) == 50
    assert concession(65, "M", False) == 40
    assert concession(30, "M", False) == 0

def test_tatkal_charge_branches():
    # travel_class == "SL"
    assert tatkal_charge("SL", 5000) == 400  # 5000 // 10 = 500 -> capped at 400
    assert tatkal_charge("SL", 500) == 100   # 500 // 10 = 50 -> hits min < 100 -> 100
    assert tatkal_charge("SL", 1000) == 100  # 1000 // 10 = 100
    
    # travel_class != "SL" (e.g., "3A")
    assert tatkal_charge("3A", 2000) == 400  # 2000 * 3 // 10 = 600 -> capped at 400
    assert tatkal_charge("3A", 500) == 150   # 500 * 3 // 10 = 150
    assert tatkal_charge("3A", 200) == 100   # 200 * 3 // 10 = 60 -> hits min < 100 -> 100