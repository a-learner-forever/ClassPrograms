from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod #decorator
    def sound(self):
        pass

    def breathing(self):
        print("All animals breathe.")   

class Dog(Animal):
    def sound(self):
        print("Bark!")

class Cat(Animal):
    def sound(self):
        print("Meow!")
# a = Animal()
# a.sound()
d = Dog() #instantiation
d.sound()       
d.breathing()   

c=Cat()
c.sound()

