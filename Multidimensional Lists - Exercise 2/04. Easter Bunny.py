rows = int(input())
matrix = [[x for x in input().split()] for _ in range(rows)]
bunny = [[k, l] for l in range(rows) for k in range(rows) if matrix[k][l] == "B"]
path_up = []
path_left = []
path_down = []
path_right = []
sum_up = 0
sum_left = 0
sum_down = 0
sum_right = 0


for num_up in range(bunny[0][0], 0, -1):
    if matrix[num_up - 1][bunny[0][1]] == "X":
        break
    sum_up += int(matrix[num_up - 1][bunny[0][1]])
    path_up.append([num_up - 1, bunny[0][1]])

for num_left in range(bunny[0][1] - 1, -1, -1):
    if matrix[bunny[0][0]][num_left] == "X":
        break
    sum_left += int(matrix[bunny[0][0]][num_left])
    path_left.append([bunny[0][0], num_left])

for num_down in range(bunny[0][0] + 1, rows):
    if matrix[num_down][bunny[0][1]] == "X":
        break
    sum_down += int(matrix[num_down][bunny[0][1]])
    path_down.append([num_down, bunny[0][1]])

for num_right in range(bunny[0][1] + 1, rows):
    if matrix[bunny[0][0]][num_right] == "X":
        break
    sum_right += int(matrix[bunny[0][0]][num_right])
    path_right.append([bunny[0][0], num_right])

max_sum = max(sum_up, sum_left, sum_right, sum_down)
if sum_up == max_sum:
    print("up")
    for up in path_up:
        print(up)
    print(max_sum)
elif sum_left == max_sum:
    print("left")
    for left in path_left:
        print(left)
    print(max_sum)
elif sum_right == max_sum:
    print("right")
    for right in path_right:
        print(right)
    print(max_sum)
elif sum_down == max_sum:
    print("down")
    for down in path_down:
        print(down)
    print(max_sum)


