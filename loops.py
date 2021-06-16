# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['Brandon', 'Alphonse', 'John', 'Mary']

#Simple 'for' loop

for person in people:
    print(f'current person: {person}')

# Break
for person in people:
    if person == 'Brandon':
        break
    print(f'current person: {person}')

# Continue 
for person in person:
    if person == 'Brandon':
        continue
    print(f'current person: {person}')

# range
for i in range(len(people)):
    print(people[i])

for i in range(0, 11):
    print(f'number: {i}')




# While loops execute a set of statements as long as a condition is true.
