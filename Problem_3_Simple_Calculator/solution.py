
#simple calculater
#1. Input two numbers.
num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
#2. Input operation.
operation =input("enter the operation (/,*,-,+):")
#3. Perform calculation.
if operation=='+':
   result=num1+num2
elif operation=='-':
  result=num1-num2
elif operation=='*':
  result =num1*num2
elif operation=='/':
#4. Handle division by zero.
  if num2==0:
    print("error or division by zero is not allowed")
    result =None
  else:
   result=num1/num2
else:
  print("invalid operation")
  result =None
#display result if valid
if result is not none:
  print("result:",result)
