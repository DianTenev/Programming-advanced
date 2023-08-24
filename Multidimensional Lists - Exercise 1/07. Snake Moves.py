from collections import deque

rows, cols = [int(x) for x in input().split()]
word = input()

word_copy = deque(word)

for i in range(rows):
    while len(word_copy) < cols:
        word_copy.extend(word)

    if i % 2 == 0:
        print(*[word_copy.popleft() for _ in range(cols)], sep="")
    else:
        print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")


