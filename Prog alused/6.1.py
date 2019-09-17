import math

r = float(input("Sisesta ringi raadius: "))
u = 2 * math.pi * r
s = math.pi * r**2
print("Ringi ümbermõõt on: " + str(round(u, 4)) + " ja pindala on: " + str(round(s,4))) 
