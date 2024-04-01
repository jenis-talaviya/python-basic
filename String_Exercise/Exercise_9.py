#Calculate the sum and average of the digits present in a string
str1 = "PYnative29@#8496"

digit = 0
sum = 0

for char in str1:
    if char.isdigit():
        sum += int(char)
        digit += 1

avg = sum/digit
print(f"sum is {sum} average is {avg}")