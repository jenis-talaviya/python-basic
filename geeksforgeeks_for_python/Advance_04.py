#Python program to select Random value from list of lists

import random

test_list = [[4, 5, 5], [2, 7, 4], [8, 6, 3]]

r_no = [0,1,2]

result = random.choice(test_list[random.choice(r_no)])

print(str(result))