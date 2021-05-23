#! python

a = 10
b = 20
print(a + b)
if a > b:
    print("a>b")
elif b > a:
    print("b>a")
else:
    print("not ok")

# -------------list

shoplist = ["apple", "grape", "orange", "banana", "papaya"]
mylist = shoplist[-1:-4:-1]
print(type(mylist))

# ----------------tupple
mytupple = ("Hello", [8, 9, 6], (1, 2, 3))
print(mytupple[1])
mytupple[1][1] = 10
print(mytupple[0].index("o"))
print(type(mytupple))

# ----------------dictionary


mycontact = {"suni": "986", "mani": "1234"}
print("Overriden ", mycontact["suni"])

mycontact = {"suni": ["986", "suni"], "mani": "1234"}
print(mycontact["suni"][1])

for a in 1, 2, 3, "asd":
    print(a)

name = input("Your Name? ")
print("Hello ", name)
