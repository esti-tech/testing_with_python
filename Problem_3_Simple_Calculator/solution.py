x=int(input("enter the first number:"))
print(x)
y=int(input("enter the second number:"))
print(y)
opration=input("enter  number opration ")

if opration=='+':
    print(x+y)
elif opration=='-':
    print(x-y)
elif opration=='*':
    print(x*y)    
elif opration=='/':
    if x&y>0:
        print(x/y)
    elif y==0:
            print("invalid")
elif opration=='%':
    print(x%y)     

