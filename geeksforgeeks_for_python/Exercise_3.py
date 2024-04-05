#Swap elements in String list
test_list = ['Gfg','is','best','for','geeks']

res = [sub.replace('G','-').replace('e','G').replace('-','e') for sub in test_list]

print("List after performing character swaps: "+str(res))

#OR 
res = ','.join(test_list)
res = res.replace('G',"_").replace('e','G').replace('_','e').split(',')

print(str(res))