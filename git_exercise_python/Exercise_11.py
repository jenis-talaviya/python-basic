#Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
#The numbers obtained should be printed in a comma-separated sequence on a single line.

start = 1000
end = 3000
values = []

for i in range(start,end+1):
    s = str(i)
    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0) and (int(s[3]) % 2 == 0):
        values.append(s)
print(",".join(values))