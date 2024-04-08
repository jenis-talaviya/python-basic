#Square the elements of a list using map()
def add(num):
    return num *num

nums = [4,5,2,9]

result = map(add,nums)

print(list(result))