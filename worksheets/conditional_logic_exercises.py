print("Conditional Logic Exercises")
# Practice if/elif/else statements here.
# grade_evaluator.py

print("Grade Evaluator")

score = input("Enter your score (0–100): ")

if not score.isdigit():
    print("Invalid input! Please enter a number.")
else:
    score = int(score)
    if score > 100 or score < 0:
        print("Score out of valid range.")
    elif score >= 85:
        print("Grade: A")
    elif score >= 70:
        print("Grade: B")
    elif score >= 50:
        print("Grade: C")
    elif score >= 40:
        print("Grade: D")
    else:
        print("Grade: F")