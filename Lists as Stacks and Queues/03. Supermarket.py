from collections import deque

collection = deque()

command = input()
while command != "End":
    while command != "Paid":
        if command == "End":
            break
        collection.append(command)
        command = input()
    if command == "End":
        break
    while collection:
        removed_person = collection.popleft()
        print(removed_person)

    command = input()

print(f"{len(collection)} people remaining.")
