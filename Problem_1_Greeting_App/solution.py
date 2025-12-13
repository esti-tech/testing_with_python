name = input("Enter your name: ")
food = input("Enter your favorite food: ")
year = int(input("Enter the current year: "))
age = int(input("Enter your age: "))

birth_year = year - age

print(f"\nHey {name}! You love {food}, right?")
print(f"You’re {age} years old, so you were likely born in {birth_year}.")
