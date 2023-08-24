with open("text.txt") as file:
    lines = 1
    chars = ["-", ",", ".", "!", "?", "'"]
    output_file = open("output", "w")
    for line in file.readlines():
        letters, punctuation = 0, 0
        for ch in line:
            if ch.isalpha():
                letters += 1
            elif ch in chars:
                punctuation += 1

        output_file.write(f"Line {lines}: {line[:-1]} ({letters})({punctuation})\n")
        lines += 1
    output_file.close()

