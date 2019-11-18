
me = {
    "fname": "Robin",
    "lname": "Kukk",
    "birthyear": 2001,
    "birthmonth": "Feburary",
    "dessert": "bruh"}

print (me.get("birthmonth"))
print (me["birthmonth"])

me["dessert"] = "bruh 2"

print ("**************************")

for x in me:
    print (x)
    
print ("**************************")

for x in me:
    print (me[x])
    
print ("**************************")

if "isikukood" in me:
    print ("the value Isikukood exists")
else:
    print ("the value Isikukood does not exist")  

print(len(me))

me["height"] = 187

print (me.get("height"))

me.pop("birthyear")
print ("**************************")




