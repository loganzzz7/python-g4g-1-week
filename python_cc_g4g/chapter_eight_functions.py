# FUNCTIONS
# syntax:
# def func_name(param):
#   stmt
#   return expression

# can specify return type => python 3.5+
# def func_name(num_one: int, num_two: int) -> int:
#   '''this func adds two numbers'''
#   num_three = num_one + num_two
#   return num_three

# some more functions
# def is_prime(n):
#     if n in [2, 3]: => 2 and 3 are prime
#         return True
#     if (n == 1) or (n % 2 == 0): => if n is 1 or divisible by 2 == not prime
#         return False
#     r = 3
#     while r * r <= n: => if n bigger than square of 3
#         if n % r == 0: => n/r has no remainder
#             return False
#         r += 2
#     return True
# print(is_prime(78), is_prime(79))

# default arg => def my_func(x, y = 10): == y is defaulted to 10 unless provided new val in func call
# once we have a default arg; all elts to the right of the default arg must have default val as well

# when calling a func the order of the args don't matter ONLY IF keyword args are used => e.g.
# def my_func(x, y):
# my_func(y = 2, x = 1) == my_func(1, 2)

# can pass a var number of args into func via *argv & **kwargs
# *argv: multiple non-keyword args
# e.g. =>
# def my_func(*argv):
#   for arg in argv:
#       print(arg)
# my_func("hello", "world", "hi")

# **kwargs: multiple keyword args
# e.g. =>
# def my_func(**kwargs):
#   for key, val in kwargs.items():
#       print("%s == %s" % (key, val)) => same as print(f"{key} == {val}")

# Print doc string:
# e.g. =>
def print_x(x):
    '''this function prints out inputed var''' # this is doc string .__doc__
    print(x)

print(print_x.__doc__) # => this function prints out inputed var

# nested func
# e.g. =>
def func_one(x):
    def func_two(x):
        print(x)
    func_two(x)
func_one(2) # => 2

def func_one():
    x = 12
    def func_two(): # this is inner func => has access to vars from parent func (func_one)
        print(x)
    func_two()
func_one() # => 12

# anonymous functions =>
def m_three(x): return x*x*x # => normal function
mult_three = lambda x: x*x*x # => anonymous function == w out name

print(m_three(3)) # => 27
print(mult_three(3)) # 27

# recursive functions:
def recursive_func_fac(x):
    # base case
    if x == 0:
        return 1
    # recursive case
    else:
        return x * recursive_func_fac(x - 1)
print(recursive_func_fac(3)) # => 3 * 2 * 1 => 6

# pass by reference:
# every var is a reference
def update_list(x):
    x[0] = 12
    return x

li = [1, 2, 3, 4, 5]
# when pass in li to update_li => x becomes a reference to li =>
# therefore can update the first val of li since x points to where li is 
print(update_list(li)) # => [12, 2, 3, 4, 5]

# pass by value:
def pass_by_val(x):
    # this changes the received reference x to something else => connection between x and passed in li is broken
    x = [1, 2, 3] # inside this function => the name x becomes a reference to the list [1, 2, 3]
li_2 = [5, 6, 7, 8, 9]
pass_by_val(li_2)
print(li_2) # outside of the function, li_2 still references to the original list [5, 6, 7, 8, 9]
# [5, 6, 7, 8, 9]

# exercise:
def swap(x, y):
    # temp is a ref to x
    temp = x
    # x inside this function is a ref to y
    x = y
    # y inside this function is a ref to temp which is a ref to x
    y = temp
    print(x, y) # => 3 2 inside of function the two vals are swapped
    # return x, y => this helps preserve the vals in the function otherwise python does not alter the vars outside of func

# Driver code
x = 2
y = 3
swap(x, y)
print(x) # => 2
print(y) # => 3
# outside of func, x and y stay same since pass by val does not update

# MAP
# used to apply a function to every val of an iterable & returns a map object
# syntax map(func, iterable)
# e.g. =>
s = ["1", "2", "3"]
update = map(int(), s) # => does int() to every val of s
print(update) # <map object at 0x100ed04f0>
print(list(update)) # => [1, 2, 3]

# using lambda
z = [1, 2, 3]
update_2 = map(lambda x: x*2, z)
print(list(update_2)) # => [2, 4, 6]

# lambda with multiple param
y = [4, 5, 6]
update_3 = list(map(lambda x, y: x + y, z, y))
print(update_3) # => [5, 7, 9]

# uppercase
x_str = ["hello", "world"]
update_4 = list(map(str.upper, x_str))
print(update_4) # => ['HELLO', 'WORLD']

# rmv white space
w_str = [" hello "]
print(w_str) # => [' hello ']
update_5 = list(map(str.strip, w_str))
print(update_5) # => ['hello']

# FILTER
# syntax = filter(function, iterable) => return iterable after running function on it
# function must be one that returns a boolean val => returned iterable only contains the elts in provided iterable which return true
# used for filtering vs map used for transforming
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
filtered = filter(lambda x: x%2 == 0, numbers)
print(list(filtered)) # => [2, 4, 6, 8]