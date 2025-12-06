print("Welcome to the Unit Converter!")
print("1. Convert miles to kilometers")
print("2. Convert Celsius to Fahrenheit")

choice = input("Enter 1 or 2: ")

if choice == "1":
    # Miles to kilometers
    miles = float(input("Enter distance in miles: "))
    kilometers = miles * 1.60934
    print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")
elif choice == "2":
    # Celsius to Fahrenheit
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")
else:
    print("Invalid choice! Please enter 1 or 2.")

