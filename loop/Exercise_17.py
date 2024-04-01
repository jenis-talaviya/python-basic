#Python for loop and if else Exercises [10 Exercise Programs

n = int(input("enter the number!!! "))

num = 2

sum = 0

for i in range(1,n+1):
    print(num,end=" ")
    sum = sum +  num
    
    num = num * 10 + 2
print(sum)