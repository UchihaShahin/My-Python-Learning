# so here we will learn about type conversion of python

# ?first have a birth year variable to store our birthday

birth_year= input("what is your birth year? ")

# !so in the bg it will look like '2001' which is a lot different from 2001 

# ?now we will guess the age with this simple calculation:

# --------- this is the example before type conversion ----------#
# age = 2021 -birth_year

# print(age)

#-----------------------------------------------------------------


# so when we try to guess the year it is showing type error, why?
# because we can't subtract a string from int...here birth_year is string and 2021 is integar
# so we need to define that which one is string and which one is integar

#? now we will change the string type to integar type in the next line,

age = 2021 - int(birth_year)
print (age)

# let's see the type of our variables

print (type(birth_year))   #string
print (type(age))   #int