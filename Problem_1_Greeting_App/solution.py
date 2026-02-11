# Personalized Greeting App
# Ask for user details

name = input("What is your name?")
favorite_food = input("What is your favorite food?")
current_year = int(input("What is the current year?"))
age = int(input("How old are you?"))

# Calculate birth year
birth_year = current_year - age
# Print personalized greeting
print("\nHello, " + name + "!")
print("Oh wow, " + favorite_food + " sounds delicious")
print("So, you were probably born in " + str(birth_year) + ".")
print("Nice to meet you," + name + "!")
