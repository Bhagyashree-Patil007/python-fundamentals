class Student:
    def __init__(self,name):
        self.name=name

s1=Student("Bhagyashree")
print(s1.name)
del s1.name
print(s1.name) #error

#del keyword:used to delete object properties or object itself
print(s1)
del s1
print(s1) #error
