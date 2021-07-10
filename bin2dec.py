# convert from dec to bin

n = input(" enter a number to be converted")

number = int(n)
bin = []
if number > 1:
    remainder = number % 2
    
print(remainder)
bin(number)
    
print(bin[remainder])

