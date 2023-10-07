from abc import ABC, abstractmethod

class Transport(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def drive(self):
        pass

# transport = Transport("Some transport") Type Error

class Car(Transport):
    # implement all abstract method to make class exact
    # def start_engine(self):
    #     print("I started engine")

    def drive(self):
        print("Wroom Wroom")

class Sedan(Car):
    def start_engine(self):
        print("I started engine")


# car = Car("Audi")
# car.drive()
# car.start_engine()

sedan = Sedan("Audi")
sedan.drive()
sedan.start_engine()
print(sedan.name)



