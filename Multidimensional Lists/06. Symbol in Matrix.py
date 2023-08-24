rows_and_cols = int(input())
matrix = []
is_found = False

for _ in range(rows_and_cols):
    inner_list = [el for el in input()]
    matrix.append(inner_list)

searched_symbol = input()

for row_index in range(rows_and_cols):
    for col_index in range(rows_and_cols):
        if matrix[row_index][col_index] == searched_symbol:
            position = (row_index, col_index)
            print(position)
            is_found = True
            break
    if is_found:
        break
else:
    print(f"{searched_symbol} does not occur in the matrix")
