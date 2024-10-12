"""class Elevator:
    def __init__(self, starting_floor):
        self.make = "The elevator company"
        self.floor = starting_floor

elevator = Elevator(8)
print(elevator.make)
print(elevator.floor)"""

class Car:
    def __init__(self):
        self.color = "Red" # ends up on the object
        self.make = "Mercedes" # becomes a local variable in the constructor

car = Car()
print(car.color) # "Red"
print(car.make) # would result in an error, `make` does not exist on the object