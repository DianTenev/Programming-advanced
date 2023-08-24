n = int(input())
matrix = []
total_sum = 0

for _ in range(n):
    matrix.append([int(num) for num in input().split()])

for i in range(n):
    total_sum += matrix[i][i]

print(total_sum)
