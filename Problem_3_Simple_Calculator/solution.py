
x=float(input("enter first number: "))
y=float(input("enter second number: "))
opration=input("enetr the operation: ")

match opration:
    case "+":
        print("sum = ", x+y)
    case "-":
        print("difference = ", x-y)
    case "*":
        print("product = ", x*y)
    case "/":
        if y==0:
            print("undefined")
        else:
            print("quotient = ", x/y)
    case _:
        print("unknown operation")
    