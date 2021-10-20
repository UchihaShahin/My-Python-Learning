secret_number = ((6*6)+(5*5*5)+(4*4*4*4)+(3*3*3*3*3)+(2*2*2*2*2*2)-(3*3*3+2*2))
while (1):
    guess= int(input("Enter a number between 1 to 1000: "))

    if guess <1 or guess >1000:
        print("Invalid input")

    elif 1 <= guess <= 100:
        print("You're far far far far away.\nAdd some more numbers I recommend +10")

    elif 101 <= guess <= 200:
        print("You're far far far far away.\nAdd some more numbers I recommend +20.\n")

    elif 201 <= guess <= 300:
        print("You're far far far away.\nAdd some more numbers I recommend +30.\n")

    elif 301 <= guess <= 400:
        print("You're far far far away.\nAdd some more numbers I recommend +40.\n")

    elif 401 <= guess <= 500:
        print("You're far far away.\nAdd some more numbers I recommend +50.\n")

    elif 501 <= guess <= 600:
        print("You're far away.\nAdd some more numbers I recommend +60.\n")

    elif 601 <= guess <= 650:
        print("You're close.\nAdd some more numbers I recommend +40.\n")

    elif 651 <= guess <= 710 and guess != secret_number:
        print("A little bit more.\nYour answer is here: (6^2+5^3+4^4+3^5+2^6-3^3-2^2)\nLets calculate it.\n")

    elif 711 <= guess <= 750:
        print("Ohh!!! you cross the correct answer.\nYour answer is here: (6^2+5^3+4^4+3^5+2^6-3^3-2^2)\nLets calculate it.\n")

    elif 751 <= guess <= 850:
        print("You're far far away.\nSubtract some numbers. I recommend -40.\n")


    elif 851 <= guess <= 950:
        print("You're far far away.\nSubtract some numbers. I recommend -50.\n")

    elif 951 <= guess <= 1000:
         print("You're far far away.\nSubtract some numbers. I recommend -80.\n")

    elif guess == secret_number:
        print("Congrats!!! Your guess is correct\n")
        break