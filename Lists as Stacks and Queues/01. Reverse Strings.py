text = input()
my_list = list(text)
result = ""

while my_list:
    removed_char = my_list.pop()
    result += removed_char

print(result)