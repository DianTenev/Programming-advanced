numbers = tuple(input().split())
dictionary = {}

for i in numbers:
    if i not in dictionary:
        dictionary[i] = 0
    dictionary[i] += 1

for key, value in dictionary.items():
    print(f"{float(key):.1f} - {value} times")
