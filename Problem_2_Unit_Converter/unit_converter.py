print("welcome " )
print(r"please enter your unit")
print("1.for length")
print("2.for time")
print("3.for temprature")
option=input("enter your option")
if option == "1":
   print("1.mile to km")
   print("1.meter to km")
   print("1.cm to km")
   choose=input("enter your option")
   if choose == "1":
    mile=float(input("eenter your value"))
    km=mile*1.609
    print(km,"kilometer")
   elif choose =="2":
    meter=float(input("enter your value in meter"))
    km=meter/1000
    print(km,"kilo meter")
   elif choose == "3":
    cm=float(input("enter your value in centi meter"))
    km=cm/10000
    print(cm,"centimeter")
   else:
     print("you enterd invalid")
elif option == "2":
  print("1.hour to minit")
  print("2.minit to second")
  choose=input("enter your choose")
  if choose == "1":
    hour=float(input("enter the time in hour") )
    minit=hour*60
    print(minit,"min")
  elif choose == "2":
    minit=input("enter your time in minit")
    sec=minit*60
    print(sec,"second")
  else :
    print("you enterd invalid")
elif option == "3":
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Celsius to Kelvin")

    choose = input("Enter your choice: ")

    if choose == "1":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(celsius, "°C")

    elif choose == "2":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9 / 5) + 32
        print(fahrenheit, "°F")

    elif choose == "3":
        celsius = float(input("Enter temperature in Celsius: "))
        kelvin = celsius + 273.15
        print(kelvin, "K")
    else:
        print("You entered an invalid option.")
else:
    print("Thank you for using the converter!")
