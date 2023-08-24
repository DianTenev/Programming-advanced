import os


def save_extensions(directory_name):
    for file_name in os.listdir(directory_name):
        file = os.path.join(directory_name, file_name)

        if os.path.isfile(file):
            current_extension = file_name.split(".")[-1]
            if current_extension not in dictionary:
                dictionary[current_extension] = []

            dictionary[current_extension].append(file_name)
        elif os.path.isdir(file):
            save_extensions(file)


dictionary = {}
directory = input()
save_extensions(directory)

for key, value in dictionary.items():
    print(f".{key}")
    for i in value:
        print(f"{i}")
