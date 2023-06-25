import random

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)
a = 0
chance = 5
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("You have only 5 chances...\n")
while a < chance:
    # Prompt the user to enter a guess
    guess = int(input("Take a guess: "))
    a += 1
    # Compare the guess with the target number
    if guess < target_number:
        print("Too low!")
    elif guess > target_number:
        print("Too high!")
    else:
        print("Congratulations! You guessed the correct number!")
        break

    if a == chance:
        print("You have Lost")
    else:
        print("You have", chance - a, "guesses left!")
