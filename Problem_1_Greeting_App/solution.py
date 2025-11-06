# Get user input
name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
current_year = int(input("Enter the current year: "))
age = int(input("Enter your age: "))

# Calculate birth year
birth_year = current_year - age

# Print personalized greeting
print(f"\nHello {name}!")
print(f"Your favorite food is {favorite_food}.")
print(f"You were born in {birth_year}.")# your code here
