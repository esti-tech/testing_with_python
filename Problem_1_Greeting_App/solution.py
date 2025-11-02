# Get user input
user_full_name = input("Kindly enter your full name? ")
favorite_food = input("What is your favorite food? ")
current_year = int(input("What is the current year? "))
age = int(input("Please enter your age in whole years: "))

# Calculate birth year
birth_year = current_year - age 

# Print personalized greeting
print(f"Hello, {user_full_name}! Your favorite food is {favorite_food}.")
print(f"You were born in {birth_year}.")