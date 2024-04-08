#Define a function sum() and a function multiply() that sums and multiplies 
#(respectively)  all the numbers in a list of numbers. For example, sum([1, 2, 3, 4])

def sum1(x):
    c= 0
    for i in x:
        c += i
    return c

def sum2(x):
    c = 1
    for i in x:
        c *= i
    return c

print("sum is: ",sum1([1,2,3,4,5]))
print("multuply is: ",sum2([1,2,3,4,5]))