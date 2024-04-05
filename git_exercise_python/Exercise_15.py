# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:

number = input('enter the number:')

#print(number)

num = [i for i in number.split(',') if int(i)%2!=0]

print(','.join(num))