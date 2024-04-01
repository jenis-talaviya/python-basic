num = 7536

result = 0

while num > 0:
    rem = num%10
    #result = rem+result*10
    num //= 10
    print(rem,end=" ")