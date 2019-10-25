fruit = ["banaan", "maasikas", "õun"]
print(fruit[0])
fruit.append("pirn")
print(fruit[-1])
fruit[1] = "kirss"
print (fruit)
if "õun" in fruit:
    print("Õun is in list fruit")
else:
    print("Õun is not in list fruit")
print (len(fruit))
fruit.remove("kirss")
fruit.reverse()
fruit.sort()
print(fruit)