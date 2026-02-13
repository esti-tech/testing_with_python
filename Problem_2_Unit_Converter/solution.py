# Unit Converter App
# Ask user for coversion type
choice = input(
    "Type 'm' to convert miles to kilometers or 'c' to convert Celsius to Fahrenheit: ").lower()
if choice == 'm':
    miles = float(input("Enter miles:"))
    kilometers = miles * 1.60934
    print(f"{miles} miles is equal to {kilometers} kilometers.")
elif choice == 'c':
    celsius = float(input("Enter celsius:"))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}degrees celsius is equal to {fahrenheit} degrees fahrenheit.")
else:
    print("Invalid choice. please type 'm' or 'c'.")
