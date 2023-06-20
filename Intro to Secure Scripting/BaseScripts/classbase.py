class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

    def introduce(self):
        print(f"My name is {self.name} and I'm a {self.breed} dog.")
#can be called in the same script by reffrencing it or in a diffrent file by uisng import (name of file) as 
(what to refer to it as)
