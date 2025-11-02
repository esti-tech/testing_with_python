print("hello! this is a code for unit converting! ")
print("select for which units to be converted to!")
print("1: celcious to fharenite")
print("2: fahrenite to celicious")
print("3: celcious to kelvin")
print("4: miles  to killometers")
print("5: meters  to milimeteres")
print("6: milimetres to kilometers")
operation = input("Enter your choice: ")
if operation == "1":
    celcious_to_fharenite = input("Enter your unit in celicius: ")
    ctof = (float(celcious_to_fharenite)) * 1.8 + 32
    print(f"your converted unit is{ctof} °fahrenite")
elif operation == "2":
    fahrenite_to_celicious = input("Enter your unit in fahrenite: ")
    ftoc = (float(fahrenite_to_celicious) - 32) / 1.8
    print(f"your converted unit is{ftoc} <UNK>celcious")
elif operation == "3":
    celcious_to_kelvin = input("Enter your unit in celcious: ")
    ktoc = float(celcious_to_kelvin) + 273.15
    print(f"your converted unit is{ktoc} <UNK>kelvin")
elif operation == "4":
    kilometers_to_milimetres = input("Enter your unit in kilometers: ")
    ktom = float(kilometers_to_milimetres) * 1000000
    print(f"your converted unit is{ktom} milimetres")
elif operation == "5":
    meters_to_milimetres = input("Enter your unit in meters: ")
    mtomil = float(meters_to_milimetres) * 1000
    print(f"your converted unit is{mtomil} milimetres")
elif operation == "6":
    milimetres_to_kilometers = input("Enter your unit in milimetres: ")
    mtokil = float(milimetres_to_kilometers) * 10 ** -6
    print(f"your converted unit is{mtokil} kilometers")
else:
    print("invslid entry! ")