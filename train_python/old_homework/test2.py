import random
import pandas as pd 
import numpy as np
import turtle as t

def some_name_of_functio():
    t.forward(100)
    t.back(12)

class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} SPEAK")

class Cat(Animal):
    def speak(self):
        return super().speak()
    
cat = Cat("CVa")
cat.speak()

any = Animal("Any")
any.speak()
#t.shape("turtle")
#some_name_of_functio()
#t.exitonclick()