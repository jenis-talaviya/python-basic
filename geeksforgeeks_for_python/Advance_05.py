#Reverse Row sort in Lists of List

test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]

for element in test_list:
    element.sort(reverse=True)
    
print(str(test_list))