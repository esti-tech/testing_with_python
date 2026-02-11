print("Datatype & I/O Exercises")
# Practice input/output and type conversions here.

# String input
name = input("Enter your name: ")

# Integer input
age = int(input("Enter your age: "))

# Float input
height = float(input("Enter your height in meters: "))

# Boolean input
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print(f"\nName: {name} (type: {type(name).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Height: {height} (type: {type(height).__name__})")
print(f"Student: {is_student} (type: {type(is_student).__name__})")
