rows, cols = [int(x) for x in input().split()]
matrix = [[int(z) for z in input().split()] for _ in range(rows)]
temp = []
highest_sum = float("-inf")
current_sum = 0

for j in range(cols - 2):
    for i in range(rows - 2):
        current_sum += sum(matrix[i][j:(j + 3)]) + sum(matrix[i + 1][j:(j + 3)]) + sum(matrix[i + 2][j:(j + 3)])
        if current_sum > highest_sum:
            highest_sum = current_sum
            temp = [matrix[i][j:(j + 3)], matrix[i + 1][j:(j + 3)], matrix[i + 2][j:(j + 3)]]
        current_sum = 0

print(f"Sum = {highest_sum}")

for k in temp:
    for l in k:
        print(l, end=" ")
    print()

