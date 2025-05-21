# Python Exception Handling
# handles errors that occur during the execution of a program => exception handling allows for response to error
# instead of crashing program go to exception case => enables catching and managing errors

# handling a simple exception in python --div by zero:
a = 10
try:
    result = a / 0
except ZeroDivisionError:
    print("cannot div by zero")
# instead of error => go into except route & prints cannot div by zero

# differences between exception and error:
# errors => serious issues that a program SHOULD NOT try to handle => e.g. syntax, memory error...
# exceptions => less serious and can be handled by program => occur due to invalid input, missing files, network issues...

# try exception syntax:
# try:
#   block of code that may raise an exception
#   !!Python will try to execute this block to test for errors => if there is an exception -> go to except: block
# except SomeException:
#   print out type of error
#   !!This block handles the error that was raised; catches the exception; try catch in c++
# else:
#   what to do if there was no exception
#   !!THIS BLOCK IS OPTIONAL; this only runs if there was no error in the try block and the code does not jump to the except block
#   !!Defines what happens if the try block succeeds w out an error
# finally:
#   code for whether or not exception occurs
#   !!This block ALWAYS run regardless of whether there was an error or not => typically used for clean up operations
#   !!e.g. => closing files, releasing resources

# Overall e.g.:
try:
    b = 0
    result2 = 100 / b
except ZeroDivisionError:
    print("cannot div by zero")
except ValueError:
    print("please provide a valid input")
else:
    print("result: " + result2)
finally:
    print("done")
# output:
# cannot div by zero
# done

# Common Exceptions:
# BaseException: base class for all exceptions => this is the base class for all exceptions
try:
    raise BaseException("This is BaseException")
except BaseException as e:
    print(e)
# also catches system exceptions --e.g. SystemExit; KeyboardInterrupt
# e.g. =>
# try:
#     result3 = 100 / 0
# except BaseException as e:
#     print(f"Exception: {type(e).__name__}") 
#     => type(e) prints out the type of exception; .__name__ = built in func to print str of name

# Exception: sub-class of BaseException => more commonly used for catching all exceptions (NOT INCLUDING EXIT EXCEPTIONS)
# ArithmeticError: Base class for all errors related to arithmetically based errors
# ZeroDivisionError: Raised when a division OR MODULO operation is performed with 0 as the divisor
# OverflowError: Raised when a numerical operation exceeds the maximum limit of a data type
#   => python ints have arbitrary precision so overflow doesn't occur
#   => floating point numbers are still IEEE floating point numbers => same possibility to overflow 32 / 64 bit floating point numbers
#   => numpy class has fixed-size data types => np.int32 or np.float32
import math

try:
    result4 = math.exp(1000)
except OverflowError as e:
    print(e) # => math range error

# FloatingPointError: Raised when floating point op fails => can be due to overflow or convert to float
# AssertionError: Raised when assertion stmt fails
#   => an assertion stmt is a debugging aid that tests whether a condition is true => syntax: assert condition, optional_msg
#   => example stmt: assert b != 0, "Division by Zero Error" --> if stmt == False then print msg => if b = 0 then False
try:
    assert 1 == 2, "assertion failed"
except AssertionError as e:
    print(e) # => assertion failed

# AttributeError: Raised when an attribute reference or assignment fails 
# e.g. => when accessing a class attribute that has not been defined
class test_class():
    pass
test_obj = test_class()
try:
    test_obj.name
except AttributeError as e:
    print(e) # => 'test_class' object has no attribute 'name'

# IndexError: Raised when accessing out of bounds => sequence subscript is out of range
test_li = [1, 2, 3]
try:
    test_li[4]
except IndexError as e:
    print(e) # => list index out of range

# KeyError: Raised when a dictionay key is not found
test_dict = {1: "one", 2: "two"}
try:
    test_dict[3]
except KeyError as e:
    print(f"{type(e).__name__}: {e}") # => KeyError: 3

# MemoryError: Raised when an operation runs out of memory 
# => python has garbage collector so memory leak uncommon but can be a cause
# => inf recursions
# => creating objs larger than memory can contain --very large string or list init
# try:
#     li = [1] * (10**10)
# except MemoryError as e:
#     print(e) # => memory error

# NameError: Raised when a local or global var is not found
try:
    print(ne)
except NameError as e:
    print(e) # => name 'ne' is not defined

# OSError: Raised when a system-related operation (e.g. --file I/O) fails
try:
    open("nefile.txt")
except OSError as e:
    print(e) # => [Errno 2] No such file or directory: 'nefile.txt'

# TypeError: Raised when an operation or function is applied to an object of inappropriate type 
# --e.g. c: expecting an int input but receiving a str
try:
    result5 = "2" + 2
except TypeError as e:
    print(e) # => can only concatenate str (not "int") to str

# ValueError: Raised when a function received an input of the valid type but inappropriate value
try:
    result6 = int("hello")
except ValueError as e:
    print(e) # => invalid literal for int() with base 10: 'hello'

# ImportError: Raised when an import stmt has issues => would catch it in the top of the file when importing modules
try:
    import nemod
except ImportError as e:
    print(e) # => No module named 'nemod'

# ModuleNotFoundError: Raised when a module cannot be found => if using a module that has not been imported
# KeyboardInterrupt: ctr + c
try:
    while True:
        pass
except KeyboardInterrupt as e:
    print(f"{e}: keyboard interrupt") # => ^C: keyboard interrupt

# SystemExit
import sys
try:
    sys.exit()
except SystemExit as e:
    print(f"{type(e).__name__}") # => SystemExit

# Python catching exceptions
# catching multiple exceptions:
# e.g. =>
c = ["10", "twenty", 30]
try:
    result3 = int(a[0]) + int(a[1])
# except (ValueError, TypeError) as e:
#     if (TypeError):
#         print(f"Type error: {e}") # => Type error: 'int' object is not subscriptable => e can be both type or value error; in this case TypeError
#     elif (ValueError):
#         print(f"Value error: {e}")
# except IndexError:
#     print("index error")
except Exception as e:
    print(f"{type(e).__name__}: {e}") # => TypeError: 'int' object is not subscriptable use exception to catch all exceptions
finally:
    print("Done")

# Raise an exception:
# raise an exception via: raise ExceptionType("Error Msg")
# can choose built-in exceptions or self-defined exceptions --inherited from Exception class
# e.g. =>
def set(age):
    if age < 0:
        raise ValueError("age cannot be neg")
    else:
        print(age)

try:
    set(-5)
except ValueError as e:
    print(f"{type(e).__name__}") # => ValueError

# DISADVANTAGES:
# performance overhead: 
# => slower to use try exception to catch errors than conditional stmts as ti requires interpreter to perform additional work
# possibly security risks:
# => improperly handled exceptions could reveal sensitive info and create security vulnerabilities
# => e.g. if the following are revealed in error prints
# Stack traces; File paths; Internal variable names; SQL queries; System configuration
# => FIX: write errors to a secure file instead of to the cmdline and only generic "error msg" to cmdline & viewable by users

# User-defined exceptions
# created by inheriting the Exception class => custom errors that handle custom scenarios
# STEPS:
# define a new exception class -> create a new class that inherits from Exception
# raise the exception -> use raise stmt to raise the custom scenario for exception
# handle the exception -> use try-except blocks to handle the exception

# e.g. =>
class InvalidInputError(Exception):
    def __init__(self, val, msg = "Value must be between 0 and 20", error_code = 0): #init attributes of instances
        self.val = val # instance has custom val attribute
        self.msg = msg # instance has custom msg attribute
        self.error_code = error_code
        super().__init__(self.msg)
        # the Exception base class is designed to:
        # store a message that can be displayed when the exception is printed
        # calling super().__init__(self.msg) => registers the msg defined in custom exception to be registered to parent Exception
        # inits base Exception with msg


    def __str__(self):
        return f"Error Code {self.error_code}: {self.val} -> {self.msg}" # custom string when print instance of this class

d = 30
def set_val(val):
    if val < 0 or val > 20:
        raise InvalidInputError(val)
    else:
        print(f"val provided: {val}")

try:
    set_val(d)
except InvalidInputError as e:
    print(f"Error: {type(e).__name__}; {e}") 
    # => Error: InvalidInputError; Error Code 0: 30 -> Value must be between 0 and 20
    # => Error Code 0: 30 -> Value must be between 0 and 20 (this is the custom defined str printed out when printing InvalidInputError)

# Network Error as a subclass of ->  RuntimeError; this is a standard exception that is raised when the error does not fall into any class
class NetworkException(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise NetworkException("error")
except NetworkException as e:
    print(e.args) # => ('e', 'r', 'r', 'o', 'r')