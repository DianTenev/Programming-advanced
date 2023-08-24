from collections import deque


monsters_armor = deque([int(x) for x in input().split(",")])
soldier_striking_impacts = [int(x) for x in input().split(",")]
monsters_killed = 0

while True:
    if not monsters_armor and not soldier_striking_impacts:
        print("All monsters have been killed!")
        print("The soldier has been defeated.")
        break
    if not monsters_armor:
        print("All monsters have been killed!")
        break
    if not soldier_striking_impacts:
        print("The soldier has been defeated.")
        break

    current_monster_armor = monsters_armor[0]
    current_soldier_striking_impact = soldier_striking_impacts[-1]

    if current_soldier_striking_impact >= current_monster_armor:
        popped_armor = monsters_armor.popleft()
        soldier_striking_impacts[-1] -= popped_armor
        popped_impact = soldier_striking_impacts.pop(-1)
        if soldier_striking_impacts:
            soldier_striking_impacts[-1] += popped_impact
        else:
            if popped_impact > 0:
                soldier_striking_impacts.append(popped_impact)
        monsters_killed += 1

    elif current_soldier_striking_impact < current_monster_armor:
        monsters_armor[0] -= current_soldier_striking_impact
        soldier_striking_impacts.pop(-1)
        monsters_armor.rotate(-1)

print(f"Total monsters killed: {monsters_killed}")