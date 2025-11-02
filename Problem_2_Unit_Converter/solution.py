def unit_converter():
    """
    Converts between Miles/Kilometers or Celsius/Fahrenheit based on user choice.
    """
    print("\n--- Problem 2: Unit Converter ---")
    
    # 1. Ask which conversion user wants.
    print("Choose a conversion type:")
    print("1: Miles to Kilometers")
    print("2: Celsius to Fahrenheit")
    
    # Get the user's choice
    choice = input("Enter your choice (1 or 2): ").strip()
    
    # Use try/except to handle cases where the user enters non-numeric input for the value.
    try:
        # Check the choice using if/elif
        if choice == '1':
            # Conversion: Miles to Kilometers
            
            # 2. Input value and convert to a number (float is best for measurements)
            miles = float(input("Enter the distance in miles: "))
            
            # Conversion Formula: 1 mile = 1.60934 kilometers
            kilometers = miles * 1.60934
            
            # 3. Convert and print result. Use .2f to show two decimal places.
            print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")

        elif choice == '2':
            # Conversion: Celsius to Fahrenheit
            
            # 2. Input value and convert to a number (float is best for temperatures)
            celsius = float(input("Enter the temperature in Celsius: "))
            
            # Conversion Formula: F = (C * 9/5) + 32
            fahrenheit = (celsius * 9/5) + 32
            
            # 3. Convert and print result. Use .1f to show one decimal place.
            print(f"{celsius} Celsius is equal to {fahrenheit:.1f} Fahrenheit.")
            
        else:
            # Handle invalid choice
            print("Invalid choice. Please enter '1' or '2'.")
            
    except ValueError:
        # This handles cases where the user enters text instead of a number for the value.
        print("Error: Please enter a valid number for the value to convert.")

# Execute the function
if __name__ == "__main__":
    unit_converter()