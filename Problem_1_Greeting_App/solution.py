 # 1. Get name , favorite food and age
name = input("Enter your name: ")
food = input("What is your favorite food? ")
age = int(input("Enter your age: ")) 
year=int(input("Enter current year"))

# 2. Print greeting
print(f"Hello {name}! Nice to meet you.")
print(f"So, you love {food}? That's great!")

# 3. Calculate birth year(optional)
birth_year = year - age

