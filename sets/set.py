# Sets: unordered, mutable, no duplicates

myset = {1, 2, 3, 1, 2}
print(myset)

myset = set([1, 2, 3])
print(myset)

myset = set("Hello")
print(myset)
print(type(myset))

myset = {} # we need to use set method to create empty set
print(type(myset))

myset = set({})

myset.add(1)
myset.add(2)
myset.add(3)
print(myset)

myset.remove(3)
print(myset)

myset.discard(2)    # if no element in the set no error will be rised
print(myset)

myset.clear()
print(myset)

myset = set([1, 2, 3])
print(myset.pop()) # Delete first element

for i in myset:
    print(i)

if 2 in myset:
    print("Yes")

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)   # union will combine elements from both sets without duplicates
print(union)

intersection = odds.intersection(primes)    # Get the elements when they appear in both sets
print(intersection)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diff = setA.difference(setB)
print(diff)

diff2 = setA.symmetric_difference(setB) # Get the elements not included in other sets
print(diff2)

#setA.update(setB)
print(setA)

#setA.intersection_update(setB)  # only elements existing in both sets
print(setA)

#setA.difference_update(setB)    # removes elements found in second set
print(setA)

setA.symmetric_difference_update(setB)  # removes elements found in both sets
print(setA)

setC = {1, 2, 3, 4, 5, 6}
setD = {1, 2, 3}

print(setC.issubset(setD))  # Is all elements in setB are in setC?
print(setD.issubset(setC))

print(setC.issuperset(setD)) # Is setC contains all elements from setD? if yes it is superset

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
print(setA.isdisjoint(setC))    # Return True if two sets have a null intersection.

#setB = setA
setB = setA.copy()
# or
#setB = set(setA)
setB.add(7)
print(setA)
print(setB)

# Frozenset - you cant modify the set after declare it
a = frozenset([1, 2, 3, 4])
print(a)

a.add(7)
a.remove(7)
print(a)