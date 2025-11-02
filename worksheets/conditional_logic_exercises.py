print("Conditional Logic Exercises")
# Practice if/elif/else statements here.
def grade_calculator():
    """
    Calculates the letter grade based on a numeric score using if/elif/else statements.
    """
    print("--- Conditional Logic Exercises: Grade Calculator ---")
    
    # 1. Input the numeric score
    try:
        score = float(input("Enter the student's score (0-100): "))
    except ValueError:
        return "Error: Please enter a valid number for the score."

    # 2. Use if/elif/else statements to assign a grade
    if score >= 90:
        grade = "A"
    elif score >= 80:
        # Score is 80-89
        grade = "B"
    elif score >= 70:
        # Score is 70-79
        grade = "C"
    elif score >= 60:
        # Score is 60-69:
        grade ="D"
    else:
        # Score is less than 60:
        grade = "F"

    # 3. Print the result
    print(f"\nScore: {score}\nGrade: {grade}")

# Execute the function
if __name__ == "__main__":
    print(grade_calculator())

