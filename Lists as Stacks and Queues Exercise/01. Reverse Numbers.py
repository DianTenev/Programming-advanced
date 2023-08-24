my_list = input().split()
new_list = my_list.copy()
for i in my_list:
    removed_number = new_list.pop()
    print(removed_number, end=" ")