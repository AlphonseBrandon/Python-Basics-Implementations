from collections import Counter



a = input("string")

print(len(a))



for letter in a:
    print(letter)

l = list(a)
i = 0
print(l)

while ' ' in a:
    i += 1
    break
print(i)

