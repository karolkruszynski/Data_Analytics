# Lists: ordered, mutable, allows duplicate elements
mylist = ["banana", "cherry", "apple"]
print(mylist)

# Refer to Index
print(mylist[0])

# Creating Empty List
mylist2 = list()
print(mylist2)

# Iterating through list
for i in mylist:
    print(i)

# Checking for element in list
if "banana" in mylist:
    print("yes")
else:
    print("no")

# Length of list
print(len(mylist))

# Add element in to the list
mylist.append("lemon")
print(mylist)

# Add element in specify position in list
mylist.insert(1, "blueberry")
print(mylist)

# Delete and show last element in the list
item = mylist.pop()
print(item)

# Remove element from list
item2 = mylist.remove("cherry")
print(item2) # We don't see which element it was

# Delete ALL elements in the list
#mylist.remove()

# Reverse list
mylist.reverse()
print(mylist)

numlist = [4, 3, 1, -1, -5, 10]
numlist.sort()
print(numlist)

sorted_list = sorted(numlist)
print(sorted_list)

mylist3 = [0] * 5
print(mylist3)

mylist4 = [1, 2, 3, 4, 5]
new_list = mylist3 + mylist4
print(new_list)

# Slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
print(a)
# Step
b = mylist[::2]
print(b)

# Fast Reversing list
c = mylist[::-1]
print(c)

# Copying
list_org = ["banana", "cherry", "apple"]
list_cpy = list_org
list_cpy.append("lemon")
print(list_org)     # Modify list_cpy also modify list_org
print(list_cpy)

# Actually copying
list_cpy2 = list_org.copy()
print(list_cpy2)
# or
list_cpy2 = list(list_org)
# or
list_cp2 = list_org[:]

# LIST COMPREHENSION
mylist_num = [1, 2, 3, 4, 5, 6]
b = [i*i for i in mylist_num]
print(mylist_num)
print(b)