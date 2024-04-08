#max_of_three

def find_max_num(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
print (find_max_num(0,15,2))