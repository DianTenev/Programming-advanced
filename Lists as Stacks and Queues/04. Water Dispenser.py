from collections import deque

collection = deque()
liters = int(input())

name = input()
while name != "Start":
    collection.append(name)
    name = input()

command = input().split()
while command[0] != "End":
    if len(command) == 1:
        removed_person = collection.popleft()
        if liters >= int(command[0]):
            liters -= int(command[0])
            print(f"{removed_person} got water")
        else:
            print(f"{removed_person} must wait")
    else:
        liters += int(command[1])
    command = input().split()

print(f"{liters} liters left")