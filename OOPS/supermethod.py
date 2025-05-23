#SUPER(): super() method is used to access methods of the parents class
class Car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
        super().start()

car1=ToyotaCar("Prius","electric")
print(car1.type)