# Strings: ordered, immutable, text representatins

mystr = "I'm a programmar"
print(mystr)
mystr = """Hello 
New World"""
print(mystr)
mystr = """Hello \
New World"""
print(mystr)
mystr = "New\nLine"
print(mystr)
mystr = "I'm a programmar"
print(mystr)

for i in range(len(mystr) - 12):
    print(mystr[i])

print(mystr[3])
# String item assignments are not supported
# mystr[0] = "F"

# Slicing
mysubstr = mystr[::-1]
print(mysubstr)

totalstr = mystr + " but copy-paste"
print(totalstr)

for x in "Hello":
    print(x)

if "but" in totalstr:
    print("in Yes")
else:
    print("in no")

mylist = totalstr.split(" ")
print(mylist)

totalstr = ":".join(mylist)
print(totalstr)

# Formating .format, f strings
var = "Sunil"
dec = 2.2
mystr = "{} is {:.2f}".format(var, dec)
print(mystr)
mystr = f"{var} is {dec}"
print(mystr)
