print("Datatype & I/O Exercises")

age_str = input("Enter your age: ")
age = int(age_str)
print(f"You are {age} years old.")

height_str = input("Enter your height in meters: ")
height = float(height_str)
print(f"Your height is {height} meters.")

name = input("Enter your name: ")
score = float(input("Enter your test score: "))
print(f"{name}, your score is {score}.")

response = input("Do you like Python? (yes/no): ").strip().lower()
likes_python = response == "yes"
print(f"Likes Python: {likes_python}")
