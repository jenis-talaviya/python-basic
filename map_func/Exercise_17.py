# Convert a given list of tuples to a list of strings using map function

colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]

cl = list(map(' '.join,colors))
print(cl)