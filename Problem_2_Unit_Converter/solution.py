print("Unit Converter")
print("1. Miles to Kilometers")
print("2. Celsius to Fahrenheit")

choice = input("Choose conversion (1 or 2): ")

if choice == "1":
    miles = float(input("Enter miles: "))
    kilometers = miles * 1.60934
    print(f"{miles} miles = {kilometers:.2f} kilometers")
elif choice == "2":
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")
else:
    print("Invalid choice")
