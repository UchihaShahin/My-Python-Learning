# Here we will talk about formatted strings

# I want to print a string like this:
# ! Shahin [Alam] is a Human

# lets declare two variables...

first_name = 'Shahin'
last_name = 'Alam'

# we will first use Concatenation String to print this

message= first_name + ' [' + last_name + '] is a Human' 
print(message)

# now we will use string formatter to make this more easier

msg = f'{first_name} [{last_name}] is a Human'
print(msg)