parent = input()
stack = []

for i in range(len(parent)):
    if parent[i] == "(":
        stack.append(i)
    elif parent[i] == ")":
        removed_index = stack.pop()
        print(parent[removed_index:i + 1])

