n = int(input("Enter a number: "))
i = int(input("Enter bit position (0-based): "))


set_bit = n | (1 << i)
print("After setting bit:", set_bit)

clear_bit = n & ~(1 << i)
print("After clearing bit:", clear_bit)

toggle_bit = n ^ (1 << i)
print("After toggling bit:", toggle_bit)

is_set = (n & (1 << i)) != 0
print("Is bit set?", "Yes" if is_set else "No")
