print("Datatype & I/O Exercises")
# Practice input/output and type conversions here.

name=input("Enter your name: ")
age=int(input("Enter your age: "))
height=float(input("Enter your height in meters: "))    
student=bool(int(input("Are you a student? (1 for Yes, 0 for No): ")))

print("\nUser Information")
print(f"Name: {name}")
print(f"data type: {type(name)}")
print(f"Age: {age} years")
print(f"data type: {type(age)}")
print(f"Height: {height} meters")
print(f"data type: {type(height)}")
print(f"Student: {student}")
print(f"data type: {type(student)}")