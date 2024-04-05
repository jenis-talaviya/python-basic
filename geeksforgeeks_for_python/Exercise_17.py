#Python program to print all even numbers in a range

start = 4
end = 15

for number in range(start,end,2):
    print(f"{number}",end=" ")
    
#Or Dynamically

s_num = int(input("enter the number "))
l_num = int(input("enter the number "))

for num in range(s_num,l_num+1):
    if num %2 == 0:
        print(num,end=" ")