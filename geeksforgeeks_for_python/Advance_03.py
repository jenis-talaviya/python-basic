#Uncommon elements in Lists of List

test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]

res_list = []

for i in test_list1:
    if i not in test_list2:
        res_list.append(i)

for i in test_list2:
    if i not in test_list1:
        res_list.append(i)

print(str(res_list))