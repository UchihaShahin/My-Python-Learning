# we will do a weight converter from kg to pound (vice-versa)

weight=int(input("Weight: "))

unit= input("(L)bs or (K)g: ")

if unit.upper() == 'L':
    converted= (weight*0.45)
    print(f"you are {converted} kilos")

elif unit.upper() == 'K':
    converted= (weight/0.45)
    print(f"you are {converted} pound")

else:
    print("please enter the right value and try again")