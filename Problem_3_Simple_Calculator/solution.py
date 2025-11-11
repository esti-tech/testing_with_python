a = float(input("enter number "))
ope = str(input("enter operaton "))
b = float(input("enter number "))
choice = ope
if choice == "/":
    if b == 0:
        print("Division by 0 is impossible! System error 1.ex786396")
    else:
        print("result", a/b)
elif choice == "-":
    print("result", a-b)
elif choice == "*":
    print("result", a*b)
elif choice == "+":
    print("result", a+b)
else:
    print("invalid operator")