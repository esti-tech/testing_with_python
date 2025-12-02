# your code hereprint("Simple Calculator")
print("Choose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

operation = input("Enter the number corresponding to the operation (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = None
error = None

if operation == "1":
    result = num1 + num2
    op_symbol = "+"
elif operation == "2":
    result = num1 - num2
    op_symbol = "-"
elif operation == "3":
    result = num1 * num2
    op_symbol = "*"
elif operation == "4":
    if num2 == 0:
        error = "Error: Division by zero is not allowed."
    else:
        result = num1 / num2
        op_symbol = "/"
else:
    error = "Invalid operation selected."

if error:
    print(error)
else:
    print(f"{num1} {op_symbol} {num2} = {result}")
