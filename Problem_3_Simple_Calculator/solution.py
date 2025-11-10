# you# Input two numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Input operation
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation
if operation == '+':
    result = num1 + num2
    print("Result:", result)
elif operation == '-':
    result = num1 - num2
    print("Result:", result)
elif operation == '*':
    result = num1 * num2
    print("Result:", result)
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid operation.")r code here
