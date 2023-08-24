rows, cols = [int(x) for x in input().split()]
matrix = []

for _ in range(rows):
    matrix.append([k for k in input().split()])

command = input().split()
while command[0] != "END":
    if len(command) != 5 or command[0] != "swap":
        command = input().split()
        print("Invalid input!")
        continue
    first = int(command[1])
    second = int(command[2])
    third = int(command[3])
    fourth = int(command[4])
    try:
        matrix[first][second], matrix[third][fourth] = matrix[third][fourth], matrix[first][second]
        for i in matrix:
            for j in i:
                print(j, end=" ")
            print()
    except:
        print("Invalid input!")
    command = input().split()

