# your code here
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
oprator = input("Enter operation (+, -, *, /): ")

if oprator == '+':
    print(a + b)
elif oprator == '-':
    print(a - b)
elif oprator == '*':
    print(a * b)
elif oprator == '/':
    if b != 0:
        print(a / b)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")
