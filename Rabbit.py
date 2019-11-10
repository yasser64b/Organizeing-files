from imports.Animal import *
class Rabbit(Animal):
    def speak(self):
        print('meep')
    def __str__(self):
        return "rabbit:" + str(self.name)+":"+str(self.age)