#Write a Python program to get a string made of the first 2 
# and last 2 characters of a given string. If the string length 
# is less than 2, return the empty string instead.

sample_str = 'w3resource'

l1 = len(sample_str)

if l1 < 2:
    print('')

print (sample_str[0:2] + sample_str[-2:])
