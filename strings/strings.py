# Strings: ordered, immutable, text representation

my_string = "Hello"
print(my_string)

#my_string = "I'm programmer"
#print(my_string)

my_doc = """
Multiple Lines for 
documentation
"""
print(my_doc)

char = my_string[0]
print(char)

#my_string[0] = 'h'  # Strings are immutable

# Slicing
substring = my_string[1:5]
print(substring)

substring = my_string[:5]
print(substring)

substring = my_string[0:]
print(substring)

substring = my_string[::-1] # Reversing string
print(substring)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for i in greeting:
    print(i)

if 'e' in greeting:
    print("Yes")
else:
    print("No")

my_string = '   Hello World   '
print(my_string)
my_string = my_string.strip()   # deleting whitespaces
print(my_string)

my_string = "Hello World"
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("Hello"))
print(my_string.endswith("l"))
print(my_string.find("o"))  # Return index number
print(my_string.find("o0")) # -1 if not find
print(my_string.count("l"))
print(my_string.replace("World", "Universe"))

my_string2 = "how are you doing"
my_list = my_string2.split()    # looks for space for def.
print(my_list)

new_string = " ".join(my_list)  # from list to string
print(new_string)


from timeit import default_timer as timer
my_list2 = ["a"] * 100000

# bad choose - very costly operation
start = timer()
my_string3 = ""
for i in my_list2:
    my_string3 += i
stop = timer()
print(stop - start)

# good
start = timer()
my_string3 = "".join(my_list2)
stop = timer()
print(stop - start)

# &, .format(), f-strings
var = 3.1234567
var2 = 6
my_string4 = "The variable is %.2f" % var       # %s - strings  %d - intiger  %f - float (.X number after dot)
print(my_string4)

# better way
my_string4 = "The variable is {:.2f} and {}".format(var, var2)
print(my_string4)

# the best way 3.6 or newer
my_string4 = f"The variable is {var:.2f} and {var2*2}"
print(my_string4)
