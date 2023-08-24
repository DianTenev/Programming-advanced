queries = int(input())
stack = []

for i in range(queries):
    query = input().split()
    if len(query) > 1:
        number = int(query[1])
        stack.append(number)
    elif len(query) == 1:
        command = query[0]
        if command == "2":
            if len(stack) > 0:
                popped_number = stack.pop()
        elif command == "3":
            if len(stack) > 0:
                print(max(stack))
        elif command == "4":
            if len(stack) > 0:
                print(min(stack))

stack.reverse()
result = ", ".join(map(str, stack))
print(result)