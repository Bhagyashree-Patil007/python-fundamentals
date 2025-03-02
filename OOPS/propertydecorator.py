#PROPERTY : we use @property decorator on any method in the class to use the method as a property
class student:
    def __init__(self,phy,chem,maths):
        self.phy=phy
        self.chem=chem
        self.maths=maths

    @property #automatically reflect the change in any other parameter
    def percentage(self): #return calculated of latest value
        return str((self.phy+self.chem+self.maths)/3) + "%"
    
c1=student(98,97,99)
print(c1.percentage)

c1.phy=86
print(c1.percentage)

