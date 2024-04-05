#Python program to find smallest number in a list
list1 = [10,20,7,4]

list1.sort()

print(list1[0])

#Min using
print(min(list1))

#OR Dynamicaly

list2 = []

num = int(input("enter the number of element in list: "))

for i in range(1,num+1):
    ele=int(input("enter element: "))
    list2.append(ele)

print(min(list2))