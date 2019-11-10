from imports.Person import*
import random

class Student(Person):
    def __init__(self,name,age,major=None):
        Person.__init__(self,name, age)
        self.major=major
    def speak(self):
        r=random.random()
        if r<0.25:
            print("I have Homework")

        if 0.25<=r<0.5:
            print("I need sleep")
        if 0.5<=r<0.75:
            print("I should eat")
        if r>0.75:
            print("I am watching TV")
    def __str__(self):
        return "student:" + str(self.name)+":"+str(self.age)+":"+str(self.major) 