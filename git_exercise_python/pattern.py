# 1
# AB
# 234
# CDEF
# 56789 print the pattern


num = 1
a = 65 

for i in range(1,6):
    for j in range(i):
        if i%2 == 1:
            print(num,end=" ")
            num += 1
        else:
            print(chr(a),end=" ")
            a+=1
            
    print()