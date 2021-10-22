numbers =[1,2,3,4,5,6]

# add the number in the last
numbers.append(12)
print(numbers)

# insert a number to the specific index (no replacing)
numbers.insert(0,10)
print(numbers)

numbers.remove(12)
print(numbers)

# numbers.clear()
# print(numbers)

#clear the last inserted value only
numbers.pop()
print(numbers)

# print the specific index
print(numbers.index(1))

#check if the value is in the list
print(10 in numbers)

#count the repeatation of a number
print (numbers.count(1))

#to sort a list
numbers.sort()
print(numbers)

#to reverse a list
numbers.reverse()
print(numbers)

#to copy a list
# this list won;t change if we make changes to the main list
copy_list = numbers.copy()
print(copy_list)


#write a program to remove the duplicates from a list

new_list = [1,1,1,2,3,4,5,5,6]
unique =[]

for number in new_list:
    if number not in unique:
        unique.append(number)

print(unique)