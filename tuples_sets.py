# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create turple
fruits = ('Apples', 'Oranges', 'Grapes') 
print(fruits)

# Single value needs tailing comma
fruits2 = ('Apples',)
print(fruits2)
# Using a constructor
fruits3 = tuple('Apples',)
print(fruits3)

# Get value
print(fruits[0])

# Can't change value
#fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get lenth
print(len(fruits))

# A Set is a collection which is unordered and unindexed. No duplicate members.
# Create set

fruits_set = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruits_set)
