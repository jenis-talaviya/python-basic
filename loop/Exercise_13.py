num = int(input("enter the number!! "))

fact = 1

if num <0:
    print("negative number is not valid!!")
elif num == 0:
    print("the factorial of 0 is 0")
else:
    for num1 in range(1,num+1,1):
        fact = fact * num1
    print(fact)