# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Read more about dictionaries at https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Create dict
person = {
    'first_name': 'Alphonse',
    'last_name': 'Brandon',
    'Age': 30
    'role': 'Data scie'
}
print(person)

# Using constructors
person2 = dict(first_name='Alp', last_name='brand', age='80')
print(person2)

# Get Value
print(person['first_name'])
print(person['last_name'])

# Add key or value
person['phone'] = '123-324-133'

# Get dict keys
print(person.keys())

# Get dict items
print(person.items())

# Copy dict
person2 = person.copy()
print(person2)

# Remove  item
del(person['Age'])
person.pop('phone')
print(person)


# Clear 
person.clear()
print(person)

# Get length
print(len(person2))

# List of dict
people = [
    {'name': 'Alphonse', 'age': 40},
    {'name': 'Brandon', 'Age': 40}
]
print(people)

# Dictionary end