myset = {1, 2, 3, 4, 5, 6}
print(myset)

myset = set([1, 2, 3, 4, 5, 6])
print(myset)

myset = set("Hello")
print(myset)

myset = {}
print(type(myset))

myset = set()
print(type(myset))

myset.add(2)
myset.add(3)
print(myset)

# myset.remove(4)
myset.remove(3)
myset.add(3)
myset.discard(4)
print(myset.pop())
print(myset)
myset.add(1)
myset.add(1)

print(myset)

for x in myset:
    print(x)

if 1 in myset:
    print("1 present")
else:
    print("1 absent")

# Clear & refill set
myset.clear()
odd = set()
evn = set()
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23}

for i in range(0, 25):
    if i % 2 == 0:
        evn.add(i)
    else:
        odd.add(i)

print("Odds: \n", odd)
print("Evens: \n", evn)

myset = evn.union(primes)
print("Union with Primes: \n", myset)

myset = odd.intersection(primes)
print("Intersection with primes:\n", myset)

# Subscript & Slicing is not possible in sets
# evn = myset[1::2]
# print(myset[2])

myset = odd.difference(primes)
print("difference with primes:\n", myset)

primes.update(odd)
print("primes update with odds:\n", primes)

primes.difference_update(odd)
print("above difference_update with odd:\n", primes)

print(evn.issuperset(primes))
print(primes.issubset(evn))

# Additions doesnt work use union & difference functions instead
# setA = myset + primes

setA = myset.union(primes)
print(setA)

setB = setA
setA.add(3)

print(setA, setB)

setB = setA.copy()
setB.add(4)
print(setA, setB)

fs = frozenset([1, 2, 3])
print(fs)
# Frozen sets are not changable
# fs.add(2)
