print("Choose conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Km to Miles")
choice = input("Enter 1, 2, or 3: ")

if choice == "1":
    value = float(input("Enter the value to convert: "))
    result = (value * 9/5) + 32
    print(f"{value}°C = {result}°F")
elif choice == "2":
    value = float(input("Enter the value to convert: "))
    result = (value - 32) * 5/9
    print(f"{value}°F = {result}°C")
elif choice == "3":
    value = float(input("Enter the value to convert: "))
    result = value * 0.621371
    print(f"{value} km = {result} miles")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")