# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules
import datetime
from datetime import date
import time
from time import time


# Pip module
import camelcase
from camelcase import Camelcase

# Import custorm module
import validator
from validator import validate_email

# today = datetime.date.today()
today = date.today()
timestamp = time()

c = Camelcase()

# print (c.hump('hello there Alphonse'))

email = 'alphonse.brand@gmail.com'
if validate_email(email):
    print('email is valid')
else:
    print('Email is invalid')
