print("Conditional Logic Exercises")
# Practice if/elif/else statements here.

# Determine grade based on marks
# Ask for marks
score = int(input("Enter your score(0-100):"))

# Check grade range

if score >= 90:
    print("Grade: A, Excellent!")
elif score >= 75:
    print("Grade: B, Good!")
elif score >= 60:
    print("Grade: C, Fair effort.")
elif score >= 45:
    print("Grade: D, Needs improvement.")
else:
    print("Grade: F, Failed.")
