commands = int(input())
lot = set()

for i in range(commands):
    direction, car = input().split(", ")
    if direction == "IN":
        lot.add(car)
    elif direction == "OUT":
        lot.remove(car)

if len(lot) == 0:
    print("Parking Lot is Empty")
else:
    for j in lot:
        print(j)