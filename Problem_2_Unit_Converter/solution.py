# Conversion Program: Miles to Kilometers or Celsius to Fahrenheit

def miles_to_kilometers(miles):
    return miles * 1.60934

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Main program
print("Choose a conversion:")
print("1. Miles to Kilometers")
print("2. Celsius to Fahrenheit")

choice = input("Enter 1 or 2: ")

if choice == "1":
    miles = float(input("Enter distance in miles: "))
    kilometers = miles_to_kilometers(miles)
    print(f"{miles} miles = {kilometers:.2f} kilometers")

elif choice == "2":
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.2f}°F")

else:
    print("Invalid choice! Please enter 1 or 2.")
