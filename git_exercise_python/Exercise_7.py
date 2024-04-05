# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡­Y-1.

X,Y = map(int,input("enter two number separated by comma: ").split(','))

array_2 = [[i*j for j in range(Y)]for i in range(X)]

print(array_2)