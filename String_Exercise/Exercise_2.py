#Append new string in the middle of a given string
s1 = "Ault"
s2 = "Kelly"

l1 = len(s1)

mid = l1//2
#print(mid)
res = s1[:mid] + s2 + s1[mid:]
print(res)