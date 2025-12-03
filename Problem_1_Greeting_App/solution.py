# your code here
from datetime import date

def inputs(question):
    while True:
        ans = input(question)
        if ans: return ans
        else: print("Field can't be left empty!! ")
def out():
    while True:
        ans = inputs("Do you want to go again?(y/n) ").upper()
        if ans == "Y" or ans == "YES": break 
        elif ans == "N" or ans == "NO": exit(0) 

while True:
    print()
    name = inputs("Name: ")
    food = inputs("Favorite food? ")
    while True:
        year = date.today().year
        age = inputs("Age: ")
        try:
            age_i = int(age)
        except Exception as e:
            print("Invalid input for age!")
        else:
            if age_i >= 0 and year - age_i >= 0:
                year -= age_i
                break
            else: print("Age can't be negative!! Either input a proper number or fix your devices time")
    print()
    print("Hi", name)
    print("Your favorite food is", food)
    print(f"You were born in the year {year}")
    out()    
