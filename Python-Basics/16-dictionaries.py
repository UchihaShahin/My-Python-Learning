# a customer can have different information like
# name, email, phone number, then we use dictionary

customer ={
    "name": "Shahin Alam",
    "age": 30,
    "is_verified": True
}
#to modify dictionary:
customer["name"]= "Md. Shahin Alam"
print(customer["name"])
#we can also use this
print(customer.get("age"))