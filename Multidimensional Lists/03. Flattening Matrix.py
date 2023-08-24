rows = int(input())
matrix = []

for i in range(rows):
    matrix.append([int(num) for num in input().split(", ")])

flattened_list = [int(x) for sublist in matrix for x in sublist]
print(flattened_list)