#Convert List to List of dictionaries

test_list = ["Gfg", 3, "is", 8, "Best", 10, "for", 18, "Geeks", 33]

key_list = ['name','id']

n = len(test_list)
res = []

for ind in range(0,n,2):
    res.append({key_list[0]: test_list[ind],key_list[1]: test_list[ind + 1]})

print(str(res))