guests = int(input())
vip = set()
regular = set()
removes = 0
temporary = []

for i in range(guests):
    current_code = input()
    if current_code[0].isdigit():
        vip.add(current_code)
    else:
        regular.add(current_code)

command = input()
while command != "END":
    if command[0].isdigit():
        vip.remove(command)
    else:
        regular.remove(command)
    removes += 1
    command = input()

print(guests - removes)

# for k in vip:
#     temporary.append(k)
# temporary = sorted(temporary)
# print("\n".join(temporary))
# temporary.clear()
#
# for j in regular:
#     temporary.append(j)
# temporary = sorted(temporary)
# print("\n".join(temporary))

print(*sorted(vip), sep="\n")
print(*sorted(regular), sep="\n")