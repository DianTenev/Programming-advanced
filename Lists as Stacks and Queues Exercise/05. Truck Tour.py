from collections import deque

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))])

pumps_data_copy = pumps_data.copy()
gas = 0
pump = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft()
    gas += petrol

    if gas >= distance:
        gas -= distance
    else:
        pumps_data.rotate(-1)
        pumps_data_copy = pumps_data.copy()
        pump += 1
        gas = 0

print(pump)



