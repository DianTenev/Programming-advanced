with open("text.txt") as file:
    lines = 0
    chars = ["-", ",", ".", "!", "?"]
    for line in file.readlines():
        if lines % 2 != 0:
            lines += 1
            continue
        for ch in chars:
            line = line.replace(ch, "@")
        line_as_list = line.split()
        line_as_list.reverse()
        print(" ".join(line_as_list))
        lines += 1

