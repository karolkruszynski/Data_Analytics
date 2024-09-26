#filepath = "C:/user/dane.txt" #absolute path
filepath = "data.txt" #relative path

f = open(filepath, "r")
print(f.read())

# options: r-read, w-write, a-append, b-binary

f = open(filepath, "r", encoding="utf-8") #polish symbols
print(f.read())
# after reading the value store in f variables will be "delete"
print(f.read())
# new read
f = open(filepath, "r", encoding="utf-8")
print(f.read(3))    # first 3 symbols
print(f.read())     # rest of the remaining symbols

# storing text
f = open(filepath, "r", encoding="utf-8")
text = f.read()
print(f.read()) #empty bc all of data is store in variable text
print(text[:5])

# readline
f = open(filepath, "r", encoding="utf-8")
print(f.readline()) # first line
print(f.readline()) # second line

# iterating lines
f = open(filepath, "r", encoding="utf-8")
for line in f:
    #print(line)
    print(line, end="") #removing spacing

# redlines to list
f = open(filepath, "r", encoding="utf-8")
lines = f.readlines()
print(f"\n{lines}")

# char by char
f = open(filepath, "r", encoding="utf-8")
znak = f.read(1)
while znak:
    print(znak)
    znak = f.read(1)

# writing data
f = open("data_w.txt", "w") # w - write
print(f.write("Text"))  # we get back a len() of the text we insert into file
print(f.write("\nSecond Line"))
print(f.write("\nThird Line"))
# or
lines = ["\nThird Line", "\nForth Line"]
f.writelines(lines) # writing many lines store in list

# pro tip
lines = ['pierwsza', 'druga', 'trzecia']
lines = [line + "\n" for line in lines] # adding newline to all elements of the list
print(lines)

# a - append
f = open("data_w.txt", "a")
f.write("\nAppending")

# remember to close the file bc the file will be open in status for other applications
f.close()

# or more Pythonic way
with open("data_w.txt", "a") as f:
    f.write(" we don't need to close this")
#f.write("test") # this throw error

# reader and writer
with open(filepath, "r") as reader, open("data_w.txt", "w") as writer:
    text = reader.read()
    writer.write(text)

# checking if file is closed
f = open(filepath, "r")
print(f.closed)
f.close()
print(f.closed)

# checking open type
f = open(filepath, "r")
print(f.readable(), f.writable())

f = open(filepath, "w")
print(f.readable(), f.writable())

f = open(filepath, "r+")
print(f.readable(), f.writable())
