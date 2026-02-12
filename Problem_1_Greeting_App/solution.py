name = input("What's your name? ")
food = input("What's your favorite food? ")
year = int(input("What year is it now? "))
age = int(input("How old are you? "))

print(f"Hi {name}! Nice to meet you.")
print(f"So you love {food}, that's awesome!")

birth_year = year - age
print(f"You were probably born in {birth_year}.")