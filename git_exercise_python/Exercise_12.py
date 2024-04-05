#Write a program that accepts a sentence and calculate the number of letters and digits.
#Suppose the following input is supplied to the program:

str1 = "hello world! 123"

letter = 0
num = 0

for i in str1:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        num += 1

print(f"letter is {letter}")
print(f"digit is {num}")