#Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible
# by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

input_number= input("enter the number: ")

number = input_number.split(",")
#print(number)

item = [num for num in number if int(num,2)%5==0]
#print(item)

print(''.join(item))