#Python program to find second largest number in a list

l1 = [10,20,4,45,99]
l1.sort()

print(l1[-2])

#OR

l1.remove(max(l1))

print(max(l1))