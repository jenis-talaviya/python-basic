#Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)

for tuple in tuple1:
    if tuple == tuple1[0]:
        print(True)


def check(t):
    return all(i == t[0] for i in t)

tuple2 = (45, 45, 45, 45)
print(check(tuple2))