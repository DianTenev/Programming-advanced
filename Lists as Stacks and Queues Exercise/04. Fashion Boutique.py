stack = input().split()
rack_capacity = int(input())
racks = 0
temporary = 0

for i in range(len(stack) - 1, -1, -1):
    current_cloth = int(stack[i])
    if current_cloth + temporary == rack_capacity:
        racks += 1
        temporary = 0
    elif current_cloth + temporary > rack_capacity:
        racks += 1
        temporary = current_cloth
    else:
        temporary += current_cloth

if temporary == 0:
    print(racks)
else:
    print(racks + 1)


