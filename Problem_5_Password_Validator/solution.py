def password_validator():
    # Ask for name and password.
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    
    # Initialize a list to store missing rules.
    missing_rules = []

    # Check Length 
    if len(password) < 8:
        missing_rules.append("Password must be at least 8 characters long.")

    # Check Digit presence
    # The 'any()' function checks if at least one character is a digit
    if not any(char.isdigit() for char in password):
        missing_rules.append("Password must contain at least one digit.")

    # Check Not same as name
    if password.lower() == name.lower():
        missing_rules.append("Password must not be the same as your name.")

    # Output strength and missing rules.
    if not missing_rules:
        print("\nPassword is strong.")
    else:
        print("\nPassword is weak. Missing rules:")
        for rule in missing_rules:
            print(f"- {rule}")

# Run the validator
password_validator()