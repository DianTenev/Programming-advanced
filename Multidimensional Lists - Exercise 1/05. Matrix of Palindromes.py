rows, cols = [int(x) for x in input().split()]
matrix = []

for i in range(rows):
    inner_list = []
    for j in range(cols):
        inner_list.append(f"{chr(97 + i)}{chr(97 + i + j)}{chr(97 + i)}")
    matrix.append(inner_list)

for k in matrix:
    for l in k:
        print(l, end=" ")
    print()