#Change a given string to a new string where the first and last chars have been exchanged
str1 = 'abcd'

str = str1[-1] + str1[1:3] + str1[0]

print(str)
