print("Datatype & I/O Exercises")
# Practice input/output and type conversions here.

# --- Exercise 1: Basic Input and Output ---
print("\n--- Exercise 1: Personal Greeting ---")

name = input("Please enter your name: ")

#    Note: input() returns a string.
age_str = input("Please enter your age: ")

# 3. Print a greeting using an f-string or concatenation.
print(f"Hello, {name}! You entered your age as {age_str}.")

print("---------------------------------------")


# --- Exercise 2: Simple Arithmetic and Type Conversion ---
print("\n--- Exercise 2: Sum of Two Numbers ---")

# 1. Get the first number (as a string).
num1_str = input("Enter the first number: ")

# 2. Get the second number (as a string).
num2_str = input("Enter the second number: ")

# 3. Convert the input strings to integers (int) for calculation.
#    Note: Use float() if you expect decimal numbers.
try:
    num1 = int(num1_str)
    num2 = int(num2_str)

    # 4. Calculate the sum.
    total_sum = num1 + num2

    # 5. Print the result.
    print(f"The sum of {num1} and {num2} is: {total_sum}")

except ValueError:
    # Handle cases where the user enters non-integer text
    print("Error: Please ensure both inputs are whole numbers.")

print("---------------------------------------")


# --- Exercise 3: Area of a Rectangle (Float) ---
print("\n--- Exercise 3: Rectangle Area Calculator ---")

# 1. Get the length.
length_str = input("Enter the rectangle's length: ")

# 2. Get the width.
width_str = input("Enter the rectangle's width: ")

# 3. Convert the input strings to floating-point numbers (float).
try:
    length = float(length_str)
    width = float(width_str)

    # 4. Calculate the area.
    area = length * width

    # 5. Print the result, including the type of the 'area' variable.
    print(f"Length: {length}, Width: {width}")
    print(f"The area of the rectangle is: {area}")
    # Show the resulting datatype
    print(f"The type of the 'area' variable is: {type(area)}")

except ValueError:
    print("Error: Please ensure the length and width are valid numbers.")

print("---------------------------------------")
