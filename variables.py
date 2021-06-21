# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

# Variable types

# int
x = 1
# float           
y = 2.5
# String
name = 'Alphonse'
# Bolean
is_cool = True

# Multiple assignment
x, y, name, is_cool = (1, 2.5, 'Alphonse', True)

# Basic math
a = x + y
print(a)

# Casting
x = str(x)
y = int(y)
z = float(y)

print(type(z), z)