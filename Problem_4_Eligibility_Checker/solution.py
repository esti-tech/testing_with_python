age=int(input("enter your  age :"))
has_license=input("have you direver license?(yes/no):")
if age>18:
    if has_license=='yes':
       print("so you are eligible for driving")
    else:
        print("yoi are not eligible for driving")
    
else:
    print("you are under age so you are not eligible")
