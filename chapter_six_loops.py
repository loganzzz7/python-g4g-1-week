# FOR LOOP
# used to iterate lists tuples strings and ranges
# can be used to iterate over any thing that is iterable => dictionary
# e.g. => set s
s = ["one", "two", "three"]

# for loop doesn't need to init iterator (no int i = 0 like in C)
for i in s:
    print(i) #this prints the index values of s not just index

# strings are also iterable in python:
a = "string"

# for i in a:
#     print(i) #prints each string in a => string treated as an array of bytes

# CONTROL STMTS
# continue exits conditional loop and returns to outer loop
# => e.g.
# for i in a:
#     if i == "t" or i == "g":
#         print("in if")
#         continue
#     print(i)

# break exits entire for loop
# => e.g.
# for i in a:
#     if i == "n":
#         break
#     print(i)

# print("outside of for: " + i)

# pass is used as stand in for code to be implemented later
# python doesn't allow for empty loops => for (int i = 0; i < n; i++) { // can be empty in c }
for i in a:
    # code to be later implemented
    pass

# FOR ELSE:
# e.g. =>
b = [1, 2, 3, 4, 5, 6]
for i in range(1, 5): #range(i, j) from i to j => j is excluded
    print(i)
else:
    print("\nfor loop done")

# can use enumerate with for loop:
# ENUMERATE => enumerate() -- this adds a counter to each item in an iterable; 0 index
# syntax -> 
# enumerate(iterable, start index --default = 0) => returns an iterator with index and elt pair from og iterable
# return structure: (index, val of elt)

for i, j in enumerate(a): #i = index; j = val of elt => index given as an INT not STR
    print("index: " + str(i), "val: " + j)
# index: 0 val: s
# index: 1 val: t
# index: 2 val: r
# index: 3 val: i
# index: 4 val: n
# index: 5 val: g

# to iterate over dict => for key, val in dict.items(): --each item in dict has key val pair

# WHILE
# while(condition):
#   stmt
# same logic in using continue, break, else

# LOOP CTRL STMT
