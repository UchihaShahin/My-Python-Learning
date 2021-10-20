#value = input("Type help for menu: ")
# if value.upper() == 'HELP':
#     print("start - to start the car\n"
#           "stop - to stop the car\n"
#           "quit - to exit\n")

while (1):
    user_input=input("What do you want? ").upper()
    if user_input == 'HELP':
        print("start - to start the car\n"
              "stop - to stop the car\n"
              "quit - to exit\n")
    elif user_input == 'START':
        print("Car started ready to go\n")

    elif user_input == 'STOP':
        print("Car Stopped\n")

    elif user_input == 'QUIT':
        break

    else:
        print("I cant understand the command\n")