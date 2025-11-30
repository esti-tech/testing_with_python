num1 = int(input("enter the first number:\n" ))
num2 = int(input("enter the second number:\n"))
oper = input("enter the operator:\n+ for addition\n- for subtraction\n* or x for multiplication\n/ for division\n")
if oper == "+":
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")
elif oper == "-":
    diff = num1 - num2
    print(f"{num1} - {num2} = {diff}")    
elif oper == "*" or oper == "x":
    prod = num1 * num2
    print(f"{num1} x {num2} = {prod}")
elif oper == "/":
    if num2 == 0:
        print("invalid input")
    else:
        qoat = num1 / num2
        print(f"{num1} / {num2} = {qoat}")
else:
    print("invalid operator")
print("thanks for using")

        