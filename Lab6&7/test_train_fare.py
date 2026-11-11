import pytest
from hypothesis import given, strategies as st
from train_fare import base_fare, concession, tatkal_charge

# --- LAB 6 UNIT TESTS ---

def test_sleeper_fare():
    assert base_fare("SL", 500) == 500
    assert base_fare("SL", 10) == 50  
    with pytest.raises(ValueError):
        base_fare("INVALID", 100)
    with pytest.raises(ValueError):
        base_fare("SL", 0)

def test_adult_no_concession():
    assert concession(30, "M", False) == 0
    assert concession(25, "M", True) == 0   
    assert concession(3, "M", False) == 100  
    assert concession(10, "F", False) == 50  
    assert concession(65, "F", False) == 50  
    assert concession(65, "M", False) == 40  

def test_tatkal_charge_branches():
    assert tatkal_charge("SL", 5000) == 400  
    assert tatkal_charge("SL", 500) == 100   
    assert tatkal_charge("SL", 1000) == 100  
    assert tatkal_charge("3A", 2000) == 400  
    assert tatkal_charge("3A", 500) == 150   
    assert tatkal_charge("3A", 200) == 100


# --- LAB 7 FUZZ TESTS (AFTER HARDENING) ---

fuzz_inputs = st.one_of(
    st.integers(),
    st.floats(allow_nan=True, allow_infinity=True),
    st.text(),
    st.none(),
    st.booleans()
)

@given(travel_class=fuzz_inputs, distance=fuzz_inputs)
def test_base_fare_fuzz(travel_class, distance):
    try:
        base_fare(travel_class, distance)
    except (ValueError, TypeError):
        pass  # Handled defensive exceptions are expected and correct

@given(age=fuzz_inputs, gender=fuzz_inputs, is_tatkal=fuzz_inputs)
def test_concession_fuzz(age, gender, is_tatkal):
    try:
        concession(age, gender, is_tatkal)
    except (ValueError, TypeError):
        pass

@given(travel_class=fuzz_inputs, fare=fuzz_inputs)
def test_tatkal_charge_fuzz(travel_class, fare):
    try:
        tatkal_charge(travel_class, fare)
    except (ValueError, TypeError):
        pass