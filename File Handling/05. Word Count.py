import re

words_file = open("words.txt")
text_file = open("text.txt")
dictionary = {}

searched_words = words_file.readline().split()
text = text_file.read().lower()
text = re.sub(r"[^\w+\s]", "", text).split()

for word in searched_words:
    times = text.count(word)
    dictionary[word] = times

for key, value in sorted(dictionary.items(), key=lambda x: x[1], reverse=True):
    print(f"{key} - {value}")
