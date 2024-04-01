#Create a new string made of the first, middle, and last characters of each input string
s1 = "America"
s2 = "Japan"

res = s1[0] + s2[0] + s1[3] + s2[2:]
print(res)