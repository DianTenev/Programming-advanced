rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
sum_primary = 0
sum_secondary = 0

for i in range(rows):
    sum_primary += matrix[i][i]

for j in range(rows):
    sum_secondary += matrix[j][rows - j - 1]

print(abs(sum_primary - sum_secondary))

