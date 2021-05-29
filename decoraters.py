# Decorators are used to modify functionality of function
# Here we change normal add frunction to add 2 tuples

import functools


def point_add_decorator(func):
    @functools.wraps(func)
    def point_add(*args, **kwargs):
        # print(type(args[0]))
        if type(args[0]) == type((1, 2)):
            x = func(args[0][0], args[1][0])
            y = func(args[0][1], args[1][1])
            return (x, y)
        elif type(args[0]) == type(1) or type(args[0]) == type(1.1):
            r = func(*args, **kwargs)
            return r
        else:
            raise TypeError("Type of aurgument not correct")

    return point_add


@point_add_decorator
def add(x, y):
    return x + y


a = 2.2
b = 4.1
print(type(a))
result = add(a, b)
print(result)

p1 = tuple([a, b])
p2 = (1, 2)

result = add(p1, p2)
print(result)

# add functools.wrap to preserver identity if not it will take identity of wrapper functions
print(add.__name__)
print(help(add))
