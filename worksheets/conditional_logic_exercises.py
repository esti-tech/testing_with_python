print("Conditional Logic Exercises")
# Practice if/elif/else statements here.

age = int(input("Enter your age: "))
grade = int(input("Enter your grade: "))

if age < 18:
    print("You are a minor")
elif age < 65:
    print("You are an adult")
else:
    print("You are a senior")

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")
