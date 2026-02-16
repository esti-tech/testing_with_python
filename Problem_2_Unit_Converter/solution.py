

print("Welcome to the Unit Converter!")

print("What would you like to convert?")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")

choice = input("Enter 1 or 2: ")

if choice == "1":
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print(f"{km} kilometers = {miles} miles")
elif choice == "2":
    miles = float(input("Enter distance in miles: "))
    km = miles / 0.621371
    print(f"{miles} miles = {km} kilometers")
else:
    print("Invalid choice! Please run again and enter 1 or 2.")
