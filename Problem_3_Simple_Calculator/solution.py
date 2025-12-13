# take input from user
num1=float(input("enter number 1:"))
num2=float(input("enter number 2:"))
print("selection of operation")
print("1.addition(+)")
print("2.subtraction(-)")
print("3.multiplcation(*)")
print("4.division(/)")
operation=input("1,2,3,or 4:")
#this is calculation part
if operation=="1":
    result=num1+num2
    print(f"{num1}+{num2}={result}")
elif operation=="2":
    result=num1-num2
    print(f"{num1}-{num2}={result}")    
elif operation=="3":
    result=num1*num2
    print(f"{num1}*{num2}={result}")  
elif operation=="4":
    if num2 != 0:
     result=num1/num2
     print(f"{num1}/{num2}={result}")
    else:  
     print(f"error:division can't by zero")  
else:
   print(f"error:please select again")     