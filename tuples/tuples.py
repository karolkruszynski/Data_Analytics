# Tuples: ordered, immutable, allows duplicate elements
mytuple = "Max", 28, "Karol"
print(mytuple)

# Single element in tuple
mytuple = ("Max",)
print(mytuple)

# Tuple function
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)

# Indexing
item = mytuple[2] # or negative index
print(item)

# Tuple is immutable
#mytuple[0] = "Tim"

# Iterating
for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("Yes")
else:
    print("No")

# Counting, searching
my_tuple = ('a', 'p', 'p', 'l', 'e')
print(len(my_tuple))
print(my_tuple.count('p'))
print(my_tuple.index('p'))  # first matching element in tuple

# Changing
mylist = list(my_tuple)
print(mylist)

my_tuple2 = tuple(mylist)
print(my_tuple2)

# Slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
b = a[:5]
print(b)
b = a[2:]
print(b)
b = a[::2]
print(b)

# Reversing
b = a[::-1]
print(b)

# Unpacking
my_tuple = "Max", 28, "Boston"

name, age, city = my_tuple  # Variables match with count of elements in tuple
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple  # * contains all elements between first and last item assign to i1 and i3 and converted to a list
print(i1)
print(i3)
print(i2)

# Memory size tuple vs list
import sys
my_list = [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

# Time to create tuple vs list
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
