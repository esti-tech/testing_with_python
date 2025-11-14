# Boolean Puzzle Game.py

print(" Welcome to the Boolean Puzzle Game!")
print("Answer each question with True or False.\n")

score = 0

ans = input("1. Is 0 treated as False in Python? ").lower()
if ans == "false":
    print("Correct! 0 means False.")
    score += 1
else:
    print(" Nope, 0 is actually False in Python.")

ans = input("2. Is an empty string ('') considered True? ").lower()
if ans == "false":
    print("Right again! Empty strings are False.")
    score += 1
else:
    print(" Nope, empty strings are False.")

ans = input("3. Does 'and' stop checking once the first False is found? ").lower()
if ans == "true":
    print(" Great! That’s called short-circuiting.")
    score += 1
else:
    print("Sorry, that’s incorrect.")

print("\nYour total score:", score, "out of 3")
if score == 3:
    print(" Perfect! You really know your Python.")
elif score == 2:
    print("Good job!")
else:
    print("Keep practicing — you’ll get there!")
