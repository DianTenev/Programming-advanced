rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([int(num) for num in input().split(", ") if int(num) % 2 == 0])

print(matrix)
