mydict1 = {"name": "Max", "age": 28, "city": "Boston"}
print(mydict1)

mydict2 = dict(name="Marry", age=24, city="New York")
print(mydict2)

value = mydict1["name"]
print(value)

mydict2["email"] = "max@xyz.com"
mydict2["email"] = "newmax.xyz.com"
print(mydict2)

# deleting item
del mydict2["name"]
print(mydict2)

mydict2.pop("age")
print(mydict2)

mydict2.popitem()
print(mydict2)

if "name" in mydict1:
    print("Name element is present")

if "Max" in mydict1.values():
    print(mydict1["name"])

try:
    print(mydict2["city"])
except:
    print("No Error")

try:
    print(mydict2["name"])
except:
    print("Error")

for key, value in mydict1.items():
    print(key)
    print(value)

mydict3 = mydict1
print(mydict3)

mydict3["email"] = "max@xyz.com"
print(mydict1)
print(mydict3)

mydict3 = mydict1.copy()
mydict3["postcode"] = "MYDICT3"
mydict4 = dict(mydict1)
mydict4["postcode"] = "MYDICT4"

print(mydict1, mydict3, mydict4)

mydict = {3: 9, 6: 36, 9: 81}
print(mydict)
print(mydict[6])

mytuple = (4, 5)
mydict = {mytuple: 20}
print(mydict)

# TypeError: unhashable type: 'list'
# mylist = [4, 5]
# mydict = {mylist, 20}
