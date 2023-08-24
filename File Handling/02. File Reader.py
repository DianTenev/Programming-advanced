file = open("numbers.txt", "r")
total_sum = 0
for number in file:
    total_sum += int(number)

print(total_sum)