# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:

raw_input = input("enter the word ")

sorted_word = sorted(raw_input.split(','))
output = ','.join(sorted_word)

print(output)