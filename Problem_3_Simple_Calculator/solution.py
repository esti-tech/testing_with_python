#problem 3
print("Quick Calculator")
num1 = float(input("Enter first number: "))
operator = input("Enter operator ( +, _, *, /): ")
num2 = float(input("Enter second number:"))
if operator == '+' :
        result = num1 + num2
        print(f"Result: {result}")
elif operator == '-' :
        result = num1 - num2
        print(f"Result: {result}")
elif operator == '*' :
        result = num1 * num2
        print(f"Result: {result}")
elif operator == '/':
   if num2!=0:
         result= num1/num2
         print(f"Result:{result}")
   else:
        print("Error: ")
else:
        print("invalid operater")
