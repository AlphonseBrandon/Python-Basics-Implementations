from collections import Counter

char_list = ["1", "2", "3"]

custom_char = {}

for char in char_list:
    if char not in custom_char:
        custom_char[char] = 1
    else:
        custom_char[char] += 1

print(custom_char)


