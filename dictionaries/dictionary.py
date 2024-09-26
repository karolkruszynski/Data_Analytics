# Dictionary: Key-Value pairs, Unordered, Mutable

mydiction = {
    "name": "Max",
    "age": 28,
    "city": "New York"
             }
print(mydiction)

mydiction2 = dict(name="Mary", age=27, city="Boston")   # no need to use "" for Key
print(mydiction2)

# Calling Key Value
value = mydiction["name"]
print(value)

# Adding new Key-Value pair
mydiction["email"] = "max@xyz.com"  # This over-write if Key Value exist
mydiction2["email"] = "max2@xyz.com"
print(mydiction)

# Deleting Key
del mydiction2["name"]
print(mydiction2)
# or
mydiction2.pop("age")
print(mydiction2)
# or delete last inserted Key
mydiction2.popitem()
print(mydiction2)

# Searching
if "name" in mydiction:
    print(mydiction["name"])

try:
    print(mydiction["lastname"])
except:
    print("Error")

# Iterating Keys
for key in mydiction:
    print(key)
# or
for key in mydiction.keys():
    print(key)

# Iterating Value
for value in mydiction.values():
    print(value)

# Iterating Both
for key, value in mydiction.items():
    print(key, value)

# Copy Dictionary
mydiction_cpy = mydiction
print(mydiction_cpy)
# copy like this point to the same dictionary inside our memory like in lists
#mydiction_cpy["email"] = "max@123.com"
print(mydiction_cpy)
print(mydiction)

# we need to do this
mydiction_cpy = mydiction.copy()
# or
mydiction_cpy = dict(mydiction)
print(mydiction_cpy)

# Merge two dictionaries
mydiction = {
    "name": "Max",
    "age": 28,
    "city": "New York"
             }
mydiction2 = dict(name="Mary", age=27, city="Boston")

mydiction.update(mydiction2)    # Over-write the data inside
print(mydiction)

# Key types
mydiction3 = {
    3: 9,
    6: 36,
    9: 81
             }
print(mydiction3)

#value = mydiction3[0]   # we need to point to the actual Key soo, 3 not index 0 for int as a Key
#print(value)
value = mydiction3[3]
print(value)

mytuple = (8, 7)
mydiction4 = {  # Tuple is possible as a Key but not a List bc lists are mutable and unhashable
    mytuple: 15
}
print(mydiction4)