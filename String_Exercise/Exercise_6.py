#Create a mixed String using the following rules

# s1 = "Abc"
# s2 = "Xyz"
# result = " "
# for c1,c2 in zip(s1,s2):
#     result += c1+c2
# print(result)

# output = "".join(c1+c2 for c1,c2 in zip(s1,s2))
# print(output)
    
input1 = "Abc"
input2 = "Xyz"

output = "".join(c1 + c2 for c1, c2 in zip(input1, input2))
print(output)  # AzbycX


