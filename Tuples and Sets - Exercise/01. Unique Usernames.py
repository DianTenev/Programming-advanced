number = int(input())
my_set = set()

for i in range(number):
    name = input()
    my_set.add(name)

print(*my_set, sep="\n")