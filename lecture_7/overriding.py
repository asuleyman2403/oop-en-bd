class Transport:
    def __init__(self, name):
        self.name = name

    def start_engine(self):
        print("Start Engine")


class Car(Transport):
    def start_engine(self):
        print("Car Engine is starting...")


audi = Car("Audi")
print(audi.name)
audi.start_engine()
