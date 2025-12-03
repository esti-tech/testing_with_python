name = input("Enter your name: ")
favorite_food = input("Enter your favorite food: ")
current_year = int(input("Enter current year: "))
age = int(input("Enter your age: "))
print("Hello " + name + "! It was nice that your favorite food is " + favorite_food + ".\nI am glad to know you are " + str(age) + " years old.")

#to calculate and display birth year
birth_year = int(current_year) - int(age)
print(f"That means you were born in {birth_year}.")

