#Concatenate two lists index-wise
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]

for i,j in zip(list1,list2):
    print(i+j,end=" ")
    
#OR
list3 = [i + j for i, j in zip(list1, list2)]
print(list3)