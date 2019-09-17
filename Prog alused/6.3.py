n = (input("Sisesta täisarv vahemikus 1-9: "))
answer = int(n) + int((n + n)) + int((n + n + n))
print (n + " + " + (n + n) + " + " + (n+ n+ n) + " = " + str(answer))