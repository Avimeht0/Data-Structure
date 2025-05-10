from matplotlib.dviread import Page


class Employee:
    Name="Arvind Mehta"#class attribute
    Language="Python"
    salary=1200000



Arvind=Employee()
Arvind.age=25#Instance atribute or object attribute

print(Arvind.Name,Arvind.Language,Arvind.salary,Arvind.age)


class Programmer:
    Company="Google"#class attribute
    def __init__(self,Name,Language,salary,age):
        self.Name=Name
        self.Language=Language
        self.salary=salary
        self.age=age

Arvind=Programmer("Arvind Mehta","Python",1200000,25)
print(Arvind.Name,Arvind.Language,Arvind.salary,Arvind.age)


class Culculator:
    def getSquare(self,n):
        return n*n
    def getCube(self,n):
        return n*n*n
    def getSquareRoot(self,n):
        return n**0.5
    
A_cul=Culculator()
print(A_cul.getSquare(4))
print(A_cul.getCube(4))
print(A_cul.getSquareRoot(4))

