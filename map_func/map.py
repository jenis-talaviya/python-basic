def addition(n):
    return n + n
 
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition,numbers)
print(list(result))

result1 = map(lambda x:x + x,numbers)
print(list(result1))

l = ['sat','bat','cat','mat']

test = list(map(tuple,l))

print(test)

def double_even(num):
    if num % 2 == 0:
        return num * 2
    else:
        return num * num
    
numbers = [1,2,3,4,5]

result2 = list(map(double_even,numbers))

print(result2)