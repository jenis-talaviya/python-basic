#Find all occurrences of a substring in a given string by ignoring the case
str1 = "Welcome to USA. usa awesome, isn't it?"

sub_string = "USA"

strr = str1.lower()
print(strr)

res = strr.count(sub_string.lower())
print(f"USA is {res}")