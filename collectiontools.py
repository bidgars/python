# collections: Counter, namedtuple, OrderedDict, defaultdict, deque

# ---------------------------------------------------------------Counter
from collections import Counter, defaultdict

print("------------ Counter: counts number of elements from list in to dict ----------")
a = "aaaaaaaabbbbbbcccc"
mycounter = Counter(a)
print(mycounter)
print(mycounter.keys())
print(mycounter.values())
print(mycounter.most_common(1))
print(mycounter.items())
print(mycounter.most_common(1)[0][0])
print(list(mycounter.elements()))

# ---------------------------------------------------------------NamedTuple
from collections import namedtuple

print("------------ Named Tuple: creates a separate class of tuples ----------")
point = namedtuple("Point", "x,y")
pt = point(1, -4)
print(pt.x, pt.y)

# ----------------------------------------------------------------OrderedDict

from collections import OrderedDict

print("---- Ordered Dictionary: remembers order in which elements were inserted ")
d = OrderedDict()
d["a"] = 3
d["c"] = 1
d["b"] = 2
print(d)

print("python 3.7 onwards normal dict also remembers order")
d = {}
d["a"] = 3
d["c"] = 1
d["b"] = 2
print(d)

# ---------------------------------------------------------------defaultdict

from collections import defaultdict

print("----- defaultdict: returns default value if the key is not present ")
d = defaultdict(int)
d["a"] = 3
d["b"] = 2
print(d["c"])

d = defaultdict(float)
print(d["c"])

# ---------------------------------------------------------------deque
from collections import deque

print("------ deque is Double Ended QUEue")
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.appendleft(1)
print(d)

d.popleft()
print(d)
d.pop()
print(d)

d.extendleft([5, 6, 7])
print(d)
d.reverse()
print(d)

d.rotate(-1)
print(d)
