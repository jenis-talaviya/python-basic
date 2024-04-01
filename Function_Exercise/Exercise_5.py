#Create an inner function to calculate the addition in the following way
def outer_fun(a,b):
    def inner_fun(a,b):
        return a+b
    add = inner_fun(a,b)
    return add + 5

res = outer_fun(5,6)
print(res)