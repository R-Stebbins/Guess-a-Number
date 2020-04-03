# Guess the number game

import random

# Guess count starts at 0
guess_count = 0
number = random.randint(1, 20)

print("Hello! What is your name?")
name = input()
print("Hi " + name + "!\n I am thinking of a number between 1 and 20.")

# user gets 7 guesses to get the right answer
while guess_count < 7:
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    guess_count += 1

    if guess < number:
        print("Guess a little higher")

    if guess > number:
        print("Guess a little lower!")

    if guess == number:
        break

if guess == number:
    guess_count = str(guess_count)
    print("Good job, " + name + "! You guessed my number in " + guess_count + " guesses!")

if guess != number:
    number = str(number)
    print("Sorry. The number I was thinking of was " + number)
