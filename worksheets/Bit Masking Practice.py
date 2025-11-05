a = (1 << 4)
b = a
c = 0b100

print(a)
print(bin(a))
a = ~(a >> 1)
print(bin(a))
print(a)
print(bin(a & b))
print(c)