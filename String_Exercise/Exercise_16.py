#Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
digit = 0

# for char in str1:
#     if char.isdigit():
        
res = "".join([char for char in str1 if char.isdigit()])

print(res)