import random

guess_number = int(input("Enter a number between 1-5: "))

random_number = random.randint(1, 5)

if guess_number == random_number:
    print("you have won")
else:
    print("you have lost")
    print("The random number was: ", random_number)