secret_number = 9
guess_count = 0
guess_limit = 3
life = 2

while guess_count < guess_limit:
    guess = int(input("Enter your Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("Your Guess is Correct")
    elif guess != secret_number:
        if life == 0:
            break
        print(f'you can try {life} more time ')
        life -= 1