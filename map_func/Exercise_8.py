#Convert a list of integers, tuple of integers in a list of strings

nums_list = [1, 2, 3, 4]
nums_tuple = (0, 1, 2, 3)

res = list(map(str,nums_list))

res1 =tuple(map(str,nums_tuple))

print(res)
print(res1)