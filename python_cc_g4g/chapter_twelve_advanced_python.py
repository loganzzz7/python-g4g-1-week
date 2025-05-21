# LIST COMPREHENSION
# list comprehension is a way to create lists using a concise syntax 
# => used to generate new list via applying a function to a given iterable --e.g. list or range
# function: cleaner / more readable code
# SYNTAX: [var expression for var in iterable if condition]
# var expression: transformation of var or val to be included in list
# var = current elt from iterable
# iterable = list, range...
# if condition (optional) = custom filtering condition for when to perform expression
# e.g. =>
a = range(5)
result = [val ** 2 for val in a] # => inline func
print(result) # => [0, 1, 4, 9, 16]
result2 = [val ** 2 for val in a if val % 2 == 0]
print(result2) # => [0, 4, 16]

# difference between for loop and list comprehension:
# for loop = multiple lines; list comp = one line
# transform result2 into for loop =>
result3 = []
for val in a:
    if val % 2 == 0:
        result3.append(val ** 2)
print(result3) # => [0, 4, 16]

# creating list from range
b = [val for val in range(10)]
print(b) # => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# using nested loops
# list comprehension can also be used with nested loops to create lists of tuples
# e.g. =>
result4 = [(x, y) for x in range(2) for y in range(2)]
print(result4) # => [(0, 0), (0, 1), (1, 0), (1, 1)]

# flattening a list of lists
# converting a list of lists [[], [], []] into a single list
lol = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result5 = [val for row in lol for val in row]
print(result5) # => [1, 2, 3, 4, 5, 6, 7, 8, 9]
# each list in lol is referenced by row => first for iterates through the lol list, second for iterates through the lists in lol

# LAMBDA FUNCS:
# syntax: lambda args: expression --e.g. lambda x: x * 2
# e.g. =>
check = lambda num: "Even" if num % 2 == 0 else "Odd"
print(check(20)) # => Even

# notes: (lambda = anonymous funcs)
# lambda can have any number of arguments but only one expression
# lambda functions can be used wherever a function obj is required
# lambda functions are a lambda type object
print(lambda x: x) # => <function <lambda> at 0x10262f740>

# example lambda funcs:
# sum
sum_func = lambda s: sum(int(val) for val in str(s))
print(sum_func(1234)) # => prints 10 
# s = 1234 => str(1234) => iterate over 1234 and for each val convert to int => s = sum int vals
# concat !
concat_func = lambda t: t + "!"
print(concat_func("C + L")) # => C + L!
# filter nums
# string.join(iterable) => this puts a string between every elt of the iterable
fn_func = lambda n: "".join([val for val in n if not val.isdigit()]) 
# => for val in h3ll0 if val is not a digit (this becomes a iterable of [h, l, l]) => join those characters together via "" --empty str
print(fn_func("h3ll0")) # => hll

# differences between lambda and normal functions
# lambda functions can only have one expression
# normal functions require the def stmt
# shouldn't used lambda do to advanced operations

# lambda functions are MOST USEFUL as simple inline functions inside of other functions --e.g. map(), filter(), sorted()...
# review!!
c = ["1", "5", "2", "4", "6", "3", "0"]
d = [(1, "one"), (2, "two"), (3, "three")]
# map(function, iterable) => applies function to iterable => returns an iterable
print("Map 2x to C:", list(map(lambda x: int(x) * 2, c)))
# => Map 2x to C: [2, 10, 4, 8, 12, 6, 0]

# filter(function, iterable) => applies filter function to iterable
print("Filered C for Even:", list(filter(lambda x: int(x) % 2 == 0, c)))
# => Filered C for even: ['2', '4', '6', '0']

# sorted(iterable, key = func to be applied to elts of iterable before sorting --optional, reverse = False --default; optional)
print("Sorted C:", sorted(c, key = lambda x: int(x), reverse = False))
# => Sorted C: ['0', '1', '2', '3', '4', '5', '6']
# => before sorting => apply int(x) to each elt of c

print("Sorted D:", sorted(d, key = lambda x: x[1], reverse = False))
# => Sorted D: [(1, 'one'), (3, 'three'), (2, 'two')]
# => before sorting apply x[1] to each elt of d => sort by the second index of each elt => "one", "two", "three"
# => "th" goes before "tw"

# CONSTRUCTORS
# a special method that is called automatically when an object is created from a class
# init obj instance attributes or state

# __new__(): => constructor that creates new instances of the class
# => this is called before init => allocates memory and returns the new object
# e.g. =>
class ClassName:
    def __new__(cls, params):
        instance = super(ClassName, cls).__new__(cls)
        return instance # => must return an instance type obj of the class or else init won't be called
    # this method is for children classes to inherit and call for obj creation => cls would be child class name
# __init__(): => constructor that sets up the initial attributes or state after creation

# default constructor:
class Car:
    def __init__(self):

        #Initialize the Car with default attributes
        self.make = "Toyota"
        self.model = "Corolla"
        self.year = 2020
# Creating an instance using the default constructor
car = Car()
car.make = "scoobert"
print(car.make)
print(car.model)
print(car.year)

# param constructor:
class Cat:
    def __init__(self, name, sound, specie, size):
        self.name = name
        self.sound = sound
        self.specie = specie
        self.size = size
    
    def __str__(self):
        return f"{self.name} {self.sound}s and is a {self.size} {self.specie}"

cat1 = Cat("scoobert", "meow", "feline", "chubby")
print(cat1) # => scoobert meows and is a chubby feline