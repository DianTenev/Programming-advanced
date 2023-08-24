from collections import deque

children = deque(input().split())
toss = int(input())

while len(children) != 1:
    children.rotate(-toss + 1)
    removed_children = children.popleft()
    print(f"Removed {removed_children}")

print(f"Last is {children[0]}")