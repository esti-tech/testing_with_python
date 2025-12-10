print("Conditional Logic Exercises")
# Practice if/elif/else statements here.

#Temperature Advice
temp=int(input("What's the current temperature in deg c? "))
if temp>30:
  advice ="Wow, it's really hot out there! Don't forget to drink plenty of water."
elif temp>20:
  advice ="Perfect weather! Great day to be outside."
elif temp>10:
  advice ="It's a bit cool today. you might want to grab a light jacket."
else:
  advice ="It's pretty cold! Make sure to dress warmly."

print(f"At {temp} deg c: {advice}")
