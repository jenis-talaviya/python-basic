salary = 45000

tax = 0
if salary<=10000:
    print(f"tax amount is {tax}")
elif salary>=10000:
    new_salary = salary - 10000
    tax += new_salary * 0.1
    
else:
    #new_salary = 
    print(salary)
