try:
    current_file = open("text.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")


