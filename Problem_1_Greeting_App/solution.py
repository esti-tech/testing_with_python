#Problem 1:Personalized Greeting App

#Ask for user input 
name =input("What is your name?")
favorite_food =input("What is your favorite food?")
current_year =int(input("What is the current year?"))
age =int(input("How old are you?"))

#Calculate birth year
birth_year =current_year-age

#Print personalized greeting 
print("\n---your personalized greeting---")
print(f"Hello {name}!")
print(f"It's great to meet someone who loves {favorite_food}!")
print(f"Since you're {age} years old and it's {current_year}, you were born in {birth_year}.")
print("Have a nice day thanks for using this app!")