# Class attribute :shared across all instances of the class
class Car:
    wheels = 4  # Class attribute (shared by all instances)

car1 = Car()
car2 = Car()
print(car1.wheels)  # Output: 4
car1.wheels = 6  # This creates an instance attribute, doesn't change the class attribute
print(car1.wheels)  # Output: 6
print(car2.wheels)  # Output: 4 (Unchanged)



