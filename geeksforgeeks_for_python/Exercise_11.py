#Count occurrences of an element in a list
lst = [15,6,7,10,12,20,10,28,10]
x = 10
count = 0
for ele in lst:
    if ele == x:
        count += 1
print(f"total {x} is {count}")

#OR

print(lst.count(x))