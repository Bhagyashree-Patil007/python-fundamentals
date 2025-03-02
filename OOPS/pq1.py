class Student:
    def __init__(self,name,marks):#phy_marks,maths,eng):
        self.name=name
        self.marks=marks
        # self.phy=phy_marks
        # self.maths=maths
        # self.eng=eng

#non-static method:use self parameter
    def average(self):
        # avg=(self.marks[0]+self.marks[1]+self.marks[2])/3
        #avg=(self.phy+self.maths+self.eng)/3
        sum=0
        for val in self.marks:
            sum+=val
        
        print("Hi",self.name,"your average score is:",sum/3)

#s1=Student("vinay",99,90,99)
s1=Student("vinay",[99,90,99])
s1.average()

s1.name="Bhagyashree"#update atributes
s1.average()

        
