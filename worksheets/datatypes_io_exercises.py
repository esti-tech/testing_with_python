print("Datatype & I/O Exercises")
# Student Grade Analyzer

# Step 1: Input
name = input("Enter student name: ")

marks = []
for i in range(1, 4):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)

# Step 2: Process
average = sum(marks) / len(marks)

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Step 3: Output
print("\n--- Report Card ---")
print(f"Name: {name}")
print(f"Marks: {marks}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
