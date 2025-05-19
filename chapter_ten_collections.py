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

# OrderedDict() reversal => does not natively support reverse() method
# reverse() method => this method reverses the iterable --supported by list; 
# however this does not return a new iterable, it just reverses the original iterable it is called on
# reversed() method => this method reverses the iterable --supported by OrderedDict() also by dict() since python 3.8
# this method DOES return a new iterable, the original iterable given in reversed order
# to reverse a dict() or OrderedDict() => e.g.
od_three = OrderedDict({1: "one", 2: "two", 3: "three"})
rod_three = OrderedDict(reversed(list(od_three.items()))) 
# reversed(od_three) => this only reverses iterator over the keys
# od_three.items() => returns a iterable object of dict's tuple key-val pairs
# list() => changes the iterable into a list => this is best practice because .items() only returns an iterator; not necessarily a list
# reversed() => returns a reversed list iterable => [(3, "three"), (2, "two"), (1, "one")]
# OrderedDict() => change list to OrderedDict() => takes list iterable and returns OD iterable
print(rod_three) # => OrderedDict({3: 'three', 2: 'two', 1: 'one'})

# popitem()
# syntax => .popitem() => returns the last inserted key-val pair => dict.popitem()
# useful for lifo ordering => e.g.
pod = OrderedDict([(1, "one"), (2, "two"), (3, "three")])
last_item = pod.popitem()
print(last_item) # => (3, 'three')

# move key order
# use move_to_end() method
# syntax => move_to_end(key, last=True) == move to end; move_to_end(key, last=False) == move to start
pod.move_to_end(1, last=True)
pod.move_to_end(2, last=False)
print(pod) # => OrderedDict({2: 'two', 1: 'one'})

# deleting and re-inserting in OrderedDict()
# deleting and re-inserting will push the inserted key-val to the back of the OD due to preserving insertion order
# deleting item => .pop(key)
pod.pop(1)
print(pod) # => OrderedDict({2: 'two'})
# re-inserting
# method one: dict[newkey] = val
# method two: dict.update([(key, val)])
pod[1] = "one"
pod.update([(5, "five")])
print(pod) # => OrderedDict({2: 'two', 1: 'one'}) => re-inserted elt ends up at the end of the dict
for key, val in pod.items():
    print(key, val)
# 2 two
# 1 one

# COLLECTIONS MODULE => OrderedDict() is a part of the collections module =>
# need to do from collections import OrderedDict
# REMEMBER: dict() is now same as OrderedDict; however, comparisons (==) of OrderedDict also accounts for key order
# time complexity of OD:
# search, insert: O(1)
# traverse, delete: O(n) => need to iterate n elts of dict 
# space complex: O(n)

# Defaultdict
# subclass of dict() -> provides a default val for nonexistent key in dict
# syntax defaultdict(default_factory) => default_factory = a function returning the default value for the dict defined
# if default_factory missing => returns a KeyError; Otherwise returns a dict obj that auto provides val for missing keys
# default_factory can be: int, str, list, or any other callable obj
# int: default = 0
# str: default = ""
# list: default = []
# can also be any function => lambda: "not present"
# e.g. =>
from collections import defaultdict
dd2 = defaultdict(lambda: "nonexistent")
dd2[1] = "one"
dd2.update([(2, "two")])
print(dd2) # => defaultdict(<function <lambda> at 0x100380400>, {1: 'one', 2: 'two'})
print(dd2[3]) # => nonexistent from lambda: "nonexistent"


# eliminates the need to check whether keys exist before using it
# when accessing a key that doesn't exist yet defaultdict auto creates it and assigns it a default val based on func provided
# need to specify the default val type when passing func --int set list
# e.g. =>
dd = defaultdict(list)
dd["fruits"].append("apple")
dd.update([("animals", ["cat"])])
print(dd) # => defaultdict(<class 'list'>, {'fruits': 'apple', 'animals': 'cat'})
print(dd["cars"]) # => [] == no KeyError

# regular_dict = {}
# regular_dict["fruits"] = ["apple"]
# print(regular_dict)
# print(regular_dict["cars"]) # => KeyError: 'cars'

# init via for => list
dd3 = defaultdict(list)
for i in range(3):
    dd3[i] = [i]
print(dd3) # => defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2]})
print(dd3[3]) # => go to default list = empty list ==> []

# int
dd4 = defaultdict(int)
a = [1, 2, 3, 4, 3, 4, 5, 2]
for i in a:
    dd4[i] += 1
    print(i)
    print(dd4[i])
    print("\nnext one: ")
print(dd4) # => defaultdict(<class 'int'>, {1: 1, 2: 2, 3: 2, 4: 2, 5: 1})



# Counters
# subclass of the dict class in the collections module => 
# used to count the occurrences of elts in an iterable or frequency of items in mapping
# syntax: Counter(any iterable or mapping with countable vars)
# can be used with:
# a sequence of items; dictionary containing keys and counts; keyword args mapping str names to counts
# returns a counter obj
# e.g. =>
from collections import Counter
b = [1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4]
ctr = Counter(b)
print(ctr) # => Counter({4: 7, 3: 6, 2: 5, 1: 4})
ctr1 = Counter([1, 2, 3, 4, 5])
ctr2 = Counter("hello")
ctr3 = Counter({1: 2, 2: 4, 3: 6})
print(ctr1) # => Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
print(ctr2) # => Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
print(ctr3) # => Counter({3: 6, 2: 4, 1: 2})
print(type(ctr1))

# accessing counter elts
print(ctr[1]) # => 4
print(ctr[4]) # => 7
# syntax => counterobj[elt] -> returns number of elt counted
# if elt ne -> ret 0

# updating counters
# counters can be updated by adding new elts or updating existing elts => use .update(new stuff)
# e.g. =>
ctr4 = Counter([2, 2, 2, 3, 3, 1, 0])
ctr4.update([0])
ctr4[0] = 0 # => sets the number of 0s in [] to be 0
print(list(ctr4.elements())) # => [2, 2, 2, 3, 3, 1]
print(ctr4) # => Counter({2: 3, 3: 2, 0: 2, 1: 1})

# counter methods:
# elements(): returns an iterator over elements repeating each as many times as it counts => elts are returned in arbitrary order
# e.g. =>
ctr5 = Counter([1, 1, 2, 2, 2, 3, 3, 3, 3])
items = list(ctr5.elements())
print(items)
print(ctr5.elements()) # => <itertools.chain object at 0x102ca4be0> => just an iterable not specifically a list!!!

# mostcommon(n): returns a LIST of the n most common elts and their counts from the most common to least 
# => if n not given then returns all
# e.g. =>
mc_ctr5 = ctr5.most_common(2)
print(mc_ctr5) # => [(3, 4), (2, 3)] => format = [(value, count)]

# subtract(): => subtracts elements from given iterable or mapping => COUNTS CAN BE NEG
# e.g. =>
ctr5.subtract([1, 3, 3, 3]) # => subtracts [1, 3, 3, 3] from [1, 1, 2, 2, 2, 3, 3, 3, 3]
print(ctr5) # => Counter({2: 3, 1: 1, 3: 1})

# ARITHMETIC
# e.g. =>
ctr6 = Counter([1, 2, 2, 3])
ctr7 = Counter([1, 2, 3, 3])
# addition: + => 
ctr_a = ctr6 + ctr7
print("counter a:", ctr_a) # => counter a: Counter({2: 3, 3: 3, 1: 2}) => total 3 2s, 3 3s, 2 1s
# subtraction: - => 
ctr_s = ctr6 - ctr7
print("counter s:", ctr_s) # => counter s: Counter({2: 1})
# intersection: & => only vals shared by both; for each key keeps the min count between the two
ctr_i = ctr6 & ctr7
print("counter i:", ctr_i) # => counter i: Counter({1: 1, 2: 1, 3: 1}) => both share 1 1, 1 2, 1 3
# union: | => keeps all keys; for each key keep the max count between the two
ctr_u = ctr6 | ctr7
print("counter u:", ctr_u) # => counter u: Counter({2: 2, 3: 2, 1: 1})



# Heapq
# Heapq or PRIORITY QUEUE => data structure that allows for quick access to the min (min heap) or max (max heap) elt 
# usually implemented as a binary tree =>
# for min heap: parent node is smaller than child node
# any node i, children are: left = 2 * i + 1; rigth 2 * i + 2
# for max heap: parent node is larger than child node
# in python heaps are usually min-heaps => smallest elt is at the root of the tree
# heapq module allows us to treat list as a heap => giving efficient methods for adding and removing from elts

# creating heap tree:
# import heap module => import heapq
import heapq
# heapq.heapify(): used on a list to rearrange list into heap!!! not create new obj
# e.g. =>
c = [1, 3, 4, 5, 2, 7, 6]
heapq.heapify(c) # => this doesn't sort it simply creates a min-heap
print("heap:", c) # => heap: [1, 2, 4, 5, 3, 7, 6] => this represents heap structure and first elt is always smallest (min-heap)
#           1
#       2       4
#   5   3       7   6

# operations IN HEAPQ MODULE:
# push: heappush(heap, elt) => adds an elt to the heap while maintaining heap property
heapq.heappush(c, 10)
# pop: heappop(heap) => pops and returns the smallest elt from the heap while maintaining heap property
min = heapq.heappop(c)

print(c) # => [2, 3, 4, 5, 10, 7, 6]
print(min) # => 1 => after pop 2 becomes root

# pushpop same time: heappushpop(heap, elt) => pushes elt to heap and pops the smallest from heap => faster than push then pop
heapq.heappushpop(c, 20) # pops 2 which is min and pushes 20
print(c) # => [3, 5, 4, 20, 10, 7, 6]

# find largest: nlargest(n, heap--iterable) => returns the n largest elts from iterable
nlarge = heapq.nlargest(2, c)
print(nlarge) # => [20, 10]

# find smallest: nsmallest(n, heap--iterable) => returns the n smallest elts from iterable
nsmall = heapq.nsmallest(2, c)
print(nsmall) # => [3, 4]

# peek: heap[0] => view the smallest elt to the heap w out removing
csmall = c[0]
print(csmall) # => 3

# replace: heapreplace(heap, elt to replace smallest) => combination of push and pop => pops the smallest from heap and inserts new elt
# useful for replacing smallest with new val => faster than pop then push
heapq.heapreplace(c, 1) # => auto pops smallest
print(c) # => [1, 5, 4, 20, 10, 7, 6]

# merge heaps: heapmerge() => merge multiple sorted iterables into a single heap -> returns an iterator over the sorted (heapified) values
h1 = [1, 5, 3, 2, 10, 8, 20]
heapq.heapify(h1) # => [1, 2, 3, 5, 10, 8, 20]
h2 = [5, 10, 15, 20]
heapq.heapify(h2) # => [5, 10, 15, 20]
print(h1) # => [1, 5, 3, 2, 10, 8, 20]
print(h2) # => [5, 10, 15, 20]
h3 = list(heapq.merge(h1, h2)) # => list converts iterable obj returned from merge into a list
print(h3) # => [1, 2, 3, 5, 5, 10, 8, 10, 15, 20, 20]

# heapify: heapify(list) => converts list to valid heap (min-heap)

# conclusion notes:
# heapq does not support sorting
# no random access
# not thread-safe

# Deque
# Double Ended queue => data structure that allows for adding and removing elts from both ends efficiently
# unlike regular queues which are FIFO; DEQUES support both FIFO AND LIFO
# LEFT IS REAR => RIGHT IS FRONT
# a part of the collections module
from collections import deque

dq = deque(["name", "age", "DOB"])
print(dq) # => deque(['name', 'age', 'DOB'])

# types of restricted deque input
# input restricted deque: insertion is limited at one end while deletion is permitted at both ends
# output restricted deque: insertion is permitted at both ends while deletion is limited at one end

dq2 = deque([1, 2, 3])
# DEQUE OPERATIONS:
# append(x): add x to the right of the deque => O(1)
dq2.append(4)
print(dq2) # => deque([1, 2, 3, 4])

# appendleft(x): add x to the left of the deque => O(1)
dq2.appendleft(0)
print(dq2) # => deque([0, 1, 2, 3, 4])

# pop(): pops elt at the right end of the deque => O(1)
dq2.pop()
print(dq2) # => deque([0, 1, 2, 3])

# popleft(): pops elt at the left end of the deque => O(1)
dq2.popleft()
print(dq2) # => deque([1, 2, 3])

# extend(iterable): extends to the right of the deque by the given iterable => O(k --length of iterable)
dq2.extend([5, 6, 7])
print(dq2) # => deque([1, 2, 3, 5, 6, 7])

# extendleft(iterable): extends to the left of the deque by the given iterable (in reversed order) => O(k --length of iterable)
dq2.extendleft([-2, -1]) # => reversed to [-1, -2]
print(dq2) # => deque([-1, -2, 1, 2, 3, 5, 6, 7])

# remove(val): removes the first occurrence of the val provided from the deque -> ret ValueError if ne => O(n) traverses entire deque
dq2.remove(1)
print(dq2) # => deque([-1, -2, 2, 3, 5, 6, 7])

# rotate(n): rotates the deque n steps to the right (if n is neg then rotate left) => O(k --n number of steps)
dq2.rotate(2)
print(dq2) # => deque([6, 7, -1, -2, 2, 3, 5])
dq2.rotate(-2)

# clear(): removes all elts from deque => O(n) --n number of deletions

# count(val): counts the occurrence of val in deque => O(n) --needs to go through entire deque

# index(val): returns the index of the first occurrence of val in deque => O(n) --worst case need to traverse all of deque

# reverse(): reverse the elts in the deque => O(n) --traverse entire deque
dq2.reverse()
print(dq2) # => deque([7, 6, 5, 3, 2, -2, -1])

# access: dq[index] => access the val at given index in deque => O(1)
# len(): returns the length of the deque => O(1)