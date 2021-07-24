import random
import string

def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation


    # selecting 1 lowercase
    for i in range(2):
        password = random.choice(string.ascii_lowercase)


    # Selecting 1 uppercase
    for i in range(2):
        password += random.choice(string.ascii_uppercase)


    # selecting 1 digit
    for i in range(2):
        password += random.choice(string.digits)
    

    # selecting 1 special symbol
    for i in range(2):
        password += random.choice(string.punctuation)
    

    #place password in a list
    password_list = list(password)


    # Shuffle all characters
    random.SystemRandom().shuffle(password_list)

    password = ''.join(password_list)

    return password


print("First random password is", get_random_password())


# second random password
print("Second random password is",get_random_password())