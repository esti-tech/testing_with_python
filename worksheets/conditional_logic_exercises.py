# conditional_logic_exercises.py

print("Welcome! Let’s see if you can get a scholarship.")

score = float(input("Please enter your test score (out of 100): "))
income = float(input("Enter your family’s monthly income: "))

print("\nChecking your eligibility...")

if score >= 90:
    print("Congratulations! You got a FULL SCHOLARSHIP ")
elif score >= 75:
    if income < 5000:
        print("Good news! You get a PARTIAL SCHOLARSHIP with priority.")
    else:
        print("You get a PARTIAL SCHOLARSHIP.")
elif score >= 60:
    print("You’ll receive a MERIT AWARD for your effort.")
else:
    print("Sorry, you didn’t qualify this time. Keep studying hard!")

print("Thank you for checking your result ")
