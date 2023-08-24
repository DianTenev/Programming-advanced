rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    matrix.append([int(num) for num in input().split()])

for col_index in range(cols):
    current_sum = 0
    for row_index in range(rows):
        current_sum += matrix[row_index][col_index]
    print(current_sum)

