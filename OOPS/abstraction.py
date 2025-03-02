#ABSTRACTION: hiding the implementation details of a class and only showing the essential features to the user

class car:
    def __init__(self):
       #hide implementation detail
        self.acc=False
        self.brk=False
        self.clutch=False
    
    def start(self):
        self.acc=True
        self.clutch=True
        #show essential detail
        print("car started...")

car1=car()
car1.start()