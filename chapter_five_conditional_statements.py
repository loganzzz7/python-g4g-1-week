# IF ELSE:
a = 10
if a > 5:
    print("yes")
else:
    print("no")

# one line form:
result = "one" if a < 10 else "two"
print(result)

# elif => e.g.
if a == 2:
    print("2")
elif a == 9:
    print("9")
else:
    print("10")



# SWITCH STMT:
# three different methods => no direct switch statement
# one: uses dictionary to keep cases rather than directly in switch stmt like in C
# e.g. =>
switch_cases = {
    0: "case_one",
    1: "case_two",
    2: "case_three",
}
# return switch_cases.get(argument, "default_case")

# two: use if elif else
# three: use class
# e.g. =>
class switich_stmt_class_python:
    def day(self, month):
        default = "incorrect day" # => instance attribute
        return getattr(self, "month_" + str(month), lambda: default)()
    # getattr() attempts to retrieve an attribute (a method in this case) named "month_" + input 
    # getattr(o: object, name: str, default) => same as o.name
    # from the current instance of the class (self)
    # if such a method exists it calls it
    # else it returns the default function lambda: default
    # () at the end calls the method => 
    # getattr(self, "month_" + str(month), lambda: default) becomes => month_one 
    # => () after which calls month_one
    
    def month_one(self):
        return "jan"
    
    def month_two(self):
        return "feb"
    
    def month_three(self):
        return "mar"
    
my_switch = switich_stmt_class_python() #object of switich_stmt_class_python class

print(my_switch.day("one"))
print(my_switch.day("three"))

# four: ONLY IN PYTHON 3.10 & newer
def switch_with_match(argument):
    match argument:
        case 0:
            return "case_zero"
        case 1:
            return "case_one"
        case 2:
            return "case_two"
        case default: 
            return "default"

option = switch_with_match(2)
option_two = switch_with_match("default")
print(option)
print(option_two)