from typing import Text


mytuple = tuple(["Max", 26, "Boston"])
print(mytuple)

# Tuple are immutable
# mytuple[0] = "Tim"

name, age, city = mytuple

print(name + " is " + Text(age) + " years old stying in " + city)

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("Max is present")
else:
    print("No Max")

mytuple = ("a", "b", "c", "d", "e", "f")
print(len(mytuple))
print(mytuple.index("b"))
# print(mytuple.index("z"))

mylist = list(mytuple)
print(mylist)


a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
b = a[::2]
print(b)
b = a[::-2]
print(b)

x, *y, z = a
print(x)
print(y)
print(z)


# List has more size
import sys

mytuple = (0, 1, 2, "hello", True)
my_list = [0, 1, 2, "hello", True]
print(sys.getsizeof(mytuple), "bytes")
print(sys.getsizeof(my_list), "bytes")

# time taken - tuples (13.64) can be more efficient than list (67.69) sec
import timeit

print(timeit.timeit(stmt="[0,1,2,3,4,5,6]", number=1000000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5,6)", number=1000000000))
