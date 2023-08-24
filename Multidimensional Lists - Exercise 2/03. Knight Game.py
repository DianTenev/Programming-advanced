rows = int(input())
matrix = [list(input()) for _ in range(rows)]
removes = 0
positions = ((-1, 2), (-1, -2), (-2, -1), (-2, 1), (1, 2), (1, -2), (2, -1), (2, 1))
attacks = 1

while True:
    max_attacks = 0
    knight_max = []
    for i in range(rows):
        for j in range(rows):
            if matrix[i][j] == "K":
                attacks = 0
                for k in positions:
                    row_pos = k[0]
                    col_pos = k[1]
                    if 0 <= i + row_pos < rows and 0 <= j + col_pos < rows:
                        if matrix[i + row_pos][j + col_pos] == "K":
                            attacks += 1
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_max = [i, j]
    if max_attacks == 0:
        break
    removes += 1
    matrix[knight_max[0]][knight_max[1]] = "0"
print(removes)

