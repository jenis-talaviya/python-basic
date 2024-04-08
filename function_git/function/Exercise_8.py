#Define a function is_palindrome() that recognizes palindromes

def is_palindrome(s):
    return s == s[::-1]

input_string = "malayalam"
if is_palindrome(input_string):
    print(True)
else:
    print(False)
