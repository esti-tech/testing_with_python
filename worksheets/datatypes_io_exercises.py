print("Datatype & I/O Exercises")
# Practice input/output and type conversions here.
# datatypes_io_exercise.py
print("=== Datatype & I/O Exercises ===")

# Get user's name (string)
name = input("1. What's your name? ")
print(f"Hello, {name} (type: {type(name).__name__})")

# Get age and convert to int
age_str = input("2. How old are you? ")
if age_str.isdigit():
    age = int(age_str)
    print(f"You are {age} years old (type: {type(age).__name__})")
else:
    print("Invalid age input!")

# Get weight and convert to float
try:
    weight = float(input("3. Enter your weight in kg: "))
    print(f"Weight: {weight} kg (type: {type(weight).__name__})")
except ValueError:
    print("Invalid weight input!")

# Yes/No input for boolean
likes_python = input("4. Do you like Python? (yes/no): ").strip().lower()
is_python_fan = likes_python in ["yes", "y"]
print(f"Loves Python: {is_python_fan} (type: {type(is_python_fan).__name__})")

# Final output
print("\n--- Summary ---")
print(f"Name         : {name}")
print(f"Age          : {age if 'age' in locals() else 'N/A'}")
print(f"Weight       : {weight if 'weight' in locals() else 'N/A'} kg")
print(f"Loves Python : {is_python_fan}")