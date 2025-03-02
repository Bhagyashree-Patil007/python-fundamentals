#static method:
#methods that don't use the self parameter(work at class level)

class student:
    @staticmethod  #decorator:it is a function which is changing the behaviour of normal function
    def college():
        print("DYPCET")

s1=student()
s1.college()

