rows, cols = [int(x) for x in input().split()]
matrix = [[z for z in input().split()] for _ in range(rows)]
squares = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        current_item = matrix[i][j]
        next_item = matrix[i][j + 1]
        below_item = matrix[i + 1][j]
        diagonal_item = matrix[i + 1][j + 1]
        if current_item == next_item == below_item == diagonal_item:
            squares += 1

print(squares)
