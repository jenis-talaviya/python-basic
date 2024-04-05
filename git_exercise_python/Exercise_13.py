#Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
#Suppose the following input is supplied to the program:

str1 = "Hello World!"

capital = 0
small = 0

for find_num in str1:
    if find_num.isupper():
        capital+=1
    elif find_num.islower():
        small += 1
        
print(f"capital word is {capital}")
print(f"lower word is {small}")