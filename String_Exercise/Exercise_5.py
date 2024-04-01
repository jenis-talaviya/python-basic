#Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"

char_count = 0
digit_count = 0
symbol_count = 0

for char in str1:
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1
print(f"char is = {char_count} \ndigit is = {digit_count} \nsymbol is = {symbol_count}")