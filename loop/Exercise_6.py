# Count the total number of digits in a number
number = int(input("enter the number!! "))
counter = 0

while number != 0:
    number //= 10
    counter += 1
print(counter)