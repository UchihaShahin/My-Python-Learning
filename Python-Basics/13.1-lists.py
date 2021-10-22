# names =['shahin0','shahin1','shahin2','shahin3','shahin4','shahin5']
# #print a range
# print(names[2:4])
#
# #print from end
# print(names[-1])

#write a program to find the largest number in a list

list = [10, 20, 30, 40, 50, 60]
max = list[0]

for number in list:
    if number>max:
        max=number

print(max)
