print("Conditional Logic Exercises")
# Practice if/elif/else statements here.

# 1️⃣ Check if a number is positive, negative, or zero
num = int(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#Check if a person is eligible to vote
age = int(input("\nEnter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")
