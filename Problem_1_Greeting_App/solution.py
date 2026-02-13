
name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
year = int(input("Enter the current year: "))
age = int(input("Enter your age: "))

print(f"\nHello, {name} Nice to meet you.")
print(f" your favorite food is {favorite_food}. That sounds delicious!")

birth_year = year - age
print(f"You were born in {birth_year}.")
