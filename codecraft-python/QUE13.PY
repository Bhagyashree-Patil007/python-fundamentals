#13. Implement program to perform arithmetic operation using function? 
class arith_operations:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2

    def add (self):
        result=self.num1+self.num2
        print("Addition is : ",result)

    def sub (self):
        result=self.num1-self.num2
        print("Subtraction is : ",result)

    def mul (self):
        result=self.num1*self.num2
        print("Multiplication is : ",result)

    def div (self):
        result=self.num1/self.num2
        print("division is : ",result)

    def Modulo (self):
        result=self.num1%self.num2
        print("Modulo is : ",result)

obj=arith_operations(12,5)
obj.add()
obj.sub()
obj.mul()
obj.div()
obj.Modulo()

