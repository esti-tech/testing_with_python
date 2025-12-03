num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation_sign = input("Enter the operation (1. add, 2. subtract, 3. multiply, 4. divide): ")
if operation_sign == "1":
    result = num1 + num2
    print(f"The result of addition is: {result}")
elif operation_sign == "2":
    result = num1 - num2
    print(f"The result of subtraction is: {result}")
elif operation_sign == "3":
    result = num1 * num2
    print(f"The result of multiplication is: {result}")
elif operation_sign == "4":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of division is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation.")