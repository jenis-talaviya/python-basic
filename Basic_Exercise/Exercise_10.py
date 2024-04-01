list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

new_list = []

for num1 in list1:
    if num1 % 2 != 0:
        new_list.append(num1)
        
for num2 in list2:
    if num2 % 2 == 0:
        new_list.append(num2)

print(new_list)