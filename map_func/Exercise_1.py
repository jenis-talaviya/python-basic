#Write a Python program to triple all numbers in a given list of integers. Use Python map.

nums = (1,2,3,4,5,6,7)

result = map(lambda x:x+x+x,nums)

print(list(result))