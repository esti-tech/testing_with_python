# datatypes_io_exercises.py

print("Hey there! Let's try something simple.")

name = input("What’s your name? ")
age = input("How old are you? ")
gpa = input("What’s your GPA so far? ")

age = int(age)
gpa = float(gpa)

print("\nHere’s what you told me:")
print("Your name is", name)
print("You are", age, "years old")
print("Your GPA is", gpa)

if gpa >= 2.0:
    print("Nice job, you’re doing well in school!")
else:
    print("Don’t worry, keep pushing — you can do better next time!")

print("Thanks for sharing ")
