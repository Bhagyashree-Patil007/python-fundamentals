class Car:
    def __init__(self, color):
        self.color = color  # Instance attribute (unique to each object)

car1 = Car("Red")
car2 = Car("Blue")
print(car1.color)  # Output: Red
print(car2.color)  # Output: Blue


# object attribute:
#when class and object attribute are same then object attribute are higher precedence
#class attribute < object attribute
class Car:
    wheels = 4 
    color="orange" # Class attribute 
    def __init__(self, color):
        self.color = color # object attribute >class attribute
car1 = Car("pink")
print(car1.color)  #pink
print(Car.color)   #orange

