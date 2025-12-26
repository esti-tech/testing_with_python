temperature = int(input("Enter the current temperature (°C): "))

if temperature > 30:
    print("It's hot outside! Stay hydrated.")
elif 20 <= temperature <= 30:
    print("The weather is pleasant.")
elif 10 <= temperature < 20:
    print("It's a bit chilly. You might need a jacket.")
else:
    print("It's cold! Dress warmly.")
