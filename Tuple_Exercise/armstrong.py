num = int(input("enter the number "))
num1 = num

res = 0
while num > 0:
    rem = num%10
    res = rem*rem*rem + res
    num //= 10
    #print(res)
if num1 == res:
    print("number is armstrong")
else:
    print("number is not armstrong")