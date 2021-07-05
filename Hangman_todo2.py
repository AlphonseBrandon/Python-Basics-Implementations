import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# testing
print(f'the solution is {chosen_word}')
display = []

for letter in chosen_word:
    display += "_"

guess = input("Guess a later").lower()
