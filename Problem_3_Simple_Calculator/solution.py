# Input two numbers ,Input operation, apply calculation 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
   addition = num1 + num2
   print("The addition of two numbers is: ",addition)

elif operation == '-':
    subtraction = num1 - num2
    print("The subtraction of two numbers  is: ",subtraction)

elif operation == '*':
    multiplication = num1 * num2
    print("The multiplication of two numbers is: ",multiplication)

elif operation == '/':
    if num2 != 0:
       division = num1 / num2
       print("The division of two numbers is: ",division)
    else:
        print("Error: Division by zero is not allowed or undifined!")

else:
    print("Invalid operation. Please use +, -, * or /.")
