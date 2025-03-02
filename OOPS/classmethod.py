#class method:a class method is bound to the class and receives the class as an implicit first arguments

#change name in method

#1.--------------no change
class Person:
    name="Anjali"
    def changeName(self,name):
        self.name=name

p1=Person()
p1.changeName("Rahul")
print(p1.name) #Rahul
print(Person.name) #Anjali


#2.-----change
class Person:
    name="Anjali"
    def changeName(self,name):
        Person.name=name

p1=Person()
p1.changeName("Rahul")
print(p1.name) #Rahul
print(Person.name) #Rahul

#3.-------using class
class Person:
    name="Anjali"
    def changeName(self,name):
        #jisbhi object ki hum class ke undar change karana chahte hai usaki hum class ko access kar sakte hai
        self.__class__.name=name
             #Person class
p1=Person()
p1.changeName("Rahul")
print(p1.name) #Rahul
print(Person.name) #Rahul

#4.-------using class method
class Person:
    name="Anjali"

    @classmethod  # directly change into class attibutes
    def changeName(cls,name):
        cls.name=name

p1=Person()
p1.changeName("Rahul")
print(p1.name) #Rahul
print(Person.name) #Rahul