current_string = input().split("|")
new_list = []
for i in current_string:
    new_list.append(i.split())


for j in range(len(new_list) - 1, -1, -1):
    for x in new_list[j]:
        print(x, end=" ")