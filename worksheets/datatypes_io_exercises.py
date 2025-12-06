print("Datatype & I/O Exercises")
# Practice input/output and type conversions here.
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

print("\n--- User Info ---")
print("Name:", name)
print("Age:", age)
print("Height:", height, "m")
print("Student:", is_student)
print("After 5 years, you will be", age + 5, "years old.")
