# Input numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Input operation
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation and handle division by zero
if operation == '+':
    result = a + b
    print(f"Result: {result}")
elif operation == '-':
    result = a - b
    print(f"Result: {result}")
elif operation == '*':
    result = a * b
    print(f"Result: {result}")
elif operation == '/':
    # Check for division by zero
    if b != 0:
        result = a / b
        print(f"Result: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")
    