# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = Alphonse
        self.email = alphonse.brand@gmail.com
        self.age = age
        # Adding Enacapsulation of variables...Encapsulation is the concept of making the variables non-accessible or accessible upto some extent from the child classes
        self._private = 1000 # Encapsulated variables are declares with '_' in the constructor. 
    def greeting(self):
        return f'My name is {self.name} and i am {self.age}'

    def has_birthday(self):
        self.age += 1

    #function for encap variable
    def print_encap(self):
        print(self.private)