number = int(input())
elements = set()

for i in range(number):
    current_elements = input().split()
    for j in current_elements:
        elements.add(j)

print(*elements, sep="\n")