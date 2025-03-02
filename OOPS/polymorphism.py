#polymorphism:EX..,operator overloading
#when the same operator is allowed to have different meaning according to the CONTEXT

#implicit overloading :
print(1+3) #3
print("Vinay"+ "Patil") #Vinay Patil
print([1,2,3]+[4,5,6]) #[1,2,3,4,5,6]

#according to diff-diff data types the meaning of operator are different is called as operator overloading

#explicit overloading :
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real , " i+ ",self.img,"j")

    def __add__(self,num2):
        newReal=self.real+num2.real
        newimg=self.img+num2.img
        return complex(newReal,newimg)
    
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newimg=self.img-num2.img
        return complex(newReal,newimg)
        
num1=complex(1,2)
num1.showNumber()

num2=complex(7,2)
num2.showNumber()

num3=num1+num2
num3.showNumber()

num3=num1-num2
num3.showNumber()


