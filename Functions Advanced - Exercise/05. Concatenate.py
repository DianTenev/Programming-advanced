def concatenate(*args, **kwargs):
    result = "".join([x for x in args])
    for key, value in kwargs.items():
        result = result.replace(key, value)
    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))