mylist = [4, 3, 1, -1, 10, -5]
print(mylist)

mylist.sort()
print(mylist)

mylist.append(44)

new_list = sorted(mylist, reverse=True)
print(new_list)

item = mylist.pop()
print(item)

print(mylist)

item = new_list.pop()
print(item)

new_list.remove(3)
print(new_list)

# new_list.remove(3)
# print(new_list)

mylist2 = [0] * 5
print(mylist)

mylist3 = [00, 12] + [4]

new_list = sorted(mylist + mylist2 + mylist3)
print(new_list.__len__())

print(new_list[::-1])

list_org = ["banana", "apple", "cherry"]
list_cpy = list_org

list_cpy.append("lemon")
print(list_org)
print(list_cpy)

list_cpy = list_org.copy()
list_cpy.append("newlemon")
print(list_org)
print(list_cpy)

a = [1, 2, 3, 4, 5, 6, 7]
b = [i * i for i in a]

print(a)
print(b)
