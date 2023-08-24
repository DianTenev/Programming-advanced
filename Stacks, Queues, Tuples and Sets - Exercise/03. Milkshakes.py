from collections import deque

chocolates = [int(x) for x in input().split(", ")]
milk = deque(map(int, input().split(", ")))
milkshakes = 0

while milkshakes != 5:
    if not chocolates or not milk:
        print("Not enough milkshakes.")
        break
    if chocolates[-1] <= 0:
        chocolates.pop()
        if milk[0] > 0:
            continue
    if milk[0] <= 0:
        milk.popleft()
        continue
    if chocolates[-1] == milk[0]:
        milkshakes += 1
        chocolates.pop()
        milk.popleft()
    else:
        milk.rotate(-1)
        chocolates[-1] -= 5
else:
    print("Great! You made all the chocolate milkshakes needed!")

if chocolates:
    print(f"Chocolate: {', '.join(map(str, chocolates))}")
else:
    print("Chocolate: empty")

if milk:
    print(f"Milk: {', '.join(map(str, milk))}")
else:
    print("Milk: empty")

