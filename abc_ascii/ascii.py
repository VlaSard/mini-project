"""ascii.py - text to pseudo graphic converter"""

import json

# read the symbol dictionary
with open('ascii.json', 'r', encoding='utf-8') as file_ascii_chars:
    ascii_chars = json.load(file_ascii_chars)

text = input("Enter the word for conversion: ").lower()

text_line = []

# create a list of characters from the pseudo-graphics for the word
for index in range(3):
    line = ["# "]

    for char in text:
        line.append(ascii_chars[char][index])
    text_line.append(line)

# record the result in a file
with open('ascii.txt', 'a', encoding='utf-8') as file_ascii_text:
    for i in text_line:
        print(*i, sep=' ', file=file_ascii_text)
    print(file=file_ascii_text)

# output the result to the console
for char_line in text_line:
    print(*char_line, sep=' ')
