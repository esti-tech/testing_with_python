name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
print("\nSummary:")
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
years_to_100 = 100 - age
print(f"\n{name}, you will turn 100 in {years_to_100} years.")
