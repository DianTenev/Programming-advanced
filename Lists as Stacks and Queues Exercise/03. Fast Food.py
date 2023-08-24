from collections import deque

food_for_the_day = int(input())
orders = deque(int(x) for x in input().split())
print(max(orders))


while orders:
    if orders[0] > food_for_the_day:
        orders_left = " ".join(map(str, orders))
        print(f"Orders left: {orders_left}")
        break
    else:
        food_for_the_day -= orders[0]
        removed_order = orders.popleft()
else:
    print("Orders complete")


