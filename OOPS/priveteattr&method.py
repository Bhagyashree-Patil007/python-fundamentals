#private(like) attributes and methods: privete attributes and methods are meant to be used only within the class and are not accessible from outside the class
#for making private used prefix as double underscore ex.,,__acc_pass
class Account:
    #private attributes:
    __name="vinay"
    
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

    #private method:these type of method used for within same class others methods are call or print these method
    #used other internal class  function (methods)
    def __hello(self):
        print("hello!")


    def welcome(self):
        self.__hello()

        
acc1=Account("12345","123asd")

print(acc1.reset_pass()) #No Error due to private methods and attributes are accesible inside class (for differant methods )
print(acc1.welcome()) #no error
print(acc1.__hello())#error due to private method
print(acc1.__name) #error due to private attributes
print(acc1.__acc_pass()) #error due to private methods and attributes are not accesible outside the class