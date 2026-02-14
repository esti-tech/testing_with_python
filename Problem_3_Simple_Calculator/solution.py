print("hello! this is a simple calculator")
print("please choose numbers from 1 upto 5 to use the calculator!")
print("1: for addition")
print("2: for subtraction")
print("3: for multiplication")
print("4: for division")
print("5: for exponentiation")
operation = input("Enter your choice: ")
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
if operation == "1":
    print(f"The total sum is {num1 + num2}!")
elif operation == "2":
    print(f"The difference is {num1 - num2}!")
elif operation == "3":
    print(f"The product is {num1 * num2}!")
elif operation == "4":
    if num2 == 0:
        print("Division by zero is not defined!")
    else:
        print(f"The quotient is {num1 / num2}!")
elif operation == "5":
    print(f"The exponent result is {num1 ** num2}!")
# your code here