# step 1 enter input
name=input("enter your name:")
food=input("enter your favorite food:")
year=int(input("enter current year:"))
age=int(input("enter your age:"))
print(f"\nHello",{name})
print(f"i heared your favorite food is {food}")
birth_year=year-age
print(f"you were probably born in {birth_year}")