#Remove empty strings from a list of strings
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]

res = []

for i in str_list:
    if i:
        res.append(i)
print(res)