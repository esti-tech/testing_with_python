A = input("Is it raining? (yes/no): ").lower() == "yes"
B = input("Do you have an umbrella? (yes/no): ").lower() == "yes"
if A and not B:
    print("You will get wet!")
elif A and B:
    print("You are safe from the rain.")
else:
    print("Enjoy your day!")
