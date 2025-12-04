x=int(input("enter number one: "))
y=float(input("enter  number two: "))
opration=input("enetr the calculation: ")

match opration:
    case "+":
        print("addition = ", x+y)
    case "-":
        print("substraction = ", x-y)
    case "*":
        print("multiplication = ", x*y)
    case "/":
        if y==0:
            print("error cannot be divide by zero ")
        else:
            print("division = ", x/y)
    case _:
        print("unknown calacultion")
    