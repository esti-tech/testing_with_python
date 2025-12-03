# Ask which conversion the user wants
print("Choose conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter 1 or 2: ")

# Get the value from the user
value = float(input("Enter the temperature value: "))

# Perform conversion
if choice == "1":
    result = (value * 9/5) + 32
    print(f"{value}°C = {result}°F")
elif choice == "2":
    result = (value - 32) * 5/9
    print(f"{value}°F = {result}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")
