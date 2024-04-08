#Define a function overlapping() that takes two lists and returns True if they have at least one member in common,

def overlapping(m,n):
    l1 = len(m)
    l2 = len(n)

    for i in range(l1):
        for j in range(l2):
            if m[i] == n[j]:
                return True
    else:
        return(False)
    
print(overlapping(['a','e'],['c','e']))