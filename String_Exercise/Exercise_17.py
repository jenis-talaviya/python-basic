#Find words with both alphabets and numbers
str1 = "Emma25 is Data scientist50 and AI Expert"

digit = 0
alpha = 0

for char in str1:
    if char.isdigit():
        digit.append(char)
    else:
        alpha.append(char)
print(digit)
print(char)