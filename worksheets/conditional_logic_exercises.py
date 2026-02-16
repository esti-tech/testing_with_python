print("Conditional Logic Exercises")

score = int(input("Enter your test score (0–100): "))
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

temperature = float(input("Enter the temperature in Celsius: "))
if temperature > 30:
    print("It's hot outside! Stay hydrated.")
elif temperature >= 20:
    print("Nice weather. Enjoy your day!")
elif temperature >= 10:
    print("A bit chilly. Grab a light jacket.")
else:
    print("Cold! Bundle up.")

