#1. Get name, favorite food, year, and age.
name = input ("enter your name :")
favorite_food = input(" enter your favorite food:" )
age=int(input("enter your age:"))
print(f"hello {name},nice to meet you!")
print(f"your favorite food is {favorite_food}")
print(f"your age is {age}")
#3. Calculate birth year (optional).
current_year=int(input("enter current year:"))
age=int(input("enter your age:"))
birth_year=current_year - age
print(f"you were born in {birth_year}.")
