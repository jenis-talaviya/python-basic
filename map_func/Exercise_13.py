def compair_pair(num1,num2):
    return num1 == num2
    
def same_pair(num3,num4):
    compa_res = sum(map(compair_pair,num3,num4))
    return compair_pair

l1 = [1, 2, 3, 4, 5, 6, 7, 8]
l2 = [2, 2, 3, 1, 2, 6, 7, 9]

print("same pair is: ",compair_pair(l1,l2))


from operator import eq

def count_pair(li1,li2):
    result = sum(map(eq,li1,li2))
    return result


print(count_pair(l1,l2))