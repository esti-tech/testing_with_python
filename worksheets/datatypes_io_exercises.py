print("Datatype & I/O Exercises")
# Practice input/output and type conversions here.
name = input("Please enter your name: ")
age_str = input("Please enter your age: ")
age_int = int(age_str)
print("Hello, " + name + "! You are " + str(age_int) + " years old.")
num = 23
textnum = "57"
MySum = num + int(textnum)
print("The sum is:", MySum)
print("The data type of the sum is:", type(MySum))
value_str = input("Enter a float number: ")
value_float = float(value_str)
print("The formatted number is: {:.2f}".format(value_float))
