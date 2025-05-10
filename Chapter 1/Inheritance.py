class Company:
    def __init__(self):
        self.CompanyName="Google"
        self.CompanyLocation="California"

    def Info(self):
        print(f"Company Name :{self.CompanyName} and the location of the company is {self.CompanyLocation}")

class Employee(Company):
    def __init__(self, Name, salary):
        super().__init__()
        self.Name=Name
        self.salary=salary

    def Info(self):
        print(f"Employee Name :{self.Name} and the salary of the employee is {self.salary}")
        super().Info()
Arvind=Employee("Arvind Mehta",1200000)
Arvind.Info()



class  TwoDVector:
    def __init__(self,i,j):
        self.i=i 
        self.j=j
    def show(self):
        print(f"i={self.i} and j={self.j}")


class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k
    def show(self):
        print(f"i={self.i} and j={self.j} and k={self.k}")


A=TwoDVector(1,2)
A.show()                    
B=ThreeDVector(1,2,3)
B.show()

class Animal:
    def __init__(self,Name,Age):
        self.Name=Name
        self.Age=Age
    def Info(self):
        print(f"Name of the animal is {self.Name} and the age of the animal is {self.Age}")

class Pets(Animal):
    def __init__(self,Name,Age,Type):
        super().__init__(Name,Age)
        self.Type=Type
    def Info(self):
        super().Info()
        print(f" and the type of the animal is {self.Type}")

class Dogs(Pets):
    def __init__(self,Name,Age,Type,Color):
        super().__init__(Name,Age,Type)
        self.Color=Color
    def Info(self):
        super().Info()
        print(f" and the color of the dog is {self.Color}")

A=Animal("Dog",2)
A.Info()
B=Pets("Dog",2,"Pet")
B.Info()
C=Dogs("Dog",2,"Pet","Black")
C.Info()