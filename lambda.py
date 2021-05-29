# lambda arguments : expression
add10 = lambda x: x + 10
print(add10(1))

mult = lambda x, y: x * y
print(mult(2, 7))

points = [(1, 2), (15, 1), (5, -1), (10, 4)]
print(points)
print(sorted(points))

points_sorted = sorted(points, key=lambda x: x[1])
print(points_sorted)

points_sorted = sorted(points, key=lambda x: x[0] + x[1])
print(points_sorted)

# map(func,sq)
a = [1, 2, 3, 4, 5]
b = list(map(lambda x: x * 2, a))
print(b)

b = [x * 2 for x in a]
print(b)

# filter(func, seq)
b = list(filter(lambda x: x % 2 == 0, a))
print(b)
b = [x for x in a if x % 2 == 0]
print(b)

# reduce (func, seq)
from functools import reduce

prod = reduce(lambda x, y: x * y, a)
print(prod)
