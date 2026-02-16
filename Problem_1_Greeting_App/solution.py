name = input("What's your name? ")
favorite_food = input("What's your favorite food? ")
current_year = int(input("What is the current year? "))
age = int(input("How old are you? "))


birth_year = current_year - age

print(f"\nHello, {name}! It's awesome that you love {favorite_food}.")
print(f"Since it's {current_year} and you're {age} years old, you were born in {birth_year}.")