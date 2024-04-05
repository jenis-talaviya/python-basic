# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

input_string = input("Enter your sequence of words: ")


words = input_string.split()
print(words)
unique_words = sorted(set(words))
print(unique_words)

# Print the sorted unique words
print(' '.join(unique_words))
