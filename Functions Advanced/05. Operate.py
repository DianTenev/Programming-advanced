from functools import reduce


def operate(operator, *args):
    # def sum_nums():
    #     return sum(args)
    #
    # def subtract():
    #     result = 0
    #     for i in args:
    #         result -= i
    #     return result
    #
    # def multiply():
    #     result = 1
    #     for i in args:
    #         result *= i
    #     return result
    #
    # def divide():
    #     result = args[0]
    #     for i in args:
    #         if i == args[0]:
    #             continue
    #         result /= i
    #     return result

    if operator == "+":
        return reduce(lambda a, b: a + b, args)
    elif operator == "-":
        return reduce(lambda a, b: a - b, args)
    elif operator == "*":
        return reduce(lambda a, b: a * b, args)
    elif operator == "/":
        return reduce(lambda a, b: a / b, args)


print(operate("*", 3, 4))