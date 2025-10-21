# simple calculator
print(" simple calculator ")
num1=float(input("enter first number: "))
operater=input("enter operater (+,-,*,/) :" )
num2=float(input("enter second number: "))

if operater =='+':
    result=num1 + num2
    print(f"\nResult: {num1} {operater} {num2} = {result}")
elif operater =='-':
    result=num1 - num2
    print(f"\nResult:{num1} {operater} {num2} ={result}")
elif operater =='*':
    result=num1 * num2
    print(f"\nResult:{num1} {operater} {num2} ={result}")
elif operater =='/':
    if num2!=0:
        result=num1 / num2
        print(f"\nResult:{num1} {operater} {num2} ={result}")
    else:
        print("\nError: ")
else:
    print("\nError: invalid operater!")       