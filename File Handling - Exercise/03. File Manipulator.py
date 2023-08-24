import os

command = input()
while command != "End":
    command = command.split("-")
    if command[0] == "Create":
        current_file = open(command[1], "w")
        current_file.close()
    elif command[0] == "Add":
        current_file = open(command[1], "a")
        current_file.write(f"{command[2]}\n")
        current_file.close()
    elif command[0] == "Replace":
        try:
            with open(command[1], "r+") as file:
                text = file.read()
                text = text.replace(command[2], command[3])
                file.seek(0)
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")
    elif command[0] == "Delete":
        try:
            os.remove(command[1])
        except FileNotFoundError:
            print("An error occurred")
    command = input()



