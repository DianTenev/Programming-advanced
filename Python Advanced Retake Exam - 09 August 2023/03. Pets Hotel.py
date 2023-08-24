def accommodate_new_pets(hotel_capacity, max_weight, *args):
    accommodated_pets = 0
    dictionary = {}
    for i in args:
        pet_type = i[0]
        pet_weight = i[1]
        if accommodated_pets < hotel_capacity:
            if pet_weight <= max_weight:
                accommodated_pets += 1
                if pet_type not in dictionary:
                    dictionary[pet_type] = 0
                dictionary[pet_type] += 1
        elif accommodated_pets >= hotel_capacity:
            result = "You did not manage to accommodate all pets!\n"
            break
    else:
        result = f"All pets are accommodated! Available capacity: {hotel_capacity - accommodated_pets}.\n"

    result += "Accommodated pets:\n"
    ordered_dict = sorted(dictionary)
    result += "\n".join([f"{i}: {dictionary[i]}" for i in ordered_dict])
    return result


print(accommodate_new_pets(
    10,
    15.0,
    ("cat", 5.8),
    ("dog", 10.0),
))

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))

print(accommodate_new_pets(
    2,
    15.0,
    ("dog", 10.0),
    ("cat", 5.8),
    ("cat", 2.7),
))






