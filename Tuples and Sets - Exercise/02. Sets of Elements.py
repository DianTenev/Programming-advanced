first, second = input().split()
first_set = set()
second_set = set()

for i in range(1, (int(first) + int(second) + 1)):
    current_number = int(input())
    if i <= int(first):
        first_set.add(current_number)
    else:
        second_set.add(current_number)

result = first_set.intersection(second_set)
print(*result, sep="\n")
