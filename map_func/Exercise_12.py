from array import array

def plusminus(nums):
    n = len(nums)
    
    n1=n2=n3=0
    
    for x in nums:
        if x>0:
            n1+=1
        elif x<0:
            n2+=1
        else:
            n3+=1
    return round(n1/n,2), round(n2/n,2), round(n3/n,2)
nums = array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])

num_arr = list(map(int,nums))

result = plusminus(num_arr)

print(result)
