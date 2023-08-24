number = int(input())
odd_set = set()
even_set = set()

for i in range(1, number + 1):
    name = list(input())
    current_result = 0
    for char in name:
        current_result += ord(char)
    current_result = current_result // i
    if current_result % 2 == 0:
        even_set.add(current_result)
    else:
        odd_set.add(current_result)


if sum(odd_set) == sum(even_set):
    temp = odd_set.union(even_set)
    print(*temp, sep=", ")
elif sum(odd_set) > sum(even_set):
    temp = odd_set.difference(even_set)
    print(*temp, sep=", ")
elif sum(odd_set) < sum(even_set):
    temp = odd_set.symmetric_difference(even_set)
    print(*temp, sep=", ")




