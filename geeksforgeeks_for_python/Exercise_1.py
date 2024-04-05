#Python program to interchange first and last elements in a list
list = [12,35,9,56,24]

list[0], list[-1] = list[-1], list[0]

print(list)

#OR

def swaplist(newlist):
    size = len(newlist)
    
    temp = newlist[0]
    newlist[0] = newlist[size-1]
    newlist[size - 1] = temp
    
    return newlist

newlist = [12,35,9,56,24]
print(swaplist(newlist))