name = input("What's your name? ")
favorite_food = input("What's your favorite food? ")
current_year = int(input("What is the current year? "))
age = int(input("How old are you? "))
birth_year = current_year - age
print(f"\nHello, {name}! Here's your personalized greeting:")
print(f"Your favorite food is {favorite_food}.")
print(f"You're {age} years old, so you were born in {birth_year}.")
print(f"Enjoy your day, {name}, and I hope you get to eat some {favorite_food} soon!")
