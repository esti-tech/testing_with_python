# Parity and Power Detector.py

print("Let’s find out if your number is even, odd, or a power of two!")

n = int(input(" any positive number: "))

if n % 2 == 0:
    print(n, "is an even number.")
else:
    print(n, "is an odd number.")

if n > 0 and (n & (n - 1)) == 0:
    print("Wow! That’s a power of two ")
else:
    print("Nope, that’s not a power of two.")

print("Done. That was easy, right?")
