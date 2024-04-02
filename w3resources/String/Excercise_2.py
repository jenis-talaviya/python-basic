#Write a Python program to count the number of characters (character frequency) in a string.

str1 = "google.com"

dict = {}

for num in str1:
    
    keys = dict.keys()
    
    if num in keys:
        dict[num] += 1
    else:
        dict[num] = 1
print(dict)
