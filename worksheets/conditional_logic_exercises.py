print("Conditional Logic Exercises")
# Practice if/elif/else statements here.
def check_voting_eligibility():
    try:
        age = int(input("Enter your age: "))
        citizenship = input("Are you a citizen? (yes/no): ").strip().lower()
        if age >= 18 and citizenship == 'yes':
            print("You are eligible to vote.")
        elif age < 18:
            print("You are not eligible to vote because you are underage.")
        elif citizenship != 'yes':
            print("You are not eligible to vote because you are not a citizen.")
        else:
            print("Eligibility could not be determined.")
            
    except ValueError:
        print("Invalid input! Please enter a valid age.")
check_voting_eligibility()
