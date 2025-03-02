class Student:
    def __init__(self,name,fullname):
        self.name=name
        self.marks=fullname

    def welcome(self):
        print("welcome",self.name)
    
    def get_marks(self):
        return self.marks

s1=Student("Bhagyahsree",99)
s1.welcome()
print("marks:",s1.get_marks())