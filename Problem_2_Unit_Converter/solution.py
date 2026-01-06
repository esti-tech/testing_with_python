convert = input("Enter the unit to convert from (Celsius/Fahrenheit): ")
if convert == "Celsius":
    Celsius= float(input("Enter temperature in Celsius: "))
    fahrenheit = (Celsius * 9/5) + 32
    print(f"Temperature in Fahrenheit: {fahrenheit}")
elif convert == "Fahrenheit":
    Fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    Celsius = (Fahrenheit - 32) * 5/9
    print(f"Temperature in Celsius: {Celsius}")
else:
    print("Invalid unit. Please enter either 'Celsius' or 'Fahrenheit'.")