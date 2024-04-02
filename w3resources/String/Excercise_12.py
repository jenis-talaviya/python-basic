#Write a Python program to count the occurrences of each word in a given sentence.

str1 = 'the quick brown fox jumps over the lazy dog.'

counts = dict()
word = str1.split()

for word in word:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts) 
        