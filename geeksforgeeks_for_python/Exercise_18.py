#Python program to print positive numbers in a list

list1 = [-10, 21, -4, -45, -66, 93]

for num in list1:
    if num > 0:
        print(num,end=" ")
        
#OR list comprehension

pos_no = [num for num in list1 if num >= 0]

print("\npositive number in the list: ",*pos_no)