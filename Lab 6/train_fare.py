RATE_PER_KM = {"SL": 1, "3A": 2, "2A": 3, "1A": 5}


def base_fare(travel_class, distance_km):
    if not isinstance(travel_class, str) or travel_class not in RATE_PER_KM:
        raise ValueError("unknown class")
    if not isinstance(distance_km, (int, float)) or isinstance(distance_km, bool):
        raise TypeError("invalid distance type")
    
    import math
    if math.isnan(distance_km) or math.isinf(distance_km) or distance_km <= 0:
        raise ValueError("invalid distance")
        
    fare = RATE_PER_KM[travel_class] * distance_km
    if fare < 50:
        fare = 50
    return fare


def concession(age, gender, is_tatkal):
    if not isinstance(is_tatkal, bool):
        raise TypeError("is_tatkal must be a boolean")
    if is_tatkal:
        return 0
        
    if not isinstance(age, int) or isinstance(age, bool):
        raise TypeError("age must be an integer")
    if not isinstance(gender, str):
        raise TypeError("gender must be a string")
        
    if age < 5:
        return 100
    elif age <= 12:
        return 50
    elif age >= 60:
        if gender == "F":
            return 50
        return 40
    return 0


def tatkal_charge(travel_class, fare):
    if not isinstance(travel_class, str) or travel_class not in RATE_PER_KM:
        raise ValueError("unknown class")
    if not isinstance(fare, (int, float)) or isinstance(fare, bool):
        raise TypeError("fare must be numeric")
        
    import math
    if math.isnan(fare) or math.isinf(fare):
        raise ValueError("invalid fare")

    if travel_class == "SL":
        charge = fare // 10
    else:
        charge = fare * 3 // 10
        
    if charge > 400:
        charge = 400
    elif charge < 100:
        charge = 100
    return charge


if __name__ == "__main__":
    print("Running hardened train_fare.py...")
    print("Base Fare:", base_fare("SL", 100))