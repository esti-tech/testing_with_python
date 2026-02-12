
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
opperation = input("Enter operation (+, -, *, /): ")

if opperation == '+':
    result = num1 + num2
elif opperation == '-':
    result = num1 - num2
elif opperation == '*':
    result = num1 * num2
elif opperation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Division by zero")
        exit()
else:
    print("Invalid operation")
    exit()

print("Result:", result)