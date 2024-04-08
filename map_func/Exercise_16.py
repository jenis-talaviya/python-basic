#Convert all the characters in uppercase and lowercase and eliminate duplicate letters from a sequence

def covert_word(char):
    return str(char).upper(),str(char).lower()


chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}

result = map(covert_word,chrars)

print(set(result))