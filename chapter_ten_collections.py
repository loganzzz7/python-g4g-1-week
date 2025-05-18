# COLLECTIONS
# OrderedDict
# syntax OrderedDict()
# dictionary subclass that remembers the order in which keys were first inserted
# the only difference between dict() and OrderedDict() lies in their handling of key order
# after python 3.7 => dict() also maintains key order => OrderedDict() not necessary unless working with older versions of python
# now both but OrderedDict() maintains the order in which keys are added
# order of insertion is preserved => first inserted = first index of dict

# key val update; key order => if the value of a key is changed, the position of the key remains the same in OrderedDict()
# and now also in dict()
# e.g. =>
from collections import OrderedDict
print("before")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
print("after")
od['c'] = 5
for key, value in od.items():
    print(key, value)
# before
# a 1
# b 2
# c 3
# d 4
# after => adjusting value of c does not change it's key index in dict == now same for dict()
# a 1
# b 2
# c 5
# d 4

# equality comparison in dict order
# OrderedDict() can be compared for equality not only based on values but also order insertion 
# => compares both values and insertion order
# e.g. =>
dict_one = {"a": 1, "b": 2, "c": 3}
dict_two = {"c": 3, "b": 2, "a": 1}
print(dict_one) # => {'a': 1, 'b': 2, 'c': 3}
print(dict_two) # => {'c': 3, 'b': 2, 'a': 1}
print(dict_one == dict_two) # => true

od_one = OrderedDict({"a": 1, "b": 2, "c": 3})
od_two = OrderedDict({"c": 3, "b": 2, "a": 1})
print(od_one) # => OrderedDict({'a': 1, 'b': 2, 'c': 3})
print(od_two) # => OrderedDict({'c': 3, 'b': 2, 'a': 1})
print(od_one == od_two) # => false!!

# IMPORTANT!!
# dict() does not compare both key vals and insertion order
# table:
# type              preserves order         comparison
# = dict()          YES                     ONLY VALS
# = OrderedDict()   YES                     VALS AND KEY ORDER

# Defaultdict
# Counters
# Heapq
# Deque