def is_valid(value, max_value):
    return 0 <= value < max_value


def next_move(command, current_row, current_col):
    if command == "up" and is_valid(current_row - 1, rows):
        return current_row - 1, current_col
    elif command == "down" and is_valid(current_row + 1, rows):
        return current_row + 1, current_col
    elif command == "left" and is_valid(current_col - 1, cols):
        return current_row, current_col - 1
    elif command == "right" and is_valid(current_col + 1, cols):
        return current_row, current_col + 1
    return None, None


rows, cols = [int(x) for x in input().split()]
matrix = []
boy_row = None
boy_col = None
start_boy_row = None
start_boy_col = None
address_row = None
address_col = None
pizza_row = None
pizza_col = None
is_pizza_taken = False
is_pizza_delivered = False

for i in range(rows):
    current_str = list(input())
    matrix.append(current_str)
    if "B" in current_str:
        boy_row = i
        boy_col = current_str.index("B")
        start_boy_row = i
        start_boy_col = current_str.index("B")
    if "A" in current_str:
        address_row = i
        address_col = current_str.index("A")
    if "P" in current_str:
        pizza_row = i
        pizza_col = current_str.index("P")

while not is_pizza_delivered:
    current_command = input()
    next_row, next_col = next_move(current_command, boy_row, boy_col)
    if next_row is None or next_col is None:
        print("The delivery is late. Order is canceled.")
        matrix[start_boy_row][start_boy_col] = " "
        break
    if matrix[next_row][next_col] == "*":
        continue
    if matrix[next_row][next_col] == "P":
        print("Pizza is collected. 10 minutes for delivery.")
        matrix[next_row][next_col] = "R"
        is_pizza_taken = True
    if matrix[next_row][next_col] == "A" and is_pizza_taken:
        print("Pizza is delivered on time! Next order...")
        is_pizza_delivered = True
        matrix[next_row][next_col] = "P"
    if matrix[next_row][next_col] == "-":
        matrix[next_row][next_col] = "."
    boy_row, boy_col = next_row, next_col


for i in matrix:
    print("".join(i))



