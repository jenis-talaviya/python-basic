#Define a function that computes the length of a given list or string

def find_length(x):
    c=0
    for item in x:
        c += 1
    return c
a = 'jenis'

print(find_length(a))