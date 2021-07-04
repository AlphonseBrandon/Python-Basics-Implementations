from collections import Counter

# Creat a list

char_list = ['a', 'b', 'c', 'd']

# instead of this
custom_counter = {}

for char in char_list:
    if char not in char_list:
        custom_counter[char] = 1
    else:
        custom_counter[char] += 1
print(custom_counter)

print(Counter(char_list))

