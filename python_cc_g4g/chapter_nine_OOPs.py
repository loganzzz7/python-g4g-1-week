# CLASSES
# a class is a user-defined template for creating objects. bundles data and functions together -> easier for use and management
# when we define a class => we define a new type of object
# create a class:
class Dog:
    sound = "bark" # => attribute of a dog object
dog_one = Dog()
print(dog_one.sound) # => bark

# __init__() => this initializes object attributes upon calling class func()
class Cat:
    species = "feline" # class attribute

    def __init__(self, name, sound):
        # instance attribute
        self.name = name
        self.sound = sound

    def meow(self):
        print(f"{self.name} is meowing")

    # this is the default string representing an object
    # w out defining this => returns the addr of reference <__main__.Cat object at 0x104278d70>
    def __str__(self):
        return f"{self.name} likes to {self.sound}"

cat_one = Cat("scoobert", "meow")
print(cat_one.name)
print(cat_one.sound)
print(cat_one.species)
# scoobert
# meow
# feline
cat_one.meow() # => scoobert is meowing
print(cat_one) # => scoobert likes to meow --this is the default string

# modify instance attribute
cat_one.name = "bobbert"

# modify class attribute
Cat.species = "bird"

print(cat_one.name) # => bobbert
print(Cat.species) # => bird

# POLYMORPHISM
# allows functions or methods or operators to behave differently depending on received data type
# python's dynamic typing makes it inherently polymorphic

# python defined functions adapt to many diff types
print(len("Hello"))  # len used on string => 5
print(len([1, 2, 3]))  # len used on int list => 3

print(max(1, 3, 2))  # max used on int tuple => 3
print(max("a", "z", "m"))  # max used on str tuple => z

# functions like add() --let it add two args work on any type of input
# operators like + work on any type of input => addition or string concat

# polymorphism in OOP
# allows methods in different classes to share same name but perform different tasks
# achieved through inheritance
# inheritance (sharing behaviour) & encapsulation(hiding complexity)
# parent class shape
class Shape:
    def area(self):
        return "Undefined"

# child rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# child circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# parent now has two objects => one rectangle; one circle
shapes = [Rectangle(2, 3), Circle(5)]
# the shape method of parent now does area(self) which becomes area(rectangle) and area(circle)
for shape in shapes:
    print(f"Area: {shape.area()}")
    # Area: 6
    # Area: 78.5

# Types of polymophism:
# compile-time polymorphism => java or c++ == behaviour of a function is determined at compliation
# => in python compile-time polymorphism is not natively supported => 
# the polymorphism is therefore instead achieved through dynamic typing & duck typing

# runtime polymorphism => python excels at this == behaviour of a function is determined at runtime
# => method overriding == a child class can redefine a method in it's parent
# the dynamic nature of python lets it excel at runtime polymorphism
# parent class
class Animal:
    def sound(self):
        return "Some generic sound"

# child
class Dog(Animal):
    def sound(self):
        return "Bark"

# child
class Cat(Animal):
    def sound(self):
        return "Meow"

# runtime here
# Polymorphic behavior
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    # the child dog() and cat() update the parent sound method during runtime 
    print(animal.sound())  # (this is inheritance based method overriding) 
    # Bark
    # Meow
    # Some generic sound

# INHERITANCE
# lets child class inherit attributes and methods from parent class => promotes code reuse
# syntax: =>
# class ParentClass:

# class ChildClass(ParentClass): => ChildClass(parent to inherit from)

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

    def speak(self):
        pass  # Placeholder method to be overridden by child classes
# Child class inheriting from Animal
class Cat(Animal):
    # inherits the __init__ method from parent (Animal)
    def speak(self):
        return f"{self.name} meows"  # Override the speak method
cat = Cat("Scoobert")
print(cat.speak()) # => Scoobert meows

# __init__() method:
# inits the object state upon creation
# Parent Class: Person
class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

# Child Class: Employee
class Employee(Person):
    # inherited attributes name and idnumber from parent
    def __init__(self, name, idnumber, salary, post):
        super().__init__(name, idnumber)  # super() method used to call the methods of parent class
        self.salary = salary
        self.post = post
    
    def __str__(self):
        return f"{self.name} has work id {self.idnumber} and makes {self.salary} doing {self.post}"

emp = Employee("scoobert", 123, 12345, "cat mail")
print(emp)

# types of inheritance:
# single inheritance: a child class inherits from one parent class
# e.g. =>
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):  # Employee inherits from Person
    def __init__(self, name, salary):
        super().__init__(name) # employee uses parent's __init__ method
        self.salary = salary
# Single Inheritance
emp = Employee("John", 40000)
print(emp.name, emp.salary) # => John 40000


# multiple inheritance: a child class inherits from more than one parent class
# e.g. =>
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job):  # Inherits from both Employee and Job
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary)  # Initialize Employee => Employee. to use methods from employee
        Job.__init__(self, salary)            # Initialize Job => Job. to use methods from job
# Multiple Inheritance
emp2 = EmployeePersonJob("Alice", 50000)
print(emp2.name, emp2.salary) # => Alice 50000


# multilevel inheritance: a class derived from a class is also derived from another class => grandparent -> parent -> child
# e.g. => 
class Manager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob 
        # => uses methods from employeepersonjob class
        self.department = department
mgr = Manager("Bob", 60000, "HR")
print(mgr.name, mgr.salary, mgr.department) # => Bob 60000 HR


# 4. Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):  # Inherits from EmployeePersonJob
    def __init__(self, name, salary, team_size):
        EmployeePersonJob.__init__(self, name, salary)  # Explicitly initialize EmployeePersonJob 
        # => uses methods from EPJ class
        self.team_size = team_size
asst_mgr = AssistantManager("Charlie", 45000, 10)
print(asst_mgr.name, asst_mgr.salary, asst_mgr.team_size) # => Charlie 45000 10


# hybrid inheritance: a combination of more than one type of inheritance
# e.g. (Multiple + Multilevel) =>
class SeniorManager(Manager, AssistantManager):  # Inherits from both Manager and AssistantManager
    def __init__(self, name, salary, department, team_size):
        Manager.__init__(self, name, salary, department)        # Initialize Manager => uses methods from manager class
        AssistantManager.__init__(self, name, salary, team_size)  # Initialize AssistantManager => uses methods from AM class
sen_mgr = SeniorManager("David", 70000, "Finance", 20)
print(sen_mgr.name, sen_mgr.salary, sen_mgr.department, sen_mgr.team_size) # => David 70000 Finance 20

# ABSTRACT CLASS
# a class that cannot be instantiated on its own => designed to be a blueprint for other classes
# allows for us to define methods that are meant to be implemented by it's sub-classes
# abstract base classes => defines methods that must be implemented by subclasses => 
# so that the subclasses can follow a consistent structure while enforcing abstraction
# ABC (provided by python)
from abc import ABC, abstractmethod
# Define an abstract class
class Animal(ABC): #ABC => abstract base class
    @abstractmethod # sound() is an abstract method, no implementation here --shown via pass
    def sound(self):
        pass 
    @property # for an abstract property
    def species(self):
        pass

# subclass of Animal
class Dog(Animal):
    # in child class --give the implementation of the abstract method
    def sound(self):
        return "Bark"  
    @property # --define the abstract attribute
    def species(self):
        return "Canine"
dog = Dog()
print(dog.sound()) # => bark
print(dog.species) # => Canine
# without a child class => dog = Dog() will return TypeError: Can't instantiate abstract class Animal with abstract method sound()

# ENCAPSULATION
# bundling of data (attributes) and methods (functions) that operate on data into a single unit => typically a class
# restricts access to some components => maintains integrity of data
# hiding internal state of an object and requiring all interactions to be performed through an object's methods
# => provides:
# control over data
# accidental modification of data
# helps modular programming

# python achieves encapsulation through public, protected, and private attributes
# makes it so that a class's methods are available but not its variables.

# data hiding: variables (attributes) are kept private or protected => not accessible outside class but can be modified via methods
# access through methods: methods are the interface through which external code interacts with the data stored in vars => 
#   getters & setters are common methods used to retrieve and update data from protected or private vars
# control & security: class enforce rules on how vars are accessed or modified in only allowing methods to change them => security

# e.g. =>
# balance (private) => modified through deposit or withdraw (public methods)

# protected
class Protected:
    def __init__(self):
        # age in protected can't be modified => it is set from the start
        self._age = 30  # Protected attribute => defined via single _
class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass
obj = Subclass()
obj.display_age()

# private
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute => defined via double __

    def salary(self):
        return self.__salary  # Access through public method
obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError