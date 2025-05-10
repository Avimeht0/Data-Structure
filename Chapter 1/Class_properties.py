#A class method is a method that gets the class itself (cls) as the first argument, not an instance (self).

from numpy import imag


class Dog:
    dogs_created = 0

    def __init__(self, name):
        self.name = name
        Dog.dogs_created += 1

    @classmethod
    def get_dog_count(cls):
        return cls.dogs_created

# Usage
dog1 = Dog("Max")
dog2 = Dog("Bella")
print(Dog.get_dog_count())  # Output: 2


# property Decorator Turns a method into a "read-only" attribute. 
# When you want to calculate a value or control access to a variable but access it like a normal attribute.

#Imagine a class where you store someone's birth year.
#  You want to calculate their age. Instead of calling person.get_age(), you want to just say person.age – like a simple variable.

class Person:
    def __init__(self, birth_year):
        self.birth_year = birth_year

    @property
    def age(self):
        return 2025 - self.birth_year

# Usage
p = Person(2000)
print(p.age)  # prints: 25


### Getter and Setter – Control access to variables
#You want to protect a variable and control what values go in or out.


class Student:
    def __init__(self):
        self._name = None
        self._age = None
        self._class_name = None

    # --- Name ---
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty")
        self._name = value

    # --- Age ---
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 5 or value > 100:
            raise ValueError("Age must be between 5 and 100")
        self._age = value

    # --- Class name ---
    @property
    def class_name(self):
        return self._class_name

    @class_name.setter
    def class_name(self, value):
        if not value.startswith("Class"):
            raise ValueError("Class name must start with 'Class'")
        self._class_name = value
s = Student()

# Try setting values with rules:
s.name = "Ravi"               # ✅ OK
s.age = 20                   # ✅ OK
s.class_name = "Class 10"    # ✅ OK

# Try wrong values:
# s.name = ""                # ❌ Error: Name cannot be empty
# s.age = 3                 # ❌ Error: Age must be between 5 and 100
# s.class_name = "10A"      # ❌ Error: Class name must start with 'Class'

print(s.name, s.age, s.class_name)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # overload +
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):  # for printing nicely
        return f"({self.x}, {self.y})"

# Usage
p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1)
p3 = p1 + p2
print(p3)   # Output: (4, 6)



class ComplexNumber:
    def __init__(self, real,imaginary):
        self.real=real
        self.imaginary=imaginary 

    #Addition: (a+bi)+(c+di)=(a+c)+(b+d)i 

    def __add__(self,other):
        real=self.real+other.real
        imaginary=self.imaginary+other.imaginary
        return ComplexNumber(real,imaginary)
    
    def __str__(self):
        return f"{self.real}+{self.imaginary}i"
    #Multiplication: (a+bi)(c+di)=(ac−bd)+(ad+bc)i (using i^2 =−1)

    def __mul__(self,other):

        real=self.real*other.real-self.imaginary*other.imaginary
        imaginary=self.real*other.imaginary+self.imaginary*other.real
        return ComplexNumber(real,imaginary)
    
C=ComplexNumber(1,2)
D=ComplexNumber(3,4)
print(C+D)
print(C*D)
    
