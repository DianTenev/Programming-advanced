number = int(input())
longest = set()

for i in range(number):
    text = input().split("-")
    first_interval = text[0].split(",")
    second_interval = text[1].split(",")
    first_set = set(x for x in range(int(first_interval[0]), int(first_interval[1]) + 1))
    second_set = set(x for x in range(int(second_interval[0]), int(second_interval[1]) + 1))
    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest):
        longest = intersection

print(f"Longest intersection is {sorted(longest)} with length {len(longest)}")


