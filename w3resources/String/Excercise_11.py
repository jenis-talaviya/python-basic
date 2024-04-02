#Remove the characters which have odd index values of a given string

str = 'abcdef'

print(str[0::2])

#OR Another Method

def odd_value(str1):
    
    Result = ""
    
    
    
    for i in range(len(str1)):
        if i % 2 == 0:
            Result = Result + str[i]
    return Result

print(odd_value('abcdef'))