# Use multiple map arguments
def addi_subs(x,y):
    return x+y,x-y

nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]

result = map(addi_subs,nums1,nums2)
print(list(result))