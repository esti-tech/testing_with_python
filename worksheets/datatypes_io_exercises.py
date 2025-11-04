print("Datatype & I/O Exercises")
# Practice input/output and type conversions here.

#BMI Calculator
print("BMI Calculator")
weight=float(input("Enter your weight(kg):"))
height=float(input("Enter your height(m):"))
BMI=weight/(height**2)

print(f"Weight:{weight}kg")
print(f"Height:{height}m")
print(f"Your BMI:{BMI:.2f}")
