from collections import deque


tools = deque(int(x) for x in input().split(" "))
substances = [int(x) for x in input().split(" ")]
challenges = [int(x) for x in input().split(" ")]

while True:
    if challenges:
        if not substances or not challenges:
            print("Harry is lost in the temple. Oblivion awaits him.")
            break

    if not challenges:
        print("Harry found an ostracon, which is dated to the 6th century BCE.")
        break

    if tools[0] * substances[-1] in challenges:
        popped_tool = tools.popleft()
        popped_substance = substances.pop(-1)
        challenges.remove(popped_tool * popped_substance)
    else:
        tools[0] += 1
        tools.rotate(-1)
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.remove(substances[-1])


if tools:
    print(f"Tools: {', '.join([str(x) for x in tools])}")

if substances:
    print(f"Substances: {', '.join([str(x) for x in substances])}")

if challenges:
    print(f"Challenges: {', '.join([str(x) for x in challenges])}")






