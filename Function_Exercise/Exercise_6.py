#Create a recursive function
def addition(num):
    if num:
        return num + addition(num - 1)
    else:
        return num

res = addition(10)
print(res)