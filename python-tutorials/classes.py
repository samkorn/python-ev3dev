#!/usr/bin/env python3

# Dog class
class Dog():
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print("Woof! Woof!")
    
    def greet(self):
        print("I am a dog, and my name is " + self.name)


# create a new instance of the Dog object, with the name "Fido"
fido = Dog(name="Fido")

# calls the dog object's methods, bark and greet
fido.bark()
fido.greet()
