# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:

n = 5

a = 9
sum = 0

for i in range(0,n):
    print(a,end="+")
    sum += a
    a = a *10 + 9
print(sum)