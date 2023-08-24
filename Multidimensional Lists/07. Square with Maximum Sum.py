rows, cols = [int(x) for x in input().split(", ")]
matrix = []

for _ in range(rows):
    matrix.append([int(num) for num in input().split(", ")])

highest_sum = float("-inf")
temp = []
for i in range(rows - 1):
    for j in range(cols - 1):
        current_item = matrix[i][j]
        next_item = matrix[i][j + 1]
        below_item = matrix[i + 1][j]
        diagonal = matrix[i + 1][j + 1]
        current_sum = current_item + next_item + below_item + diagonal
        if current_sum > highest_sum:
            highest_sum = current_sum
            temp = [[current_item, next_item], [below_item, diagonal]]

print(temp[0][0], temp[0][1])
print(temp[1][0], temp[1][1])
print(highest_sum)


