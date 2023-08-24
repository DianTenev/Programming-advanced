import math
from collections import deque

string = deque(input().split())
lst = []
result_sum = 0
result_mul = 1
first_time = False

while string:
    current_number = string[0]
    if current_number == "*":
        for i in lst:
            result_mul *= int(i)
        lst.clear()
        result_sum = result_mul
        string.popleft()
        first_time = True
    elif current_number == "/":
        for i in lst:
            if not first_time:
                result_mul = int(i)
                first_time = True
            else:
                result_mul = result_mul // math.floor(int(i))
        lst.clear()
        result_sum = result_mul
        string.popleft()
    elif current_number == "+":
        for i in lst:
            result_sum += int(i)
        lst.clear()
        result_mul = result_sum
        string.popleft()
        first_time = True
    elif current_number == "-":
        for i in lst:
            if not first_time:
                result_sum = int(i)
                first_time = True
            else:
                result_sum -= int(i)
        lst.clear()
        result_mul = result_sum
        string.popleft()
    else:
        lst.append(string.popleft())

print(result_sum)




