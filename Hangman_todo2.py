import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# testing
print(f'the solution is {chosen_word}')

guess = input("Guess a later").lower()

display = []
word_lenth = len(chosen_word)

for _ in range(len(word_lenth)):
    display += "_"
print(display)

for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
    
print(display)