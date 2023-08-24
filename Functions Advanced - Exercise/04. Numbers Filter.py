def even_odd_filter(**kwargs):
    dictionary = {}

    for key, value in kwargs.items():
        if key == "odd":
            odd_list = [int(x) for x in kwargs["odd"] if x % 2 != 0]
            dictionary["odd"] = odd_list
        elif key == "even":
            even_list = [int(x) for x in kwargs["even"] if x % 2 == 0]
            dictionary["even"] = even_list

    return dict(sorted(dictionary.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(odd=[1, 2, 3, 4, 10, 5], even=[3, 4, 5, 7, 10, 2, 5, 5, 2]))
print(even_odd_filter(odd=[2, 2, 30, 44, 10, 5]))
