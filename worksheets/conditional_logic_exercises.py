#print("Conditional Logic Exercises")
# Practice if/elif/else statements here.
grade = int(input("enter your grade:\n"))
if grade < 0 and grade > 100:
  ("print invalid input")
elif grade >= 90:
  print("you scored A+")
elif grade >= 85:
  print("you scored A")
elif grade >= 80:
  print("you scored A-")
elif grade >= 75:
  print("you scored B+")
elif grade >= 70:
  print("you scored B")
elif grade >= 65:
  print("you scored B-")
elif grade >= 60:
  print("you scored C+")
elif grade >= 55:
  print("you scored C")
elif grade >= 50:
  print("you scored C-")
else: print("you scored F")
