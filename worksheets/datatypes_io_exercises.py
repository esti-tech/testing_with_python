print("Datatype & I/O Exercises")

#to get user input and display message
name=input("Enter your name: ")
print(type(name))
print("Hello " + name )

age=int(input("Enter your age: "))
print(type(age))
print("Your age is " + str(age))

height=float(input("Enter your height in meters: "))
print(type(height))
print("your height is " + str(height) + " meters")

#to check a number is complex or real
complex_num=complex(input("Enter a number: "))
if complex_num.imag == 0:
    print("the number that you entered is real")
else:
    print("the number that you entered is complex")
print(type(complex_num))

#to demonstrate boolean datatype
bool_value=bool(int(input("Enter 1 for true and 0 for false: ")))
print("the boolean value that you entered is " + str(bool_value))
print(type(bool_value))

#to demonstrate type casting
num1=input("Enter a number: ")
num2=input("Enter another number: ")
sum=int(num1)+int(num2)
print("The sum of the two numbers is: " + str(sum))
float_sum=float(num1) + float(num2)
print("the sum of the two numbers in float is: " + str(float_sum))