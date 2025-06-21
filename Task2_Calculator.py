print("Welcome to Calculator.")

num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))

print("Choose an operator:1 for + , 2 for -, 3 for *, 4 for /")
operator = int(input("Enter your choice of integer for operator: "))

if operator==1 :
    print(f"Your summation is {num1+num2}")

elif operator==2 :
    print(f"Your subtraction is {num1-num2}")    

elif operator==3 :
    print(f"Your multiplication is {num1*num2}")

elif operator==4 :
    if num2 != 0:
        print(f"Your division is {num1 / num2}")
    else:
        print("Error: Cannot divide by zero.")
    
else :
    print("Entered integer for operator is not valid.")
