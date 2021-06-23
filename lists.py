# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Using a constructor
numbers2 = list((1, 2, 3, 4, 5))
print(numbers2)

# Get a value
print(fruits[1])

# Get the last value
print(fruits[-1])

# Get length
print(len(fruits))

# Append to list 
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Change value
fruits[0] = 'Blueberries'
print(fruits)