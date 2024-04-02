#Find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string
words = ["python","exercise","longest","word"]

long_word = ''
count = 0

for word in words:
    if len(word) > count:
        long_word = word
        count = len(word)

print(f"longest word {long_word}")
print(f"legnth is {count}")