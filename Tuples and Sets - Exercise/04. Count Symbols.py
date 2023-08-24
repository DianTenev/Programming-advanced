text = list(input())
dictionary = {}

for i in text:
    if i not in dictionary:
        dictionary[i] = 0
    dictionary[i] += 1
sorted_dictionary = sorted(dictionary)

for current_item in sorted_dictionary:
    print(f"{current_item}: {dictionary[current_item]} time/s")




