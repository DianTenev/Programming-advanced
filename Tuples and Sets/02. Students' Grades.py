students = int(input())
dictionary = {}

for i in range(students):
    name, grade = input().split()
    if name not in dictionary:
        dictionary[name] = []
    dictionary[name].append(float(grade))

for key, value in dictionary.items():
    average = sum(value) / len(value)
    temporary = ' '.join([str(f"{current_grade:.2f}") for current_grade in value])
    print(f"{key} -> {temporary} (avg: {average:.2f})")


