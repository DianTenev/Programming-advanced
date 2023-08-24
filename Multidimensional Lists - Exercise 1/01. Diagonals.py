rows = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(rows)]
sum_primary = 0
sum_secondary = 0
primary_diagonal = []
secondary_diagonal = []

for i in range(rows):
    sum_primary += matrix[i][i]
    primary_diagonal.append(matrix[i][i])

for j in range(rows):
    sum_secondary += matrix[j][rows - j - 1]
    secondary_diagonal.append(matrix[j][rows - j - 1])

print(f"Primary diagonal: {', '.join(map(str, primary_diagonal))}. Sum: {sum_primary}")
print(f"Secondary diagonal: {', '.join(map(str, secondary_diagonal))}. Sum: {sum_secondary}")

