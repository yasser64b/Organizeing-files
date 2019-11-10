from imports.Animal import *
class Person(Animal):
    def __init__ (self, name, age):
        Animal.__init__ (self, age)
        Animal.set_name(self, name)
        self.friends =[]
    def get_friends(self):
        return self.friends
    def add_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak (self):
        print("HELLO")
    def age_diff (self, other):
        diff=self.get_age() -other.get_age()
        if self.age > other.age:
            print(self.name , "is", diff , "years older than " , other.name)
        else:
            print(self.name , "is", -diff , "years younger than " , other.name)
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)