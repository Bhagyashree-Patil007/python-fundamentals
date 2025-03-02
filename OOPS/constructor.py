#CONSTRUCTOR:automatically invoked when object is created
#those constructor call which has match the parameter
#types:1.default constructor:when we not created default constructor then automatically python is created default constructor.
#      2.parameterized constructor: which has more parameter other than self parameter


#1.default constructor:
class Student:
    def __init__(self):
        pass

#---------
class Student:
    def __init__(self):
        print(self)#referrence of object(s1)
        print("hii bhagyshree")

s1=Student()
print(s1)#same output as self

# ---------
#2.parameterized constructor:
class Student1:
    def __init__(self,fullname):
        self.name=fullname

s=Student1("Vinay")
print(s.name)

#------------------
class Student1:
    def __init__(self,fullname):
        self.name=fullname

s=Student1("Vinayak")
print(s.name)

#---------------
class Student1:#the condition is only pass one arguments as any name but mostly prefer self parameter
    def __init__(abcd,name,marks):
        #point towords which is new created in object
        abcd.name=name#point parameter name
        abcd.marks=marks

s=Student1("Patil",99)
print(s.name,s.marks)

s2=Student1("Bhagyashree",100)
print(s2.name,s2.marks)



