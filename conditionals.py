# If/ Else conditions are used to decide to do something based on something being true or false

x = 21
y = 20

# Comparison Operators (==, !=, >, <, >=, <=) - Used to compare values

# Simple if
if x > y:
    print(f'{x} is greater than {y}')

# if/else
if x > y:
    print(f'{x} is greater than {y}')
else:
    print(f'{y} is greater than {x}')

#elif
if x > y:
    print(f'{x} is equall to {y}')
elif x == y:
    print (f'{x} is equal to {y}')
else:
    print(f'{y} is greater than {x}')
# Logical operators (and, or, not) - Used to combine conditional statements
# and
if x > 2 and x <= 10:
    print(f'{x} is greater than 2 and less than 10')

# or
if x > 2 or x <= 10:
    print(f'{x} is greater than 2 and less than or eqall to 10')

#not
if not(x == y):
    print(f'{x} is not equall to {y}')

# Membership Operators (in, not in) - Membership operators are used to test if a sequence is presented in an object:

numbers = [1,2,3,4,5]

# in
if x in numbers:
    print(x in numbers)

# not in
if x not in numbers:
    print(x not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
if x is y:
    print(x is y)

#not
if x is not y:
    print(x is not y)