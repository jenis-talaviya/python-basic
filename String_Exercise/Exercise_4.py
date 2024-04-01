#Arrange string characters such that lowercase letters should come first
str1 = "PyNaTive"

lower = []
upper = []

for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
str = "".join(lower + upper)
print(str)
        