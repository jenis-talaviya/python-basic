number = str(input("Enter the number "))

if number == number[::-1]:
    print(f"{number} number is palidrome")
else:
    print(f"{number} number isn not palidrome")