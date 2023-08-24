def age_assignment(*args, **kwargs):
    dictionary = {}
    result = ""
    for i in args:
        dictionary[i] = kwargs[i[0]]
    sorted_dict = sorted(dictionary.items(), key=lambda x: x[0])
    for name, age in sorted_dict:
        result += f"{name} is {age} years old." + "\n"
    return result


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))