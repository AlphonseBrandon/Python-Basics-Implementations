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

    # Extend class
    class Customer(User):

        # Constructor
        def __init__(self, name, email, age):
            User.__init__(self, name, email, age) #Called proper parent class constructor to make this as proper child inehriting all methods.
            self.name = name
            self.email = email
            self.age = age
            self.balance = 0

        def set_balance(self, balance):
            self.balance - balance

        def greeting(self):
            return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

        # init user object
        brad = User('Alphonse Brandon', 'alphonse.brand@gmail.com', 90)
        #init customer object
        janet = Customer('Brandon Alphonse', 'alphonse.brand@gmail.com', 80)

        janet.set_balance(600) # create function
        def sayHello(name='Brand'):
            print(f'Hello {name}')
        print(janet.greeting())

        brad.has_birthday()
        print(brad.greeting())

        # Encapsulation 
        brad.print_encap()
        brad._private = 800 # changing for brad
        brad.print_encap()

        # Method inherited from parent
        janet.print_encap() # changing the variable for brad doesn't affect janets variable --> Encapsulation
        janet._private = 500
        janet.print_encap()

        #Similary changing janet's doesn't affect brad's variable.
        brad.print_encap()