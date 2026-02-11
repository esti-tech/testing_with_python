# Simple Calculator

# Ask the user for two numbers
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
# Ask for the operation
print("Choose an operation: +,-,*,/")
operation = input("Enter your choice:")
# Perform calculation based on user choice
if operation == "+":
    result = num1 + num2
    print("The sum is:", result)
elif operation == "-":
    result = num1 - num2
    print("The difference is:", result)
elif operation == "*":
    result = num1 * num2
    print("The product is:", result)
elif operation == "/":
    # check if num2 is not zero
    if num2 != 0:
        result = num1/num2
        print("The quotient is:", result)
    else:
        print("Error: Cannot divide by zero!")
else:
    print("Invalid operation please choose +,-,*,/.")
