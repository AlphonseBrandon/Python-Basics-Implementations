# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w')

# Get some info
print('Name:', myFile.name)
print('Is closed :', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('I am an ML engineer')
myFile.write('Alphonse Brandon')
myFile.close() 

# Append to a file
myFile = open('myfile.tex', 'a')
myFile.write('I am also a datascientist')
myFile.close()

# Read to file
myFile = open('myfile.text', 'r+')
text = myFile.read(100)
print(text)