# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language"). 
def translate(x):
    s = ''
    for i in x:
        if i not in ('aeiou'):
            s += i + "o" + i
        else:
            s += i 
    print (s) 
    
translate("this is fun")
