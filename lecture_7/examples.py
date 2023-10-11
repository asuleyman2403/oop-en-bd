class Animal:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        print("Something voice")


class Cat(Animal):
    pass
    # def make_sound(self):
    #     print("Meow")


class Dog(Animal):
    def make_sound(self):
        print("Woof")

class Car:
    def make_sound(self):
        print("Wroom Wroom")


def make_sound(sound_maker):
    sound_maker.make_sound()

sound_makers = [Dog("Bobik"), Cat("Barsik"), Car()]

for sound_maker in sound_makers:
    # Duck typing
    make_sound(sound_maker)



