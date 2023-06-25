import random

def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value, max_value)

print("Welcome to the Dice Roller!")

while True:
    roll = input("Press r to roll the dice (or 'q' to quit): ")
    if roll.lower() == 'q':
        print("Goodbye!")
        break
    
    if roll.lower() =='r':
        dice_result = roll_dice()
        print("You rolled:", dice_result)
