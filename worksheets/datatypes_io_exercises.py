print("Datatype & I/O Exercises")
name = input("Enter your name: ")
print(f"Hello, {name}!")
age = input("Enter your age: ")
age = int(age)  
print(f"You are {age} years old.")
radius = input("Enter the radius of a circle: ")
radius = float(radius) 
area = 3.14 * radius ** 2
print(f"The area of the circle with radius {radius} is {area:.2f}.")
string_number = "100"
int_number = int(string_number)
print(f"The integer value of the string '100' is {int_number}.")
num = 25
num_str = str(num)
print(f"The string representation of the number 25 is '{num_str}'.")
x, y = input("Enter two numbers separated by space: ").split()
x, y = int(x), int(y)
print(f"The sum of {x} and {y} is {x + y}.")
