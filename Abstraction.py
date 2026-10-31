from abc import ABC,abstractmethod

# Abstract class
# ABC stands for Abstract Base Class. We can not change that name
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def stop_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

car = Car()
car.start_engine()
car.stop_engine()
