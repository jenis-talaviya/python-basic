#Find sum and average of List in Python

input_str = [4,5,1,2,9,7,10,8]

sum = 0

for i in input_str:
    sum += i

svg = sum/len(input_str)

print(f"sum: {sum}")
print(f"avg: {svg}") 