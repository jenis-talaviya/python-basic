#Return multiple values from a function
def calculate(a,b):
    add = a+b
    sub = a-b
    return add,sub

res = calculate(40,10)
print(res)