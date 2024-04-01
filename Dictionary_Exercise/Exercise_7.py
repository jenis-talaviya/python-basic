#Check if a value exists in a dictionary

sample_dict = {'a': 100, 'b': 200, 'c': 300}

l1 = list(sample_dict.values())
print(l1)

if 200 in sample_dict.values():
    print("200 present in a dict") 