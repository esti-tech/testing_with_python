# ask which converstion users want
print("select converstion type")
print("1.miles to kilometers")
print("2.Celsius to Fahrenheit")
choice=input("1 or 2")
#users select number 1 miles to kilometers
if choice=="1":
    miles=float(input("enter miles :"))
    km=miles*1.069
    print(f"{miles}mile={km:.1f}kilometers")
#users select number 2 celcius   to  fahrenhite
elif choice=="2":
    celcius=float(input("enter celcius:"))
    fahrenite=(celcius*9/5)+32
    print(f"{celcius}°C={fahrenite:.1f}°f")
else:
    print("incorrect choice please select 1 or 2")
