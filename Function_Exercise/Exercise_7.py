#Assign a different name to function and call it through the new name

def display_stud(name,age):
    print(name,age)
    
show_stud = display_stud

show_stud("emma",26)