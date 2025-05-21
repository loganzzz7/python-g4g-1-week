# LISTS
# built dynamic size array => elts can be appended or removed
# can store any type of item (can also store another list) [[li2], 2, "two"]
# list store references to elts (&elt) at contiguous loc while each item can be store in a diff position

# list => 
# can contain dups
# are mutable
# are ordered
# 0 index and ea item can be accessed via list[index] --supports neg indexing

# to create a list
# brackets: [items, items, items]
# use list() on another type of iterable: list((item, item, item)) --list() on a tuple ()
# can also do: a = [1] * 5 => [1, 1, 1, 1, 1]

# add to list:
# append: append(elt) => add elt to the end of the list
# insert: insert(pos index, elt) => add elt to pos index of the list
# extend: extend([1, 2, 3]) => used to add multiple elts to end of list

# update elt of a list:
# a[0] = "new" => updates elt of a list at index 0

# remove from list:
# remove: remove(elt) => remove first occurrence of elt from list
# pop: pop(index) => index is defaulted to last; if specified then removes the elt at index given from list
# del: del a[0] => this deletes the elt at index 0 from list => prev 2nd elt = new 1st elt

# NESTED LIST => list with lists e.g. =>
c = [
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 9]
]

print(c[1][0]) # => this prints the elt at the 0 index of the first index of list c
# 4



# TUPLE
# a collection of objs separated by commas in a () => same as list in accessing, indexing, nesting
# however; tuples are:
# IMMUTABLE

# concatenate two tuples via + operator => e.g.
tup1 = (1, 2, 3)
tup2 = ("one", "two", "three")
tup_conc = tup1 + tup2
tup_nested = (tup1, tup2)

print(tup_conc) # => (1, 2, 3, 'one', 'two', 'three')
print(tup_nested) # => ((1, 2, 3), ('one', 'two', 'three')) tuple of two tuples

# can also do * to create tuple of same item x times
x = 5
tup3 = (0,) * x
print(tup3) # => (0, 0, 0, 0, 0)

# TUPLE SLICING
# dividing tuples up => done via indexing method
tup4 = (1, 2, 3, 4, 5, 6, 7, 8)

print(tup4[1:]) # slices tuple into index 1 until end => (2, 3, 4, 5, 6, 7, 8)
print(tup4[1:4]) # slices tuple into index 1 until 4 (4 is not included) => (2, 3, 4)
print(tup4[1::4]) # slices tuple into index 1 and index 5 (4 is not included) => (2, 6)
print(tup4[::-1]) # prints tuple via reverse indexing => 
# starts at -1 which is the last elt and continues to the first 0 index pos => (8, 7, 6, 5, 4, 3, 2, 1)

# delete tup
# del tup

# length of tuple => len(tup) returns the length of a tuple
print(len(tup3)) # => 5

# convert list into tuple a = [1, 2, 3] => tuple(a) == (1, 2, 3)

# tuple in loop
tup5 = ("one_elt")
for i in range(5):
    tup5 = (tup5, )
    print(tup5)
print(tup5) # => ((((('one_elt',),),),),)

# ways to create tuple
# (): (1, 2, 3) => use () brackets to def tuple => if nothing in bracket then empty tuple
# ,: 1, 2, 3 => use , separation to def tuple
# tuple(): tuple(iterable) => converts to tuple
# (1, ): single elt tuple => must have comma or else it is not tuple

# tuple built in methods:
# index(val): returns index of where val is found in tuple
# count(val): returns how many elts with val in found in tuple

# tuple built in functions:
# all(): => returns true if all elts of the tuple are true
# any(): => returns true if any elts of the tuple are true
# len(): => returns the length of the tuple
# enumerate(): => returns enumerated object of tuple => object structure (index, val)
# max(): => reutrns the max number in tuple
# min(): => returns the min number in tuple
# sum(): => returns sum of numbers in tuple
# sorted(): => inputs elts in tuple and returns a new sorted list []
# tuple(): => converts iterable into tuple

# DIFF METHODS / FUNC BETWEEN TUPLE AND LIST:
# tuple cannot use: DUE TO IMMUTABILITY
# insert(), append(), remove(), pop(), clear(), sort(), reverse()

# tuples with immutable elts can be used as a key for dict
# iterating through a tuple is faster than a list

# DICTIONARIES
dict_a = {1: "one", 2: "two", 3: "three"}
print(dict_a) # => {1: 'one', 2: 'two', 3: 'three'}

dict_b = dict(a = "one", b = "two", c = "three") # cannot use numbers as name params => pretty much just var decl in dict()
print(dict_b) # {'a': 'one', 'b': 'two', 'c': 'three'}

# dicts are ordered
# dict keys are case sensitive
# keys must be immutable
# keys must be unique
# dictionary uses internal hashing => search, insert, delete == O1 constant time

# access elt in dict
# dict[key]: dict_a[1]
# dict.get(key): dict_a.get(2)

# add elt in dict
# dict[newkey] = "val"
# dict[key] = "new val" => updates val of key

# remove elt in dict
# del dict[key] => removes key pair at given key
# dict.pop(index) => remove key pair at given index
# key, val = dict.popitem()
# dict.clear() => clears entire dictionary

# iterating through dict:
# iterate keys
for key in dict_a:
    print(key)
# 1
# 2
# 3

# iterate vals
for val in dict_a.values():
    print(val)
# one
# two
# three

# iterate key, val pairs
for key, val in dict_a.items():
    print("key: " + str(key), "val: " + val)
# key: 1 val: one
# key: 2 val: two
# key: 3 val: three

# nested dicts:
dict_c = {1: "one", 2: "two", 3: {1: "one", 2: "two", 3: "three"}}
print(dict_c)
# {
# 1: 'one', 
# 2: 'two', 
# 3: {1: 'one', 2: 'two', 3: 'three'}
# }

# SET
# no duplicate elts => if try to insert new elt that alr exists => overwrites the prev
# unordered
# uses hashing => search, insert, delete done in constant time
# mutable => cannot change elt but can add and del
# can store elts of diff types

# defined via
# {}; set(); 

# frozen sets:
# IMMUTABLE => elts cannot be added or deleted
# created via frozenset()

# sets are a hash table
# => if multiple vals are at the same index => the index becomes a linked list

# add to a set
# set.add(elt) => returns a set with the added elt => there is no ordering in set!!!

# union of sets U
# => all of the shared elts in set_one and set_two and all of the diff elts == no dups
# this has a runtime of O(len(set_one) + len(set_two))
# methods:
# set_one.union(set_two): set_three = set_one.union(set_two)
# |: set_three = set_one | set_two => set_three

# intersection of sets ∩ \intersect in latex
# => all of the dup elts in set_one and set_two and nothing else => no dups
# this has a runtime of O( min( len(set_one), len(set_two) ) ) => length of shorter set
# methods:
# set_one.intersection(set_two): set_three = set_one.intersection(set_two)
# &: set_three = set_one & set_two

# difference of sets
# => difference between two sets
# runtime of set_one - set_two => O(len(set_one))
# methods:
# set_one.difference(set_two): set_three = set_one.difference(set_two)
# -: set_three = set_one - set_two

# clear a set => set.clear()

# supported operators:
# key in set
# key not in set
# s1 == s2
# s1 != s2
# s1 >= s2: s1 is superset of s2
# s1 <= s2: s1 is subset of s2
# s1 > s2: s1 is proper superset of s2
# s1 < s2: s1 is proper subset of s2
# s1 | s2: union of s1 and s2
# s1 & s2: intersection of s1 and s2
# s1 - s2: set of elts that is in s1 but not in s2
# s1 ^ s2: XOR => set of elts exclusively in s1 or s2