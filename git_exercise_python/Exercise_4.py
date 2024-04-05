#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:

# Get the input string from the console
input_sequence = input("Enter a sequence of comma-separated numbers: ")

# Generate a list of numbers using list comprehension
number_list = [int(item) for item in input_sequence.split(',')]

# Convert the list to a tuple
number_tuple = tuple(number_list)

print(f"List: {number_list}")
print(f"Tuple: {number_tuple}")
