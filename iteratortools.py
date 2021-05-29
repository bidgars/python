# itertools: product, permutations, combinations, accumulate, groupby, and infinite Iterator

from itertools import product

print("--- product ---")
a = [1, 2]
b = [3, 4]
p = product(a, b)
print(list(p))

p = product(a, b, repeat=2)
print(list(p))

from itertools import permutations

print("--- permutations ---")
a = [1, 2, 3]
p = permutations(a)
print(list(p))
p = permutations(a, 2)
print(list(p))

from itertools import combinations

print("--- combinations ---")
a = [1, 2, 3, 4, 5]
c = combinations(a, 2)
print(list(c))

from itertools import accumulate
import operator

print("--- accumulate ---")
a = [1, 2, 3, 4, 5]
ac = accumulate(a)
print(list(ac))

ac = accumulate(a, func=operator.mul)
print(list(ac))

from itertools import groupby

print("--- groupby ---")


def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4, 5]
groupobj = groupby(a, key=smaller_than_3)
for key, value in groupobj:
    print(key, list(value))

groupobj = groupby(a, key=lambda x: x <= 3)
for key, value in groupobj:
    print(key, list(value))

items = [
    {"name": "apple", "type": "fruit"},
    {"name": "cake", "type": "desert"},
    {"name": "pinaple", "type": "fruit"},
    {"name": "orange", "type": "fruit"},
    {"name": "bitroot", "type": "vegies"},
]
groupobj = groupby(items, key=lambda x: x["type"])
for key, value in groupobj:
    print(key, list(value))

print("--- infinite iterator ---")

from itertools import count, cycle, repeat

print("--- count ---")

for i in count(10, 2):
    print(i)
    if i > 50:
        break

a = [1, 2, 3]
for i in cycle(a):
    print(i)
    if i > 2:
        break

a = [1, 2, 3, 4]
for i in repeat(1, 14):
    print(i)
    if i > 5:
        break
