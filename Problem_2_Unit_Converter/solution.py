def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# Dictionary mapping user's choice to conversion function and units
conversions = {
    '1': {
        'func': celsius_to_fahrenheit,
        'from_unit': 'Celsius',
        'to_unit': 'Fahrenheit'
    },
    '2': {
        'func': fahrenheit_to_celsius,
        'from_unit': 'Fahrenheit',
        'to_unit': 'Celsius'
    }
}

print("Choose conversion:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter choice (1 or 2): ")

if choice in conversions:
    value = float(input(f"Enter temperature in {conversions[choice]['from_unit']}: "))
    result = conversions[choice]['func'](value)
    print(f"{value} {conversions[choice]['from_unit']} is {result:.2f} {conversions[choice]['to_unit']}")
else:
    print("Invalid choice.")