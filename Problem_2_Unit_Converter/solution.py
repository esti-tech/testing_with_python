print("what type of conversion do you want? please enter ")
choice1 = input("1 for length\n2 for temprature\n")
if choice1 == "1":
    choice2 = input("1 from mile to kilometer\n2 from kilometer to mile\n")
    if choice2 == "1":
        num = input("enter the number in mile\n" )
        num = int(num)
        num *= 1.609
        print(f"{num}km")
    elif choice2 == "2":
        num = input("enter the number in kilometers\n" )
        num = int(num)
        num *= 0.621
        print(f"{num}miles")
    else:
        print("invalid input")
elif choice1 == "2":
    choice2 = input("1 from celsius to fahrenheit\n2 from fahrenheit to celsius\n")
    if choice2 == "1":
        num = input("enter the number in celsius\n" )
        num = int(num)
        num = num*1.8 + 32
        print(f"{num}°F")
    elif choice2 == "2":
        num = input("enter the number in fahrenheit\n" )
        num = int(num)
        num = (num - 32)/1.8
        print(f"{num}°c")
    else:
        print("invalid input")
else:
    print("invalid input")
print("thanks for using!")



