# SYNTAX
# python uses indentation to define blocks
if (2 > 1):
    print("yes")
print("\nout of loop")

# no need to declare types in python => auto determines types
# vars in python are named references to objects in memory -> & 
a = 10
b = "hello"
c = ["1", "2"]
d = ("1", "2uple")

print(type(a))
print(type(b))
print(type(c))
print(type(d))
# <class 'int'>
# <class 'str'>
# <class 'list'>
# <class 'tuple'>

# python identifiers -> snake_case NOT camelCase
# unique names assigned to vars, funcs, classes, other entities 
# e.g. first_name

# list of keywords reserved (unabled to be used as var names):
# False       await       else       import       pass  
# None        break       except     in           raise 
# True        class       finally    is           return
# and         continue    for        lambda       try  
# as          def         from       nonlocal     while
# assert      del         global     not          with  
# async       elif        if         or           yield

'''
multiline comment with triple apostrophes
'''

# use \ to break lines for readability but stays as one line => explicit line continuation
long_line = "super super super super super super super " \
            "long line"
print(long_line)

long_add = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        7 + 8 + 9
print(long_add)

# python auto supports implicit line continuation when defining lists, tuples, dicts
# e.g. list => prints as [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = [1, 2, 3, 
           4, 5, 6, 
           7, 8, 9
           ]
print(numbers)

# fstrings => uses f to signify formatting conventions used
# >>> print("Pi to two decimals is ", round(3.14159, 2), ".", sep="")
# Pi to two decimals is 3.14.
# >>> print(f"Pi to two decimals is {3.14159:.2f}.") -> uses .2f (2 decimal float) to format
# Pi to two decimals is 3.14.

print("Pi to two decimals is {3.14159:.2f}.") # -> Pi to two decimals is {3.14159:.2f}.
print(f"Pi to two decimals is {3.14159:.2f}.") # -> Pi to two decimals is 3.14.

# {3.14159:.2f} => formatting convention
# %s %i ... c formatting conventions



# DATA TYPES
# everything is an object in python => therefore python data types are classes and variables are instances
# a = 10 => a is an instance of the int class
# data types listed:
# numeric: int, float, complex
# int: pos or neg whole numbers no INT_MAX or INT_MIN
# float: decimal number -> can use e followed by number for scientific notation
# complex: real + imaginary -> 2 + 1j
a_int = 1
b_float = 1.2
f_complex = 2 + 1j
print(type(a_int)) # <class 'int'>
print(type(b_float)) # <class 'float'>
print(type(f_complex)) # <class 'complex'>



# sequence: string, list, tuple
# strings: arrays of bytes representing unicode characters => there is no char type in python -> each character is string of length one
# strings can be created using single quotes ' ', double " ", or triple ''' ''' 
# lists: can have items of all types => supports negative indexing as well
# tuples: same as lists but immutable
c_string = "hello"
print(c_string[-1]) #string has 0-index => -1 wraps around to back
d_list = ["h", "e", "l", "l", "o", 1, 2]
print(d_list[-1])
# print(d_list[-8]) => can only wrap around once
g_tuple = ("one_item_tuple", )
h_tuple2 = ("one", "two", [2, 3, 4])
print(h_tuple2[1])
print(h_tuple2[2])
i_tuple_one_list = ([1, 2, 3, 4])
print(i_tuple_one_list[-1]) #accesses last index in tuple item



# mapping: dict
# collection of data vals => mapped
# has key: val
l_dict = {1: "first_val", 2: "second_val", 3: "third_val"}
m_dict = dict({"first": "first_val_m", "second": "second_val_m", "third": "third_val_m"})
print(l_dict) # {1: 'first_val', 2: 'second_val', 3: 'third_val'}
print(m_dict) # other decl form

print(l_dict.get(2)) #access via get => second_val
print(m_dict["first"]) #access via key => first_val_m
print(m_dict.get("third")) # => third_val_m



# boolean: bool
# bool: must be True or False cannot be true or false
j_bool = True
print(type(j_bool)) #<class 'bool'>



# set: set, frozenset
# set: unordered collection of items that is iterable, mutable, and no dup elts
e_set = set({"s", "e", "t", "e", "t"})
k_set = set("sett")
print(e_set) #{'s', 't', 'e'} => unordered so prints diff order everytime
print(k_set) #{'t', 'e', 's'} => does not print dups
# since sets have no ordering -> must use loop to access elts in set => e.g.
for i in e_set:
    print(i, end=" ")
    print()
# everytime set vals printed in diff order since sets have no order

print("t" in e_set) #checks if "t" exists in e_set print true or false

# binary: bytes, bytearray, memoryview



# PRACTICE
# list
z_list = ["a", "b", "c"]
z_list.append("d") # => add d at end
z_list.remove("a") # => rmv (input)
print(z_list) # ['b', 'c', 'd']

# print tuple
y_tuple = (1, 2)
print("tuple_first: ", y_tuple[0], sep = '') # => tuple_first: 1
print("tuple_second: ", y_tuple[-1], sep = '') #neg index => tuple_second: 2
 