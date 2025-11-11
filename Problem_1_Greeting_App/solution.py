
name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
current_year = int(input("Enter the current year: "))
age = int(input("Enter your age: "))

print(f"\nHello {name}! Nice to meet you.")
print(f"I heard you like {favorite_food}. That sounds great!")

birth_year = current_year - age
print("You were born in approximately {birth_year}.")
