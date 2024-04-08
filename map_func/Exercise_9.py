#Create a new list taking specific elements from a tuple and convert a string value to integer
def stud_name(x):
    return x[0]


student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'), ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]

res_data = list(map(stud_name,student_data))

print(res_data)

#OR

stud_data = list(map(lambda x:x[0],student_data))
stud_dob = list(map(lambda x:x[1],student_data))
stud_weight = list(map(lambda x:int(x[2][:-2]),student_data))

print(stud_data)
print(stud_dob)
print(stud_weight)