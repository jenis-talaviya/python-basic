num = int(input("enter the number "))

res = 0
while num > 0:
    rem = num % 10
    res = rem + res*10
    num //= 10
print(res)