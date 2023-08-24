def even_odd(*args):
    command = args[-1]
    even_list = [int(args[x]) for x in range(len(args) - 1) if args[x] % 2 == 0]
    odd_list = [int(args[x]) for x in range(len(args) - 1) if args[x] % 2 != 0]
    if command == "even":
        return even_list
    else:
        return odd_list


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "even"))
