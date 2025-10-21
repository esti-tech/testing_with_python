def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return "Error: Division by zero!" if b == 0 else a / b

print("Simple Calculator")
print("Choose operation: +, -, *, /")

op = input("Enter operator: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if op == '+':
    print(f"Result: {add(num1, num2)}")
elif op == '-':
    print(f"Result: {subtract(num1, num2)}")
elif op == '*':
    print(f"Result: {multiply(num1, num2)}")
elif op == '/':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid operator.")
