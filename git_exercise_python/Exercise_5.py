# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class in_out_string():
    def __init__(self):
        self.input_s = ""
        
    def getstring(self):
        self.input_s = input("enter the string:")
    
    def printstring(self):
        print(self.input_s.upper())
    
def string_manipul():
    sm = in_out_string()
    sm .getstring()
    sm.printstring()
    
string_manipul()