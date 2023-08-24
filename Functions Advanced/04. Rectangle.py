def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    def area():
        return f"Rectangle area: {length * width}"

    def perimeter():
        return f"Rectangle perimeter: {2 * (length + width)}"
    return area() + "\n" + perimeter()


print(rectangle(2, 10))
