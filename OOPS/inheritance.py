#INHERITANCE: when one class (child/derived) derives the properties and methods of another class (parent/base)

#SINGLE-LEVEL INHERITANCE:
class Car:
    color="black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("Fortuner")
car1=ToyotaCar("prius")

print(car1.name)
#inherited properties:
print(car1.start())
print(car1.stop())
print(car1.color)

#MULTI-LEVEL INHERITANCE: 
class Car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type=type

car1=Fortuner("diesel")
car1.start()
        
#MULTIPLE INHERITANCE:
#BASE CLASS1:
class A:
    varA="welcome to class A"
#BASE CLASS2:
class B:
    varB="welcome to class B"
#CHILD CLASS:inherites properties of two or more base class
class C(A,B):
    varC="welcome to class C"

c1=C()
print(c1.varC)
print(c1.varB)
print(c1.varA)