num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Choose operation: +, -, *, /")
operation = input("Enter operation: ")
if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed!")
    else:
        result = num1 / num2
        print("Result:", result)

else:
    print("Invalid operation! Please enter +, -, * or /.")
