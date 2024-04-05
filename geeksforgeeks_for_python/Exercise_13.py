# Sum of number digits in List

test_str = [12, 67, 98, 34]

result = []

for i in test_str:
    sum = 0
    for digit in str(i):
        sum += int(digit)
    result.append(sum)
    
print(str(result))