import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# testing
print(f'the solution is {chosen_word}')

guess = input("Guess a later").lower()

display = []

for _ in range(len(chosen_word)):
    display += "_"
print(display)

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
    