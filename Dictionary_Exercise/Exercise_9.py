#Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

res = min(sample_dict,key=sample_dict.get)
print(res)
