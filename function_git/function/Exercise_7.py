#Define a function reverse() that computes the reversal of a string.


def reverse(x):
    str1 =[]
    for i in range(len(x))[::-1]:
        str1.append(x[i])
    print(''.join(str1))

reverse('i am python')

