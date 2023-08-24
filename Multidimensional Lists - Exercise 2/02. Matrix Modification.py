rows = int(input())
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

command = input()
while command != "END":
    com, row, col, value = command.split()
    if int(row) not in range(0, len(matrix)) or int(col) not in range(0, len(matrix[int(row)])):
        command = input()
        print("Invalid coordinates")
        continue
    if com == "Add":
        matrix[int(row)][int(col)] += int(value)
    else:
        matrix[int(row)][int(col)] -= int(value)
    command = input()

for k in matrix:
    for l in k:
        print(l, end=" ")
    print()
