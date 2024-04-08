# Compute the square of first N Fibonacci numbers, use map function and generate a list of the numbers

def fibo(n):
    fibo_sequence = [0,1]
    for i in range(2,n):
        fibo_sequence.append(fibo_sequence[-1]+fibo_sequence[-2])
    return fibo_sequence

def squre(num):
    return num *num

nums = 10

fibo_numbers = fibo(nums)

res_num = list(map(squre,fibo_numbers))

print(res_num)