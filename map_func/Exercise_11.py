#Compute the sum of elements of a given array of integers
from array import *

def arr_sum(num_arr):
    sum_n = 0
    for n in num_arr:
        sum_n += n
    return sum_n

num = array('i',[1,2,3,4,5,-15])
num_arr = list(map(int,num))

result = arr_sum(num_arr)
print(result)